## 2024-05-24 - Accessible Focus States in Static HTML
**Learning:** In repositories without a CSS build system or Tailwind, standard accessibility features like "ring" shorthands are unavailable. Using `outline` with `outline-offset` combined with `:focus-visible` ensures that keyboard users have a high-contrast, non-disruptive indicator that respects the site's color palette.
**Action:** Always implement `:focus-visible` with `outline` and `outline-offset` for static HTML projects to provide clear keyboard navigation without affecting the visual design for mouse users.

## 2024-05-24 - Contextual ARIA Labels for Repetitive Actions
**Learning:** Dashboard interfaces often use repetitive "Call to Action" text like "Open site" or "View preview". For screen reader users, these links are ambiguous when listed out of context.
**Action:** Use `aria-label` to provide specific context (e.g., `aria-label="Abrir site da Lumina Smile Studio"`) while keeping the visual text clean and concise.

## 2024-05-24 - Environment-Agnostic Generation Scripts
**Learning:** Hardcoded absolute paths (e.g., `C:/Users/...`) in generation scripts are a major blocker for portability.
**Action:** Use `Path(__file__).parent` in Python to resolve paths relative to the script's location, ensuring the script remains functional across different operating systems and directory structures.
