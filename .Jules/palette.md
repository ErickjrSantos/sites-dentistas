# Palette's Journal - Critical UX Learnings

## 2024-05-24 - Interactive Enhancement for Static Showcase
**Learning:** For static HTML dashboards without a build system, injecting a small `<style>` block with transitions and `focus-visible` states provides high ROI for UX/a11y with minimal overhead. Descriptive ARIA labels on repetitive link text ("Abrir site") are essential for screen reader context in template galleries.
**Action:** Use CSS variables from the existing palette and `focus-visible` to ensure keyboard accessibility matches the visual theme. Always add context to repetitive CTA buttons.
