# Problemas identificados durante a execução

Três problemas não foram capturados na análise inicial das fontes e só se manifestaram durante a execução dos notebooks no Databricks.

## 1. Modo ANSI e parsing de data

O runtime do Databricks (Spark 4.1 / Photon) opera em modo ANSI por padrão. Nesse modo, `to_date` e `to_timestamp` lançam exceção (`CANNOT_PARSE_TIMESTAMP`) quando o valor de entrada não corresponde ao formato especificado, em vez de retornar `null`.

Isso afeta diretamente qualquer `coalesce` com múltiplos formatos de data: a primeira tentativa que não casar interrompe a execução, em vez de permitir que a próxima tentativa seja avaliada.

**Ajuste aplicado:** substituição de `to_date`/`to_timestamp` por `try_to_date`/`try_to_timestamp` (via `F.expr(...)`) em todas as colunas de data com múltiplos formatos possíveis. Essas funções preservam o comportamento de retornar `null` em caso de falha de parsing.

## 2. Valor não numérico em coluna de custo

O campo `cost` em `logistica_entregas.json` contém o valor `"unknown"` em 10 registros, em vez de um número. A falha só ocorre na camada Gold, ao agregar `SUM(cost)` por pedido na construção de `fact_pedido_item` (erro `CAST_INVALID_INPUT`).

**Ajuste aplicado:** leitura de `cost` como `string` seguida de `try_cast(... AS DOUBLE)`, que retorna `null` para valores não conversíveis. Os 10 registros afetados ficam com custo de frete nulo. O mesmo padrão foi aplicado preventivamente a `pricing.list_price` em `cadastro_produtos_api_dump.json`, que apresenta o mesmo risco com o valor `"N/A"`.

## 3. Conflito de schema em sobrescrita de tabela Delta

Após alterar o tipo de uma coluna (`preco_lista`, `cost`) e reexecutar a escrita com `mode("overwrite")` sobre uma tabela já existente, o Delta Lake rejeitou a operação com `DELTA_FAILED_TO_MERGE_FIELDS`, mesmo com o tipo final da coluna sendo o mesmo do anterior.

**Ajuste aplicado:** inclusão de `.option("overwriteSchema", "true")` em todas as operações de escrita do projeto (29 ocorrências, nos 14 notebooks), prevenindo o mesmo erro em qualquer re-execução futura após alteração de schema.
