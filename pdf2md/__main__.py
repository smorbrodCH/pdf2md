"""pdf2md – convert one PDF to Markdown on standard output.

    pdf2md FILE.pdf [--max-pages N]

Exit codes: 0 ok, 2 usage, 3 too many pages, 4 no text layer (scan),
5 unreadable or encrypted PDF. The first line on stderr is a machine-readable
status (e.g. ``pages=12``), so a caller can show limits without parsing
Markdown.

Copyright (C) 2026 digitalify GmbH
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License version 3 as published by
the Free Software Foundation. It is distributed WITHOUT ANY WARRANTY; see
LICENSE. Source: https://github.com/smorbrodCH/pdf2md
"""

from __future__ import annotations

import argparse
import sys

import pymupdf
import pymupdf4llm

MIN_CHARS_PER_PAGE = 20  # below this on average, the PDF is most likely a scan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pdf2md")
    parser.add_argument("path")
    parser.add_argument("--max-pages", type=int, default=100)
    args = parser.parse_args(argv)
    try:
        doc = pymupdf.open(args.path)
    except Exception:
        print("error=unreadable", file=sys.stderr)
        return 5
    with doc:
        if doc.needs_pass:
            print("error=encrypted", file=sys.stderr)
            return 5
        pages = doc.page_count
        print(f"pages={pages}", file=sys.stderr)
        if pages > args.max_pages:
            return 3
        text_chars = sum(len(page.get_text("text").strip()) for page in doc)
        if pages and text_chars / pages < MIN_CHARS_PER_PAGE:
            return 4
        markdown = pymupdf4llm.to_markdown(doc, show_progress=False)
    sys.stdout.write(markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
