# Resumo Executivo Técnico — Case Engenheiro de Dados

## O que foi construído

Pipeline de engenharia de dados em camadas (Bronze → Silver → Gold) no Databricks, em PySpark e Delta Lake, transformando 9 fontes brutas e heterogêneas (CSV, JSON, Excel, NDJSON, arquivo legado) em uma base analítica para consumo por um Analista de BI.

O modelo final é composto por 6 tabelas dimensão e 3 tabelas fato, em esquema estrela, que atendem diretamente às perguntas de negócio definidas no case — receita líquida, ticket médio, taxa de cancelamento, taxa de atraso, segmentação por região, canal, categoria e período — sem necessidade de tratamento adicional pelo analista.

## Decisões técnicas

- **Granularidade de item de pedido** na fato principal (`fact_pedido_item`), em vez de pedido — permite segmentação por produto/categoria sem perder a capacidade de agregação no nível de pedido.
- **Rateio de receita por item**, dado que `net_amount` está disponível apenas no cabeçalho do pedido — evita duplicação de receita ao agregar por item.
- **Normalização geográfica centralizada** em uma tabela de apoio única, reutilizada pelos notebooks de clientes, vendedores e entregas.
- **Fatos de evento (entrega, ocorrência) mantidas separadas** da fato de item, em função da cardinalidade um-para-muitos entre pedido e entrega/ocorrência.
- **Critério de deduplicação explícito em todos os casos** — data de atualização mais recente, score de qualidade dos campos, ou critério de desempate definido quando os anteriores não são suficientes.

## Desafios técnicos

As 9 fontes apresentavam inconsistências de qualidade típicas de integração de sistemas distintos: datas em até 3 formatos na mesma coluna, variação de capitalização em campos de status, registros duplicados com conteúdo divergente entre versões, delimitadores diferentes entre arquivos do mesmo sistema de origem, e referências cruzadas sem correspondência (produto sem cadastro, canal duplicado com grafias distintas).

Dois problemas adicionais foram identificados apenas durante a execução, e não na etapa de análise:

- O runtime do Databricks opera em modo ANSI por padrão, o que altera o comportamento de `to_date`/`to_timestamp` — a função passou a lançar exceção em formato inválido, em vez de retornar nulo.
- O campo `cost` (custo de frete) contém o valor `"unknown"` em 10 registros — identificado apenas quando a agregação de soma falhou na camada Gold.

Ambos foram corrigidos com funções de parsing tolerantes a erro (`try_to_date`, `try_cast`).

## Modelo final

**Dimensões:** cliente, vendedor, produto, canal, região, tempo (calendário gerado).

**Fatos:** pedido/item (com flags de cancelamento, atraso, lead time e produto não cadastrado), entrega (tempo de trânsito e custo), ocorrência de atendimento (SLA e canal).

## Próximos passos recomendados

- Investigar com a área de ERP a causa das divergências de valor entre cabeçalho e itens (12 pedidos, 47 itens) antes de ajustar a fórmula de cálculo de receita.
- Padronizar a captura de dados nas fontes de origem — formato único de data, domínio fechado para campos de status — reduzindo o volume de tratamento em cargas futuras.
- Agendar a execução da pipeline via Databricks Jobs.
- Revisar com a área de CRM o conflito de estado identificado no cliente C0025 antes de consolidar o cadastro.
