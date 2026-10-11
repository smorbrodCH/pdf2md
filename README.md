# pdf2md

Wandelt ein PDF in Markdown um, als Kontext für Sprachmodelle. Kleines, eigenständiges Programm auf Basis von [PyMuPDF](https://github.com/pymupdf/PyMuPDF) / pymupdf4llm.

```bash
pip install .
pdf2md skript.pdf --max-pages 100 > skript.md
```

Exit-Codes: 0 ok, 2 Aufruf falsch, 3 zu viele Seiten, 4 keine Textebene (Scan), 5 Datei unlesbar oder verschlüsselt. Die erste Zeile auf stderr nennt die Seitenzahl (`pages=12`).

## Lizenz

GNU Affero General Public License v3.0 (siehe [LICENSE](LICENSE)), wie PyMuPDF. VoiceTutor ruft `pdf2md` als separaten Prozess auf (ADR 0011 im VoiceTutor-Repository).

Copyright (C) 2026 digitalify GmbH
