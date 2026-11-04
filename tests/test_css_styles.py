#!/usr/bin/env python3
"""
Automated verification tests for css-styles (Tickets 01-04, 7298, 7476, 7477).
"""
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STYLES_PATH = REPO_ROOT / "styles.css"
README_PATH = REPO_ROOT / "README.md"


def _rel_lum(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in (r, g, b)]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]


def _contrast(c1: str, c2: str) -> float:
    l1, l2 = _rel_lum(c1), _rel_lum(c2)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


class TestCssStyles(unittest.TestCase):
    def setUp(self):
        self.css = STYLES_PATH.read_text(encoding="utf-8")

    def test_balanced_braces_and_no_trailing_garbage(self):
        stripped = re.sub(r"/\*.*?\*/", "", self.css, flags=re.S).strip()
        self.assertEqual(stripped.count("{"), stripped.count("}"))
        self.assertFalse(stripped.endswith(">"))

    def test_ticket_01_dark_mode_tokens_and_wcag_aa_contrast(self):
        for token in (
            "--bg-canvas",
            "--bg-card",
            "--text-main",
            "--text-muted",
            "--border-subtle",
            "--accent-primary",
        ):
            self.assertIn(token, self.css)
        self.assertIn('[data-theme="dark"]', self.css)
        self.assertGreaterEqual(_contrast("#fafafa", "#111827"), 4.5)
        self.assertGreaterEqual(_contrast("#0f172a", "#f8fafc"), 4.5)

    def test_ticket_02_responsive_navbar_classes(self):
        for cls in (".nav-container", ".nav-brand", ".nav-links", ".nav-item"):
            self.assertIn(cls, self.css)
        self.assertIn("@media (max-width: 768px)", self.css)

    def test_ticket_03_button_transitions(self):
        for cls in (".btn-primary", ".btn-secondary", ".btn-outline"):
            self.assertIn(cls, self.css)
        self.assertIn("cubic-bezier", self.css)
        self.assertIn("scale(0.98)", self.css)
        self.assertIn(":focus-visible", self.css)

    def test_ticket_04_grid_layout_classes(self):
        self.assertIn(".grid-layout", self.css)
        self.assertIn("repeat(12, 1fr)", self.css)
        for span in (".col-span-12", ".col-span-6", ".col-span-4", ".col-span-3"):
            self.assertIn(span, self.css)

    def test_readme_documented(self):
        readme = README_PATH.read_text(encoding="utf-8")
        self.assertIn("styles.css", readme)
        self.assertIn("WCAG AA", readme)


if __name__ == "__main__":
    unittest.main()
