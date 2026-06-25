# Spec

## Objetivo
Criar previews comerciais individuais para todos os consultórios prospectados em Moema, cada um com identidade visual própria e copy alinhada ao posicionamento percebido.

## Escopo
- Gerar 1 preview HTML para cada lead do CSV.
- Gerar 1 JSON estruturado para cada lead.
- Criar 1 página índice para navegar entre os previews.
- Diferenciar visual, tom e proposta de valor entre os consultórios.
- Manter apenas dados públicos já capturados.

## Fora de escopo
- Backend.
- CMS.
- Integração com domínio final.
- Automação de geração por IA em runtime.
- Auditoria detalhada do site atual de cada consultório.

## Usuários
- Operador comercial da fábrica de sites.
- Donos/gestores dos consultórios que receberão o preview.

## Funcionalidades
- Página índice com cards dos consultórios.
- Preview individual para cada consultório.
- CTA principal visível.
- Bloco de especialidades/serviços coerente com o lead.
- Contato e localização com dados públicos.

## Regras de negócio
- Não inventar telefone, CRO, credenciais ou prova social inexistente.
- Cada consultório deve ter identidade visual distinta.
- O texto deve parecer comercial e pronto para apresentação.
- Leads sem telefone público não devem ter CTA falso de WhatsApp.

## Fluxo principal
1. Operador abre o índice local.
2. Escolhe um consultório.
3. Visualiza o preview individual.
4. Usa o link local/online no outreach.

## Integrações
- WhatsApp via wa.me quando houver telefone.
- Google Maps via link externo.

## Riscos
- Dados públicos limitados reduzem personalização profunda.
- Leads sem telefone público terão CTA menos forte.
- Sem fotos reais, parte da autoridade continua visual/sintética.
