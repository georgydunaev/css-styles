# `css-styles` — Shared Academic & Dashboard CSS Design System

Shared stylesheet library providing foundational typography, responsive layout containers, accessible light/dark mode custom properties, navigation bar utilities, interactive buttons, and 12-column CSS grid classes.

## Repository Contents

- [`styles.css`](styles.css): Primary stylesheet defining:
  - **Accessible Theme Tokens (Tickets 01 & 7476)**: `:root` and `[data-theme="dark"]` variables (`--bg-canvas`, `--bg-card`, `--text-main`, `--text-muted`, `--border-subtle`, `--accent-primary`) meeting WCAG AA ($\ge 4.5:1$) contrast requirements.
  - **Responsive Navigation Bar Utilities (Ticket 02)**: `.nav-container`, `.nav-brand`, `.nav-links`, `.nav-item`, with automatic vertical stacking at `@media (max-width: 768px)`.
  - **Interactive Button Transitions (Ticket 03)**: `.btn-primary`, `.btn-secondary`, `.btn-outline` with `0.2s cubic-bezier(0.4, 0, 0.2, 1)` transitions, `:active` `transform: scale(0.98)`, and `:focus-visible` outline rings.
  - **12-Column CSS Grid Layout (Ticket 04)**: `.grid-layout` (`grid-template-columns: repeat(12, 1fr); gap: 16px;`) and span helpers `.col-span-12`, `.col-span-6`, `.col-span-4`, `.col-span-3`.
- [`tests/test_css_styles.py`](tests/test_css_styles.py): Automated verification test suite checking brace balance, absence of syntax errors, WCAG AA contrast ratios, and presence of all documented utility classes.
- [`tickets/`](tickets/): Enhancement tickets and audit specifications.

## Running Verification Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```
