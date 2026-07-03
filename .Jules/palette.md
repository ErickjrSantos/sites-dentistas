## 2025-03-24 - Accessible focus states and descriptive link labels in static sites

**Learning:** In repositories containing pure HTML/CSS without a build system or framework, common accessibility pitfalls include missing focus indicators (as default browser styles are often removed by resets) and repetitive link text ("Abrir site") that lacks context for screen readers. Using `outline` and `outline-offset` with `:focus-visible` provides a clean, accessible focus state without affecting layout, and `aria-label` is essential for disambiguating links that look identical but have different destinations.

**Action:** Always check for focus-visible states when reviewing static HTML sites. When generating content via scripts, ensure that the templates include context-aware `aria-label` attributes for all interactive elements, especially when they are part of a repeating list or grid.
