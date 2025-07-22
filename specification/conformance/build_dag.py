#!/usr/bin/env python3
import json
from graphviz import Digraph
import logging
import argparse
import sys

def init_logger(level):
    # Create a logger instance
    logger = logging.getLogger(__name__)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    match level:
        case 'DEBUG':
            logger.setLevel(logging.DEBUG)
        case 'INFO':
            logger.setLevel(logging.INFO)
        case 'WARNING':
            logger.setLevel(logging.WARNING)
        case 'ERROR':
            logger.setLevel(logging.ERROR)
        case 'CRITICAL':
            logger.setLevel(logging.CRITICAL)
        case _:
            logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def get_args():
    parser = argparse.ArgumentParser(description='SCR Graph Generator.')
    parser.add_argument('-t', '--table-name', default="FOCUS", help='Table to generate SCR graph for')
    parser.add_argument('--include-checks', action='store_true', help='Add checks to graph')
    parser.add_argument('--include-attributes', action='store_true', help='Add attributes to graph')
    parser.add_argument('-f', '--scr-filename', type=str, default='scr-1.2.json', help='SCR definition filename to load')
    parser.add_argument('--dot-filename', type=str, default='scr_graph.dot', help='Output SCR graph dot filename')
    parser.add_argument('--png-filename', type=str, default='scr_graph.png', help='Output SCR graph png filename')
    parser.add_argument('--logging-level', type=str, default='WARNING', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    parser.add_argument('--start-at', type=str, default=None, help='Start the graph at a specific item')
    return parser.parse_args()
    

class SCR:
    def __init__(self, scr_filename, table_name, logger, include_checks=True, include_attributes=False, start_at=None):
        self.scr_filename = scr_filename
        self.table_name = table_name
        self.include_checks = include_checks
        self.include_attributes = include_attributes
        self.scr_definition = {}
        self.SCRGraph = SCRGraph(graph_name=f'{self.table_name} Table Conformance DAG', logger=logger)
        self.logger = logger
        self.start_at = start_at

    def __load_scr_definition(self):
        if not self.scr_definition:
            # Load SCR JSON
            with open(self.scr_filename, "r") as f:
                self.scr_definition = json.load(f)

    def __add_check_item(self, requirement, rule_id):
        
        check_function = requirement.get("CheckFunction", None)
        if check_function in {'OR', 'AND'}:
            for item in requirement.get("Items", []):
                self.__add_check_item(item, rule_id)
        elif check_function == "CheckSCR":
            target = requirement.get("SCR", None)
            if target:
                self.SCRGraph.add_node(target, custom_data=self.scr_definition['ConformanceRules'].get(target, {}))
                self.SCRGraph.add_edge(rule_id, target)
                self.__traverse_dependencies(target)
        else:
            if self.include_checks:
                self.SCRGraph.add_node(check_function, custom_data=self.scr_definition['CheckFunction'].get(check_function, {}))
                self.SCRGraph.add_edge(rule_id, check_function)
                self.__traverse_check_attributes(check_function)
            else:
                self.logger.warning(f'Skipping {check_function} checks is disabled') 

    def __traverse_check_attributes(self, check_id):
        if not self.include_attributes:
            self.logger.warning(f'Skipping {check_id} attribute checks is disabled')
            return
        
        check_function = self.scr_definition["CheckFunction"].get(check_id, {})
        if not check_function:
            self.logger.warning(f'Skipping {check_id} check not found')
            return

        for attribute in check_function.get('FormatAttributes', []):
            self.SCRGraph.add_node(attribute, custom_data=self.scr_definition['ConformanceRules'].get(attribute, {}))
            self.SCRGraph.add_edge(check_id, attribute)
            self.__traverse_dependencies(attribute)

    def __traverse_dependencies(self, rule_id):
        self.logger.info(f'traversing {rule_id}')
        rule = self.scr_definition["ConformanceRules"].get(rule_id, {})
        requirement = rule.get("ValidationCriteria", {}).get("Requirement", {})
        if requirement:
            check_function = requirement.get("CheckFunction", None)
            if check_function:
                self.__add_check_item(requirement, rule_id)
        for rule_depenency in rule.get("ValidationCriteria", {}).get("Dependencies", []):
            self.SCRGraph.add_edge(rule_id, rule_depenency)

    def load_graph(self):
        self.__load_scr_definition()
        if self.start_at:
            rule = self.scr_definition["ConformanceRules"].get(self.start_at)
            if not rule:
                self.logger.error(f'Provided --start-at rule "{self.start_at}" not found in ConformanceRules')
                return
            self.SCRGraph.add_node(self.start_at, custom_data=rule)
            self.__traverse_dependencies(self.start_at)
        else:
            table_data = self.scr_definition["ConformanceTables"].get(self.table_name, {})
            self.SCRGraph.add_node(f"Table: {self.table_name}", shape='box', custom_data=table_data)
            for rule_id in self.scr_definition["ConformanceTables"][self.table_name]["ConformanceRules"]:
                self.SCRGraph.add_node(rule_id, custom_data=self.scr_definition['ConformanceRules'].get(rule_id, {}))
                self.SCRGraph.add_edge(self.table_name, rule_id)
                self.__traverse_dependencies(rule_id)

    def generate_dot_file(self, dot_filename):
        self.SCRGraph.render(dot_filename, format_type="dot")
    
    def generate_png_file(self, png_filename):
        self.SCRGraph.render(png_filename, format_type="png")


class SCRGraph:
    def __init__(self, graph_name, logger):
        self.graph_name = graph_name
        self.dot = None
        self.__init_dot()
        self.added_nodes = set()
        self.added_edges = set()
        self.logger = logger

    def __init_dot(self):
        # Initialize the DOT graph
        self.dot = Digraph(comment=self.graph_name)
        self.dot.attr(overlap='false')

    def add_node(self, node_id, custom_data=None, label=None, shape='ellipse'):
        if node_id not in self.added_nodes:
            self.logger.info(f'Adding node: {node_id}')
            if custom_data:
                self.dot.node(node_id, label or node_id, shape=shape, customData=json.dumps(custom_data))
            else:
                self.dot.node(node_id, label or node_id, shape=shape)
            self.added_nodes.add(node_id)

    def add_edge(self, src, dst):
        edge = (src, dst)
        if edge not in self.added_edges:
            self.logger.info(f'Adding edge: {src} -> {dst}')
            self.dot.edge(src, dst)
            self.added_edges.add(edge)

    def render(self, filename, format_type):
        self.dot.render(filename.replace(f'.{format_type}', ''), format=format_type, cleanup=True)

if __name__ == '__main__':
    args = get_args()

    logger = init_logger(args.logging_level)
    scr = SCR(scr_filename = args.scr_filename,
              table_name=args.table_name,
              include_checks=args.include_checks,
              include_attributes=args.include_attributes,
              start_at=args.start_at,
              logger=logger
            )
    scr.load_graph()
    scr.generate_dot_file(args.dot_filename)
    scr.generate_png_file(args.png_filename)

