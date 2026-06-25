# Requirements

## Funcionais
- RF001: Criar preview HTML para cada lead do arquivo `leads-moema.csv`.
- RF002: Criar página índice com links para todos os previews.
- RF003: Cada preview deve ter hero, proposta, serviços, diferenciais, FAQ e contato.
- RF004: Cada preview deve usar identidade visual distinta.
- RF005: Cada preview com telefone público deve ter CTA funcional para WhatsApp.
- RF006: Lead sem telefone público deve ter CTA alternativo seguro.

## Não funcionais
- RNF001: HTML estático, sem build.
- RNF002: Layout responsivo.
- RNF003: Visual comercial moderno.
- RNF004: Navegação local simples.

## Técnicos
- RT001: Arquivos gerados dentro da pasta `dentistas-moema/previews/`.
- RT002: Dados estruturados em JSON por consultório.
- RT003: Índice em `previews/index.html`.
- RT004: Sem dependências externas além de fontes/CDN já usadas no HTML.

## Critérios de aceite
- CA001: Existir 6 previews individuais gerados.
- CA002: Existir 1 índice navegável.
- CA003: Cada preview abrir localmente sem erro de console.
- CA004: Cada preview ter paleta e proposta visual distinguíveis.
- CA005: Não existir linguagem de mockup na interface principal.
