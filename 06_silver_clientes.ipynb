# Bronze: inventário de qualidade das 9 fontes

A camada Bronze realiza a ingestão das 9 fontes sem aplicar correções de qualidade, apenas os ajustes necessários para que cada formato seja lido corretamente (delimitador, schema aninhado, encoding). O tratamento de qualidade é tratado integralmente na camada Silver.

Esta página relaciona os problemas identificados em cada fonte durante a etapa de análise.

## vendedores.csv

- 2 registros duplicados com conflito real: `V004` (canal `CH02` válido vs `CH99` inexistente) e `V008` (nome correto vs "Vendedor 8 duplicado").
- `canal_id` com casing inconsistente (`ch07` em minúsculo).
- `regional_code` misturando sigla (`S`, `N`, `NE`...) com nome por extenso (`sul`).
- `hire_date` em 2 formatos (`yyyy-MM-dd` e `dd/MM/yyyy`).
- `status` com `Ativo`/`ativo`/`inativo`/vazio.

## comercial_canais.xlsx

- `CH05` duplicado com grafias diferentes: "E-commerce" (com hífen) e "ecommerce" (sem hífen). Não é só diferença de capitalização, são strings de fato diferentes.
- `CH06` sem nome cadastrado (a própria planilha já tem a observação "nome ausente").
- `ch07` com id em minúsculo.
- `ativo` com `sim`/`Sim`/`SIM`/`nao`.

## cadastro_produtos_api_dump.json

- JSON aninhado em 3 níveis (`product`, `pricing`, `attributes`).
- `product_id` em minúsculo em 5 registros.
- `P0006` duplicado dentro do próprio cadastro.
- `status` com `Ativo`/`ativo`/`inativo`/`descontinuado`/null.
- `pricing.list_price` com tipos mistos: a maioria numérico, mas com `'N/A'` literal em um registro (`P9999`) e alguns números vindo como string entre aspas.

## crm_clientes_export.xlsx

- `customer_id` em minúsculo (`c0051`).
- 3 duplicidades reais: `C0010` (segunda versão completa um campo vazio), `C0025` (conflito real de estado entre as 2 versões: RJ na primeira, Sta Catarina na segunda) e `C0051` (segunda versão com e-mail inválido, sem "@", com `updated_at` igual ao da primeira versão, sem diferença real de data entre as duas).
- `estado` com sigla, nome completo, abreviação, variação de caixa.
- `data_cadastro` em 3 formatos.
- `status_cliente` com `Ativo`/`ATIVO`/`ativo`/`inativo`/null.

## erp_pedidos_cabecalho_2025.csv

- 3 `order_id` duplicados com conflito: `O00121` (uma versão com data válida, outra com `2025-13-40`, mês inexistente), `O00081` (uma versão com valor válido, outra com `N/A`), `O00011` (duplicata simples).
- `order_date` em 3 formatos distintos (`yyyy-MM-dd`, `yyyy/MM/dd`, `dd/MM/yyyy`). O padrão com "/" mistura duas convenções de ordem de campos. Por isso a validação precisa ser feita por amostragem de linhas, não só pela inspeção do separador.
- `status_order` com `Faturado`/`faturado`/`EM_SEPARACAO`/`em separacao`/`entregue`/`cancelado`/vazio (64 vazios).
- Valores numéricos com ponto, vírgula decimal, ou literal `N/A`.
- `net_amount` não reconcilia com `gross_amount - discount_amount` em 12 pedidos (diferenças de centavos a ~R$120).
- `payment_details` é um JSON dentro de string.

## erp_pedidos_itens_2025.csv

- Delimitador diferente do cabeçalho ("," em vez de ";").
- `unit_price` com vírgula decimal em parte das linhas.
- `item_status` com `Ativo`/`ativo`/`cancelado`/vazio.
- `total_item` divergente de `quantity * unit_price` em 47 itens.
- Código de produto `P8888` referenciado mas sem cadastro correspondente (diferente de `P9999`, que existe).

## legado_regioes_pipe.txt

- `S` e `sul` representam a mesma regional com grafia diferente.
- `SE` duplicado (uma vez com `state=SP`, outra com `state=sao paulo`).
- Linha `XX`: regional inativa, sem nome e sem estado, claramente um registro de teste ou descartado.

## logistica_entregas.json

- `destination.state` com 18 variações de grafia para apenas 4 estados reais.
- `carrier.mode` com `Rodoviário`/`rodoviario`/null.
- `delivery_status` com `Delivered`/`delivered`/`atrasado`/`cancelled`/`in_transit`/null.
- Timestamps em 2 formatos.
- 1 `shipped_at` estruturalmente inválido (`31/02/2025`, fevereiro não tem 31 dias).
- 1 `order_ref` com 2 entregas associadas (reentrega/entrega parcial, não duplicidade).
- `cost` com 10 registros contendo o valor literal `"unknown"` em vez de número. Não identificado na análise inicial. Detalhes em [`problemas-execucao.md`](problemas-execucao.md).

## atendimento_ocorrencias.ndjson

- Schema variável: `metadata` (canal/SLA) e `customer_code` aparecem só em parte das 270 linhas.
- `event_type` com `Delay`/`delay`/`refund`/`troca`/`cancel_request`/`complaint`/null.
- `status` com `Open`/`open`/`closed`/null.
- `severity` com `High`/`high`/`medium`/`low`/null.
- `created_at` em 3 formatos.
