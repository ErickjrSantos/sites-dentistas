## 2026-06-30 - Disambiguating Repetitive Navigation Links
**Learning:** In dashboards or showcases where multiple items use identical call-to-action text (e.g., "Open Site", "View Preview"), screen reader users lose context. While visual proximity provides context for sighted users, accessibility requires programmatic disambiguation.
**Action:** Use `aria-label` to provide unique descriptions for repetitive links (e.g., `aria-label="Abrir site Lumina Smile Studio"`) and ensure keyboard focus states (`:focus-visible`) are prominent when using custom button styles.
