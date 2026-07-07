# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-05-14 - [Initial Observation] - Pure Static HTML Structure
**Learning:** The repository uses pure HTML and CSS without a build system (no Tailwind, no React). Accessibility and UX enhancements must be applied directly to the static files using semantic HTML and standard CSS.
**Action:** Focus on improving base HTML attributes (ARIA labels) and adding micro-interactions via CSS transitions and focus states directly in the style blocks.

## 2025-05-14 - [Accessibility] - Repetitive Link Text
**Learning:** The showcase dashboard uses identical "Abrir site" text for multiple buttons. This is a common accessibility anti-pattern as screen reader users navigating by links won't have context.
**Action:** Always use context-specific `aria-label` attributes to disambiguate repetitive link text.
