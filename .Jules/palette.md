# PALETTE'S JOURNAL - CRITICAL LEARNINGS ONLY

## 2025-05-15 - Repository Initial Exploration
**Learning:** The repository contains multiple static HTML files across `showcase/` and `prospects/` with consistent theme variables (`--bg`, `--panel`, `--line`, etc.) but lacks basic micro-UX features like hover transitions and keyboard focus indicators on index pages. Repetitive link text like "Abrir site" and "Abrir preview" is a common accessibility pattern that needs fixing.
**Action:** Implement `aria-label` for repetitive links and inject base interactivity CSS (transitions, focus-visible) into index files.
