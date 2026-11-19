#!/usr/bin/env python3
import argparse
import json
from graphviz import Digraph
from build_helpers import init_logger

def get_args():
    parser = argparse.ArgumentParser(description='Model Graph Generator.')
    parser.add_argument('-t', '--dataset-name', default="CostAndUsage", help='Dataset to generate model graph for')
    parser.add_argument('--include-checks', action='store_true', help='Add checks to graph')
    parser.add_argument('--include-attributes', action='store_true', help='Add attributes to graph')
    parser.add_argument('-f', '--model-filename', type=str, default='build/model-1.2.json', help='Model definition filename to load')
    parser.add_argument('--dot-filename', type=str, default='model_graph.dot', help='Output model graph dot filename')
    parser.add_argument('--png-filename', type=str, default='model_graph.png', help='Output model graph png filename')
    parser.add_argument('--logging-level', type=str, default='WARNING', choices={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}, help='Logging level to use')
    parser.add_argument('--start-at', type=str, default=None, help='Start the graph at a specific item')
    return parser.parse_args()
    

class ModelRequirements:
    def __init__(self, model_filename, dataset_name, logger, include_checks=True, include_attributes=False, start_at=None):
        self.model_filename = model_filename
        self.dataset_name = dataset_name
        self.include_checks = include_checks
        self.include_attributes = include_attributes
        self.model_definition = {}
        self.model_graph = ModelGraph(graph_name=f'{self.dataset_name} Dataset Model DAG', logger=logger)
        self.logger = logger
        self.start_at = start_at

    def __load_model_definition(self):
        if not self.model_definition:
            # Load Model JSON
            with open(self.model_filename, "r") as f:
                self.model_definition = json.load(f)

    def __add_check_item(self, requirement, rule_id):
        check_function = requirement.get("CheckFunction", None)
        if check_function in {'OR', 'AND'}:
            for item in requirement.get("Items", []):
                self.__add_check_item(item, rule_id)
        elif check_function == "CheckModelRule":
            target = requirement.get("ModelRuleId", None)
            if target:
                self.model_graph.add_node(target, custom_data=self.model_definition['ModelRules'].get(target, {}))
                self.model_graph.add_edge(rule_id, target)
                self.__traverse_dependencies(target)
        else:
            if self.include_checks:
                self.model_graph.add_node(check_function, custom_data=self.model_definition['CheckFunctions'].get(check_function, {}))
                self.model_graph.add_edge(rule_id, check_function)
                self.__traverse_check_attributes(check_function)
            else:
                self.logger.warning(f'Skipping {check_function} checks is disabled') 

    def __traverse_check_attributes(self, check_id):
        if not self.include_attributes:
            self.logger.warning(f'Skipping {check_id} attribute checks is disabled')
            return
        check_function = self.model_definition["CheckFunctions"].get(check_id, None)
        if not check_function:
            self.logger.warning(f'Skipping {check_id} check not found')
            return

        for attribute in check_function.get('FormatAttributes', []):
            self.model_graph.add_node(attribute, custom_data=self.model_definition['ModelRules'].get(attribute, {}))
            self.model_graph.add_edge(check_id, attribute)
            self.__traverse_dependencies(attribute)

    def __traverse_dependencies(self, rule_id):
        self.logger.info(f'traversing {rule_id}')
        rule = self.model_definition["ModelRules"].get(rule_id, {})
        requirement = rule.get("ValidationCriteria", {}).get("Requirement", {})
        if requirement:
            check_function = requirement.get("CheckFunction", None)
            if check_function:
                self.__add_check_item(requirement, rule_id)
        for rule_dependency in rule.get("ValidationCriteria", {}).get("Dependencies", []):
            self.model_graph.add_edge(rule_id, rule_dependency)

    def load_graph(self):
        self.__load_model_definition()
        if self.start_at:
            rule = self.model_definition["ModelRules"].get(self.start_at)
            if not rule:
                self.logger.error(f'Provided --start-at rule "{self.start_at}" not found in ModelRules')
                return
            self.model_graph.add_node(self.start_at, custom_data=rule)
            self.__traverse_dependencies(self.start_at)
        else:
            dataset_name = self.model_definition["ModelDatasets"].get(self.dataset_name, {})
            self.model_graph.add_node(f"Dataset: {self.dataset_name}", shape='box', custom_data=dataset_name)
            for rule_id in self.model_definition["ModelDatasets"][self.dataset_name]["ModelRules"]:
                self.model_graph.add_node(rule_id, custom_data=self.model_definition['ModelRules'].get(rule_id, {}))
                self.model_graph.add_edge(self.dataset_name, rule_id)
                self.__traverse_dependencies(rule_id)

    def generate_dot_file(self, dot_filename):
        self.model_graph.render(dot_filename, format_type="dot")
    
    def generate_png_file(self, png_filename):
        self.model_graph.render(png_filename, format_type="png")


class ModelGraph:
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
    model = ModelRequirements(model_filename = args.model_filename,
              dataset_name=args.dataset_name,
              include_checks=args.include_checks,
              include_attributes=args.include_attributes,
              start_at=args.start_at,
              logger=logger
            )
    model.load_graph()
    model.generate_dot_file(args.dot_filename)
    model.generate_png_file(args.png_filename)
