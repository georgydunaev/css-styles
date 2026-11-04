# Ticket 01: Add accessible dark mode color palette variables

**Project:** css-styles
**Importance:** 3/10
**State:** opened
**Target Model Tier:** Tier 2 / Tier 3 (Free Cloud / Small LLMs)
**Labels:** user, simple-task, tier2-model, tier3-model, css-styles

## Description
In `styles.css`, define modern CSS custom properties under `:root` and `[data-theme="dark"]`: `--bg-canvas`, `--bg-card`, `--text-main`, `--text-muted`, `--border-subtle`, `--accent-primary`. Verify contrast ratio meets WCAG AA (>= 4.5:1).

## Acceptance Criteria
1. Implementation is clean, tested, and self-contained within `css-styles/`.
2. Do not modify files outside `css-styles/`.
3. Verify syntax and tests pass without errors.
