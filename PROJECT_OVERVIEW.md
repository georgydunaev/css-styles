# Project Overview: Shared Academic and Dashboard CSS Design System (`css-styles`)

## Purpose and Scope

`css-styles` (`/botworkspace/css-styles`) provides the shared CSS design tokens, responsive layout containers, accessible light/dark mode custom properties, navigation bar utilities, interactive button styles, and 12-column CSS grid classes used across workspace academic portals and dashboards.

## Repository Contents

- [styles.css](file:///botworkspace/css-styles/styles.css): Primary stylesheet defining:
  - **Accessible Theme Variables**: `:root` and `[data-theme="dark"]` color tokens (`--bg-canvas`, `--bg-card`, `--text-main`, `--text-muted`, `--accent-primary`, `--border-subtle`) meeting WCAG AA contrast standards.
  - **Typography and Academic Formatting**: Serif body typography, responsive headings, mathematical theorem/proof blocks, and horizontal overflow guards.
  - **Responsive Grid and Flex Utilities**: `.container`, `.grid-12`, `.col-*`, `.card`, `.navbar`, and `.btn` component classes.
  - **Print Stylesheet (`@media print`)**: Clean high-contrast print rules hiding interactive chrome and preserving page breaks.
- [README.md](file:///botworkspace/css-styles/README.md): Design token reference and usage documentation.
- [tests/](file:///botworkspace/css-styles/tests/): Automated CSS syntax, selector, and accessibility token test suite.
- [tickets/](file:///botworkspace/css-styles/tickets/): Resolved CSS design and refactoring tickets.

## Verification Command

```bash
python3 -m unittest discover -s /botworkspace/css-styles/tests -p "test_*.py"
```
