"""
Module to implement a plugin that enforces title case for headings.
"""
import re
from typing import cast

from pymarkdown.tokens.inline_markdown_token import InlineMarkdownToken
from pymarkdown.tokens.markdown_token import MarkdownToken
from pymarkdown.plugin_manager.plugin_details import PluginDetails
from pymarkdown.plugin_manager.rule_plugin import PluginScanContext, RulePlugin


class RuleMd991(RulePlugin):
    """
    Class to implement a plugin that enforces title case for headings.

    Title case rules:
    - First and last words are always capitalized
    - All major words are capitalized
    - Minor words (articles, conjunctions, prepositions) are lowercase unless first/last
    - Words after colons are capitalized
    """

    # Words that should be lowercase in title case (unless first/last word)
    __minor_words = {
        'a', 'an', 'the',  # articles
        'and', 'but', 'or', 'nor', 'for', 'yet', 'so',  # coordinating conjunctions
        'as', 'at', 'by', 'for', 'in', 'of', 'on', 'to', 'up', 'via', 'with', 'from',  # prepositions
    }

    def __init__(self) -> None:
        super().__init__()
        self.__in_atx_heading = False
        self.__in_setext_heading = False

    def get_details(self) -> PluginDetails:
        """
        Get the details for the plugin.
        """
        return PluginDetails(
            plugin_name="heading-title-case",
            plugin_id="MD991",
            plugin_enabled_by_default=True,
            plugin_description="Heading should use title case",
            plugin_version="0.1.0",
            plugin_interface_version=1,
            plugin_url="",
        )

    def starting_new_file(self) -> None:
        """
        Event that a new file to be scanned is starting.
        """
        self.__in_atx_heading = False
        self.__in_setext_heading = False

    def next_token(self, context: PluginScanContext, token: MarkdownToken) -> None:
        """
        Event that a new token is being processed.
        """
        # Track heading state
        if token.is_atx_heading:
            self.__in_atx_heading = True
        elif token.is_atx_heading_end:
            self.__in_atx_heading = False
        elif token.is_setext_heading:
            self.__in_setext_heading = True
        elif token.is_setext_heading_end:
            self.__in_setext_heading = False

        # Check text in headings
        if token.is_text and (self.__in_atx_heading or self.__in_setext_heading):
            text_token = cast(InlineMarkdownToken, token)
            heading_text = text_token.token_text.strip()

            if heading_text and not self._is_title_case(heading_text):
                suggestion = self._to_title_case(heading_text)
                self.report_next_token_error(
                    context,
                    token,
                    extra_error_information=f"Actual: '{heading_text}', Expected: '{suggestion}'"
                )

    def _is_title_case(self, text: str) -> bool:
        """
        Check if text follows title case rules.
        """
        # Split on whitespace to get words (preserving punctuation)
        tokens = text.split()

        if not tokens:
            return True

        for i, token in enumerate(tokens):
            is_first = (i == 0)
            is_last = (i == len(tokens) - 1)

            # Check if previous token ended with colon
            follows_colon = i > 0 and tokens[i-1].endswith(':')

            # Extract all alphanumeric words from token to handle hyphenated terms
            for word_match in re.finditer(r'\w+', token):
                word = word_match.group()
                word_lower = word.lower()

                # Skip numbers (they have no case)
                if word.isdigit():
                    continue

                # Check capitalization rules
                if is_first or is_last or follows_colon:
                    # First, last, or after colon: should be capitalized
                    if not word[0].isupper():
                        return False
                elif word_lower in self.__minor_words:
                    # Minor word in middle: should be lowercase
                    if not word.islower():
                        return False
                else:
                    # Major word: should be capitalized
                    if not word[0].isupper():
                        return False

        return True

    def _to_title_case(self, text: str) -> str:
        """
        Convert text to title case for error message suggestions.
        """
        tokens = text.split()
        result = []

        for i, token in enumerate(tokens):
            is_first = (i == 0)
            is_last = (i == len(tokens) - 1)

            # Check if previous token ended with colon
            follows_colon = i > 0 and result[i-1].endswith(':')

            # Process all alphanumeric words in token (handles hyphenated terms)
            new_token = token
            offset = 0  # Track position changes as we replace words

            for word_match in re.finditer(r'\w+', token):
                word = word_match.group()
                word_lower = word.lower()

                # Skip numbers (keep them as-is)
                if word.isdigit():
                    continue

                # Determine if this word should be capitalized
                if is_first or is_last or follows_colon or word_lower not in self.__minor_words:
                    # Smart case preservation: keep existing camelCase or ACRONYMS intact
                    if len(word) > 1 and any(c.isupper() for c in word[1:]):
                        capitalized_word = word[0].upper() + word[1:]
                    else:
                        capitalized_word = word.capitalize()
                else:
                    # Minor word in middle: lowercase
                    capitalized_word = word.lower()

                # Replace the word in the token while preserving surrounding punctuation
                start = word_match.start() + offset
                end = word_match.end() + offset
                new_token = new_token[:start] + capitalized_word + new_token[end:]
                offset += len(capitalized_word) - len(word)

            result.append(new_token)

        return ' '.join(result)
