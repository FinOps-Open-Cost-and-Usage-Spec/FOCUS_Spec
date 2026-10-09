"""
Module to implement a plugin that checks references to a column's Display Name
use the exact Display Name casing.
"""
import re
from typing import List, Optional, Tuple, cast

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

    A match of the Display Name (ignoring case) is a Display Name reference when:
    - It is the subject of the introduction, i.e. the first words of the first
      paragraph after the "# " heading, optionally after an article and inside a
      link (e.g., "An [*availability zone*](#glossary:availability-zone) is").
    - Elsewhere, a word after the first is capitalized (e.g., "Sub account Name").
      All-lowercase text refers to the concept, and a capital on the first word
      only may be sentence case, so neither is flagged. An acronym written as in
      the Display Name (e.g., "resource ID") is not counted as a capital.

    A Display Name reference must use the exact Display Name casing.
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
        self.__name_pattern: Optional[re.Pattern] = None
        self.__subject_pattern: Optional[re.Pattern] = None
        self.__seen_title = False
        self.__intro_done = False
        self.__in_fence = False

    def get_details(self) -> PluginDetails:
        """
        Get the details for the plugin.
        """
        return PluginDetailsV3(
            plugin_name="display-name-casing",
            plugin_id="MD992",
            plugin_enabled_by_default=True,
            plugin_description="Display Name reference should match the Display Name casing",
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
        self.__name_pattern = None
        self.__subject_pattern = None
        self.__seen_title = False
        self.__intro_done = False
        self.__in_fence = False

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
                self.__name_pattern = re.compile(
                    rf"(?<![\w-])({words})(?![\w-])", re.IGNORECASE
                )
                self.__subject_pattern = re.compile(
                    rf"^{RuleMd992.__articles}\[?\*{{0,2}}({words})(?![\w-])",
                    re.IGNORECASE,
                )

    def __find_errors(self, line: str, is_intro: bool) -> List[Tuple[int, int, str]]:
        """
        Return (start, end, actual) for each miscased Display Name reference.
        """
        assert self.__display_name and self.__name_pattern and self.__subject_pattern
        errors: List[Tuple[int, int, str]] = []
        if is_intro:
            match = self.__subject_pattern.match(line)
            if match and match.group(1) != self.__display_name:
                errors.append((match.start(1), match.end(1), match.group(1)))
        for match in self.__name_pattern.finditer(line):
            actual = match.group(1)
            if actual == self.__display_name:
                continue
            if any(start == match.start(1) for start, _, _ in errors):
                continue
            if self.__has_later_capital(actual):
                errors.append((match.start(1), match.end(1), actual))
        return sorted(errors)

    def __has_later_capital(self, actual: str) -> bool:
        """
        Whether a word after the first has a capital that marks the text as a
        Display Name reference. An acronym written as in the Display Name
        (e.g., "ID" in "resource ID") is not evidence, since concept text uses it too.
        """
        assert self.__display_name
        expected_words = self.__display_name.split()[1:]
        for word, expected in zip(actual.split()[1:], expected_words):
            is_acronym = len(expected) > 1 and expected.isupper()
            if any(char.isupper() for char in word) and not (
                is_acronym and word == expected
            ):
                return True
        return False

    def next_line(self, context: PluginScanContext, line: str) -> None:
        """
        Event that a new line is being processed.
        """
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            self.__in_fence = not self.__in_fence
            return
        if (
            not self.__is_column_file
            or not self.__name_pattern
            or self.__in_fence
            or not stripped
        ):
            return
        if stripped.startswith("#"):
            if self.__seen_title:
                self.__intro_done = True
            self.__seen_title = True
            return

        is_intro = self.__seen_title and not self.__intro_done
        self.__intro_done = self.__intro_done or self.__seen_title
        errors = self.__find_errors(line, is_intro)
        if not errors:
            return

        if context.in_fix_mode:
            fixed_line = line
            for start, end, _ in reversed(errors):
                fixed_line = fixed_line[:start] + self.__display_name + fixed_line[end:]
            context.set_current_fix_line(fixed_line)
        else:
            for start, _, actual in errors:
                self.report_next_line_error(
                    context,
                    start + 1,
                    extra_error_information=(
                        f"Actual: '{actual}', Expected: '{self.__display_name}'"
                    ),
                )
