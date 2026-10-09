"""
Module to implement a plugin that checks the subject of a column file's
introduction uses the exact Display Name casing.
"""
import re
from typing import Optional, cast

from pymarkdown.tokens.atx_heading_markdown_token import AtxHeadingMarkdownToken
from pymarkdown.tokens.inline_markdown_token import InlineMarkdownToken
from pymarkdown.tokens.markdown_token import MarkdownToken
from pymarkdown.plugin_manager.plugin_details import PluginDetails, PluginDetailsV3
from pymarkdown.plugin_manager.rule_plugin import PluginScanContext, RulePlugin


class RuleMd992(RulePlugin):
    """
    Class to implement a plugin that checks Display Name casing in column files.

    The Display Name comes from the "## Display Name" section, or from the
    "# " heading when that section is missing. Only files in a "columns"
    directory are checked.

    The subject of the introduction (the first words of the first paragraph
    after the "# " heading, optionally after an article and inside a link) is
    the column, so when it matches the Display Name ignoring case it must use
    the exact Display Name casing (e.g., "An [*availability zone*](#glossary:availability-zone) is"
    becomes "An [*Availability Zone*](#glossary:availability-zone) is").

    Display Name references elsewhere in the file (e.g., "Sub account Name") are
    not checked. Outside the introduction subject, text cannot reliably be told
    apart from the concept (e.g., "billing currency") or from sentence case, so
    a check there could flag or rewrite correct text. A future rule could warn
    about such text without fixing it or failing the build.
    """

    __articles = r"(?:(?:A|An|The)\s+)?"

    def __init__(self) -> None:
        super().__init__()
        self.__display_name: Optional[str] = None
        self.__heading_text: Optional[str] = None
        self.__heading_level = 0
        self.__in_display_name_section = False
        self.__in_paragraph = False
        self.__is_column_file = False
        self.__subject_pattern: Optional[re.Pattern] = None
        self.__seen_title = False
        self.__intro_done = False

    def get_details(self) -> PluginDetails:
        """
        Get the details for the plugin.
        """
        return PluginDetailsV3(
            plugin_name="display-name-casing",
            plugin_id="MD992",
            plugin_enabled_by_default=True,
            plugin_description="Introduction subject should match the Display Name casing",
            plugin_version="0.1.0",
            plugin_url="",
            plugin_supports_fix=True,
            plugin_fix_level=0,
        )

    def starting_new_file(self) -> None:
        """
        Event that a new file to be scanned is starting.
        """
        self.__display_name = None
        self.__heading_text = None
        self.__heading_level = 0
        self.__in_display_name_section = False
        self.__in_paragraph = False
        self.__is_column_file = False
        self.__subject_pattern = None
        self.__seen_title = False
        self.__intro_done = False

    def next_token(self, context: PluginScanContext, token: MarkdownToken) -> None:
        """
        Event that a new token is being processed. Collects the Display Name
        before the lines are processed.
        """
        if token.is_atx_heading:
            self.__heading_level = cast(AtxHeadingMarkdownToken, token).hash_count
            self.__in_display_name_section = False
        elif token.is_atx_heading_end:
            self.__heading_level = 0
        elif token.is_paragraph:
            self.__in_paragraph = True
        elif token.is_paragraph_end:
            self.__in_paragraph = False
            self.__in_display_name_section = False
        elif token.is_text:
            text = cast(InlineMarkdownToken, token).token_text.strip()
            if self.__heading_level == 1 and self.__heading_text is None:
                self.__heading_text = text
            elif self.__heading_level == 2:
                self.__in_display_name_section = text == "Display Name"
            elif self.__in_paragraph and self.__in_display_name_section:
                self.__display_name = text
                self.__in_display_name_section = False
        elif token.is_end_of_stream:
            self.__is_column_file = "columns" in re.split(r"[\\/]", context.scan_file)
            name = self.__display_name or self.__heading_text
            if name:
                self.__display_name = name
                words = r"\s+".join(re.escape(word) for word in name.split())
                self.__subject_pattern = re.compile(
                    rf"^{RuleMd992.__articles}\[?\*{{0,2}}({words})(?![\w-])",
                    re.IGNORECASE,
                )

    def next_line(self, context: PluginScanContext, line: str) -> None:
        """
        Event that a new line is being processed. Only the first line of the
        introduction is checked.
        """
        stripped = line.strip()
        if (
            not self.__is_column_file
            or not self.__subject_pattern
            or self.__intro_done
            or not stripped
        ):
            return
        if stripped.startswith("#"):
            self.__intro_done = self.__seen_title
            self.__seen_title = True
            return
        if not self.__seen_title:
            return

        self.__intro_done = True
        match = self.__subject_pattern.match(line)
        if not match or match.group(1) == self.__display_name:
            return

        if context.in_fix_mode:
            context.set_current_fix_line(
                line[: match.start(1)] + self.__display_name + line[match.end(1) :]
            )
        else:
            self.report_next_line_error(
                context,
                match.start(1) + 1,
                extra_error_information=(
                    f"Actual: '{match.group(1)}', Expected: '{self.__display_name}'"
                ),
            )
