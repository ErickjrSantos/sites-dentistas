# Dentist Sites Repo

Coleção organizada de sites e previews comerciais para clínicas odontológicas.

## Estrutura padrão

```text
showcase/
  index.html
  01-lumina-smile/
  02-atlas-implant-center/
  03-viva-kids-family/
  screenshots/

prospects/
  dentistas-moema/
    README.md
    data/
    docs/
    drafts/
    previews/
    screenshots/
    scripts/
```

## Conteúdo

### `showcase/`
3 sites-demo prontos para apresentar estilos diferentes de clínica odontológica:
- `01-lumina-smile` — premium estético
- `02-atlas-implant-center` — implantes / autoridade
- `03-viva-kids-family` — família / odontopediatria

Abra `showcase/index.html` para navegar entre os 3 demos.

### `prospects/dentistas-moema/`
Pacote comercial completo para prospecção de dentistas em Moema:
- leads públicos coletados
- documentação SDD (`spec`, `requirements`, `tasks`)
- previews individuais por clínica
- screenshots de apoio
- script de geração
- draft HTML base da Dra. Elisa

Abra `prospects/dentistas-moema/previews/index.html` para navegar entre os previews dos consultórios.

## Uso local

Por serem HTMLs estáticos, basta abrir no navegador:
- `showcase/index.html`
- `prospects/dentistas-moema/previews/index.html`

## Observação

Os previews usam apenas dados públicos capturados no material original. Não há backend nem dependências obrigatórias para visualização local.
