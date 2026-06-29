# Silver — limpeza, normalização e deduplicação

A camada Silver aplica as correções de formatação, deduplicação e padronização identificadas na análise da Bronze. Cada fonte possui um notebook dedicado (`02_silver_regioes` a `09_silver_ocorrencias`).

## Normalização geográfica centralizada

Clientes, vendedores e entregas representam estado/região com grafias distintas (sigla, nome completo, variações de acentuação e caixa). Foi criada uma tabela de apoio (`apoio_map_uf`) que resolve qualquer variação para a sigla de UF e a região geográfica oficial correspondentes. A tabela é construída uma única vez no notebook de regiões e reutilizada pelos notebooks de clientes e entregas, evitando a duplicação da lógica de normalização geográfica.

## Regras de deduplicação sempre com critério explícito

Toda duplicidade é resolvida por um critério definido e auditável, nunca pela ordem de leitura do arquivo. Critérios aplicados, em ordem de prioridade:

- **Atualização mais recente** (`updated_at`), quando a fonte tem esse campo (produtos, clientes).
- **Score de qualidade** (quantos campos críticos vieram válidos), quando não há campo de atualização (pedidos).
- **Critério de desempate secundário** quando o campo de atualização é idêntico entre as versões (cliente `C0051`: e-mail válido prevalece sobre e-mail inválido). Necessário porque, sem esse critério, o resultado dependeria da ordem física de processamento no cluster, que não é determinística em Spark distribuído.
- **Valor de referência definido manualmente** quando a divergência não é resolvível por transformação automática de string (canal `CH05`: "E-commerce" e "ecommerce" diferem pela presença do hífen, não apenas pela capitalização — `initcap()` não normaliza esse caso).

## Itens sem cadastro de produto correspondente

O item com `product_code = P8888` não possui registro correspondente em `cadastro_produtos_api_dump.json`. Esse item é mantido na camada Gold via `LEFT JOIN` com `dim_produto`, sinalizado pela coluna `produto_cadastrado = false`. A exclusão do registro removeria receita real do modelo em função de uma lacuna no cadastro de produtos.

## Divergências de valor sinalizadas, não corrigidas

`net_amount` apresenta divergência em relação a `gross_amount - discount_amount` em 12 pedidos; `total_item` diverge de `quantity * unit_price` em 47 itens. Em ambos os casos, o valor original é preservado e a divergência é sinalizada via flag (`flag_valor_inconsistente`, `flag_total_item_inconsistente`). A causa-raiz (taxas adicionais, regra de arredondamento do sistema de origem) não pode ser determinada a partir dos dados disponíveis, e por isso nenhuma correção foi aplicada automaticamente.

## Resumo por fonte

| Fonte | Notebook | Principal tratamento |
|---|---|---|
| Regiões | `02_silver_regioes` | Cria `apoio_map_uf`; descarta linha `XX` inativa; consolida `S`/`sul` e os 2 `SE` |
| Canais | `03_silver_canais` | Resolve `CH05` duplicado; preenche nome ausente do `CH06`; normaliza `ch07` |
| Produtos | `04_silver_produtos` | Achata JSON aninhado; normaliza case; remove duplicata `P0006`; `try_cast` em `preco_lista` |
| Vendedores | `05_silver_vendedores` | Remove duplicatas `V004`/`V008`; normaliza canal e região; parse de 2 formatos de data |
| Clientes | `06_silver_clientes` | Remove 3 duplicatas (`C0010`, `C0025`, `C0051`); resolve UF via `apoio_map_uf`; parse de 3 formatos de data |
| Pedidos (cabeçalho + itens) | `07_silver_pedidos` | Remove 3 duplicatas conflitantes; parse de 3 formatos de data; normaliza valores numéricos sujos |
| Entregas | `08_silver_entregas` | Achata JSON; resolve UF; `try_cast` em `cost` (10 valores `'unknown'`) |
| Ocorrências | `09_silver_ocorrencias` | Lida com schema variável (`metadata`, `customer_code` parciais); parse de 3 formatos de data |
