# Validações, limitações e próximos passos

## Validações aplicadas

- Soma de `receita_liquida_item` por pedido sempre reconcilia com `net_amount` do cabeçalho (validado explicitamente no notebook de `fact_pedido_item`).
- Checagem de produtos referenciados em itens sem cadastro correspondente — identificado `P8888`.
- Checagem de pedidos/entregas/ocorrências sem correspondência cruzada (`LEFT JOIN` + filtro por nulo).
- Contagem de linhas bronze → silver impressa em cada notebook, para confirmar que a quantidade de duplicatas removidas é exatamente a esperada.

## Limitações conhecidas

- `net_amount` não reconciliado em 12 pedidos e `total_item` não reconciliado em 47 itens — sinalizados via flag, não corrigidos automaticamente, porque a causa raiz não pode ser inferida só com os dados disponíveis.
- O conflito de estado em `C0025` (RJ vs Sta Catarina) foi resolvido pela versão mais recente do cadastro, mas é uma divergência factual real que merece confirmação com a área de CRM.
- 10 entregas com custo de frete desconhecido (`cost = 'unknown'` na origem) — `custo_frete_total` fica nulo para os pedidos associados a essas entregas.
- A tabela `dim_tempo` cobre o intervalo de `order_date` ± 1 ano; datas muito fora dessa janela não teriam correspondência no calendário (não observado nos dados atuais, mas é uma premissa a documentar).

## Sugestões de evolução

- Investigar com a área de ERP a causa das divergências de `net_amount`/`total_item` antes de decidir se a fórmula de cálculo de receita precisa de ajuste.
- Padronizar a captura de dados nas fontes de origem (datas em formato único, status com domínio fechado) para reduzir o volume de tratamento necessário a cada nova carga.
- Adicionar um job agendado (Databricks Jobs) para execução periódica da pipeline, eliminando a execução manual.
- Avaliar particionamento adicional nas tabelas fato por período (ano/mês), à medida que o volume de dados crescer.
