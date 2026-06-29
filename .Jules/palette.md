# Palette's Journal - Critical UX/Accessibility Learnings

This journal documents critical UX and accessibility learnings discovered during the development process.

## 2025-01-24 - Accessible Focus States in Static CSS
**Learning:** In projects using plain CSS without Tailwind or a modern build system, the 'ring' shorthand is unavailable. To maintain high accessibility for keyboard users, explicit `outline` and `outline-offset` must be used within a `:focus-visible` block to ensure focus states are visually distinct and don't affect layout flow.
**Action:** Always implement `:focus-visible` with a high-contrast `outline` and an `outline-offset` of at least 2px for all interactive elements in this repo.

## 2025-01-24 - Context-Specific ARIA Labels for Repetitive Links
**Learning:** Repetitive link text like "Abrir site" or "Saiba mais" provides a poor experience for screen reader users as it lacks context in the links list.
**Action:** Supplement repetitive CTA text with unique `aria-label` attributes that include the specific target or category name (e.g., "Abrir site [Clinic Name]").
