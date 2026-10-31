## 2024-05-24 - Contextualizing Repetitive Links
**Learning:** Generic call-to-action text like "Abrir site" (Open site) repeated across multiple cards in a dashboard creates a poor experience for screen reader users, who may navigate via link lists without visual context.
**Action:** Always provide unique `aria-label` attributes for repetitive links to include the specific context (e.g., "Abrir site da clínica [Nome]").

## 2024-05-24 - Accessible Focus Indicators in Custom UIs
**Learning:** Custom-styled buttons in dark-themed landing pages often lack high-contrast focus indicators, breaking keyboard accessibility.
**Action:** Implement `:focus-visible` with `outline` and `outline-offset` using a theme-consistent accent color to ensure a clear, non-disruptive focus state.

## 2026-10-31 - Sincronização de Templates Estáticos Gerados por Script
**Learning:** Em catálogos gerados programmaticamente por scripts (ex: Python para HTML), melhorias de acessibilidade feitas apenas no arquivo HTML final são sobrescritas na próxima execução do gerador.
**Action:** Sempre aplicar os atributos de acessibilidade (como `aria-label` dinâmico com o nome da entidade) e regras CSS de interação diretamente nas strings de template dentro do script gerador, garantindo reprodutibilidade do design acessível.
