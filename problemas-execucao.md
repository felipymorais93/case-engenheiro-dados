# Ambiente

O case especifica Databricks Community Edition, descontinuado e substituído pela Free Edition. Três diferenças de arquitetura impactam diretamente a configuração desta solução:

- Compute serverless, sem criação manual de cluster.
- Unity Catalog obrigatório (sem `hive_metastore`). Os arquivos brutos ficam em um Volume (`/Volumes/workspace/case_dados/raw_files/`), não em DBFS.
- Modo ANSI ativo por padrão no runtime (Spark 4.1 / Photon), alterando o comportamento de `to_date`/`to_timestamp`/`cast`. Ver [`problemas-execucao.md`](problemas-execucao.md).
