"""Validate internal relative links in the built spec.html.

Runs as part of the spec build (see the Makefile). Two checks:

* Fragment links (``#anchor``) resolve to an ``id`` or ``name`` defined
  somewhere in the document.
* Relative file links (e.g. ``styles/foo.css``, ``../../data/x.csv``) point
  at a file that exists on disk, resolved relative to spec.html's location
  (the same way a browser resolves them).

Absolute URLs (``https://``), ``mailto:`` links, and empty hrefs are ignored.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urldefrag, urlparse

import pytest

SPEC_DIR = Path(__file__).resolve().parent.parent
SPEC_HTML = SPEC_DIR / "spec.html"


class _LinkCollector(HTMLParser):
    """Collect href targets and the anchor ids/names defined in a document."""

    def __init__(self):
        super().__init__()
        self.hrefs = []  # (href, line) tuples
        self.anchors = set()  # values of every id= and name= attribute

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        for key, value in attrs:
            if value is None:
                continue
            if key == "href":
                self.hrefs.append((value, line))
            elif key in ("id", "name"):
                self.anchors.add(value)


def _parse():
    parser = _LinkCollector()
    parser.feed(SPEC_HTML.read_text(encoding="utf-8"))
    return parser


def _is_external(href):
    # A URL scheme (http, https, mailto, ...) means the link is not a local
    # relative path. Fragments and relative paths have an empty scheme.
    return bool(urlparse(href).scheme)


# Parse once; skip the whole module when the build artifact is absent.
if SPEC_HTML.exists():
    _DOC = _parse()
else:
    _DOC = None


requires_html = pytest.mark.skipif(
    _DOC is None, reason=f"{SPEC_HTML} not built yet"
)


@requires_html
def test_internal_anchor_links_resolve():
    """Every ``#fragment`` link matches an id or name in the document."""
    broken = {}
    for href, line in _DOC.hrefs:
        if not href.startswith("#") or href == "#":
            continue
        fragment = unquote(href[1:])
        if fragment not in _DOC.anchors:
            broken.setdefault(href, line)

    if broken:
        lines = [f"  line {line}: {href}" for href, line in sorted(broken.items())]
        pytest.fail(
            f"{len(broken)} internal anchor link(s) point at missing targets in "
            f"{SPEC_HTML.name}:\n" + "\n".join(lines),
            pytrace=False,
        )


@requires_html
def test_relative_file_links_exist():
    """Every relative file link points at a file that exists on disk."""
    broken = {}
    for href, line in _DOC.hrefs:
        if href.startswith("#") or not href or _is_external(href):
            continue
        path_part = urldefrag(href).url  # strip any trailing #fragment
        if not path_part:
            continue
        target = (SPEC_DIR / unquote(path_part)).resolve()
        if not target.exists():
            broken.setdefault(href, line)

    if broken:
        lines = [f"  line {line}: {href}" for href, line in sorted(broken.items())]
        pytest.fail(
            f"{len(broken)} relative file link(s) point at missing files in "
            f"{SPEC_HTML.name}:\n" + "\n".join(lines),
            pytrace=False,
        )
