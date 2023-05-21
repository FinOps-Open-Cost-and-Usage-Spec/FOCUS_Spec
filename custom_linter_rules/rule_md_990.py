"""
Module to implement a plugin that looks for smart characters in the files.
"""
from typing import cast

from pymarkdown.inline_markdown_token import TextMarkdownToken
from pymarkdown.markdown_token import MarkdownToken
from pymarkdown.parser_helper import ParserHelper
from pymarkdown.plugin_manager.plugin_details import PluginDetails
from pymarkdown.plugin_manager.plugin_scan_context import PluginScanContext
from pymarkdown.plugin_manager.rule_plugin import RulePlugin


class RuleMd990(RulePlugin):
    """
    Class to implement a plugin that looks for smart characters in the files.
    """
    __smart_char_items = [u"\u2013", u"\u201c", u"\u201d", u"\u2018", u"\u2019", u"\u2026"]

    def __init__(self) -> None:
        super().__init__()

    def get_details(self) -> PluginDetails:
        """
        Get the details for the plugin.
        """
        return PluginDetails(
            plugin_name="no-smart-characters",
            plugin_id="MD990",
            plugin_enabled_by_default=True,
            plugin_description="Smart character found",
            plugin_version="0.1.0",
            plugin_interface_version=1,
            plugin_url="",
        )

    def next_token(self, context: PluginScanContext, token: MarkdownToken) -> None:
        """
        Event that a new token is being processed.
        """
        if (
            token.is_text
        ):
            text_token = cast(TextMarkdownToken, token)
            for smart_char_item in RuleMd990.__smart_char_items:
                start_index = 0
                found_index = text_token.token_text.find(smart_char_item, start_index)
                while found_index != -1:
                    (
                        column_number_delta,
                        line_number_delta,
                    ) = ParserHelper.adjust_for_newlines(text_token.token_text, 0, found_index)
                    self.report_next_token_error(
                        context,
                        token,
                        line_number_delta=line_number_delta,
                        column_number_delta=column_number_delta,
                    )
                    start_index = found_index + len(smart_char_item)
                    found_index = text_token.token_text.find(smart_char_item, start_index)


        elif token.is_code_block:
            self.__in_code_block = True
        elif token.is_code_block_end:
            self.__in_code_block = False
        elif token.is_html_block:
            self.__in_html_block = True
        elif token.is_html_block_end:
            self.__in_html_block = False
        elif token.is_inline_link:
            self.__in_link = True
        elif token.is_inline_link_end:
            self.__in_link = False

