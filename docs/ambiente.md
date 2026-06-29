# Ambiente

O case especifica Databricks Community Edition. Essa versão foi descontinuada e substituída pela Free Edition, que apresenta diferenças relevantes de arquitetura:

- Não há criação manual de cluster. O compute é serverless e atribuído automaticamente ao notebook.
- Unity Catalog é obrigatório; não há `hive_metastore`. Arquivos brutos são armazenados em Volumes (`/Volumes/workspace/case_dados/raw_files/`), não em DBFS de uso geral.
- O runtime (Spark 4.1, Photon) opera em modo ANSI por padrão, o que altera o comportamento de funções de parsing de data e cast — detalhado em [`problemas-execucao.md`](problemas-execucao.md).

Essas diferenças afetam a forma de provisionamento (schema, volume, compute) e algumas funções de transformação, mas não alteram o desenho da solução.
