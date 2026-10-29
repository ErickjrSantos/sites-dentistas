## 2024-05-24 - Contextualizing Repetitive Links
**Learning:** Generic call-to-action text like "Abrir site" (Open site) repeated across multiple cards in a dashboard creates a poor experience for screen reader users, who may navigate via link lists without visual context.
**Action:** Always provide unique `aria-label` attributes for repetitive links to include the specific context (e.g., "Abrir site da clínica [Nome]").

## 2024-05-24 - Accessible Focus Indicators in Custom UIs
**Learning:** Custom-styled buttons in dark-themed landing pages often lack high-contrast focus indicators, breaking keyboard accessibility.
**Action:** Implement `:focus-visible` with `outline` and `outline-offset` using a theme-consistent accent color to ensure a clear, non-disruptive focus state.
