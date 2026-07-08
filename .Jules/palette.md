## 2025-05-15 - [Acessibilidade em links repetitivos]
**Learning:** Links com o mesmo texto (ex: "Abrir site") em uma grade de cards confundem usuários de leitores de tela que navegam por lista de links.
**Action:** Sempre adicionar `aria-label` descritivo e único para cada link em componentes repetitivos.

## 2025-05-15 - [Feedback visual e foco acessível]
**Learning:** Em sites estáticos minimalistas, a ausência de transições e estados de foco torna a interface "morta" e inacessível via teclado.
**Action:** Implementar `transition: all 0.2s ease` e `:focus-visible` usando `outline` e `outline-offset` para garantir interatividade fluida e acessível.
