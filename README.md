# Case Engenheiro de Dados

Pipeline de engenharia de dados em camadas (Bronze → Silver → Gold), construída em Databricks com PySpark e Delta Lake, transformando 9 fontes brutas e heterogêneas numa base analítica pronta para consumo por um Analista de BI.

![Arquitetura em camadas](diagrams/arquitetura_camadas.png)

## Como executar

1. Criar um schema e um volume no Unity Catalog (Databricks Free Edition). Isso é feito automaticamente pelo notebook `notebooks/00_setup/00_setup_ambiente.ipynb`.
2. Subir os 9 arquivos fonte para o volume (`Catalog > workspace > case_dados > Volumes > raw_files > Upload to this volume`).
3. Importar a pasta `notebooks/` para o Workspace do Databricks, mantendo a mesma estrutura de subpastas.
4. Abrir `notebooks/00_run_tudo.ipynb` (precisa estar no mesmo nível das 4 subpastas) e rodar. Ele instala a dependência de leitura de Excel e executa os 14 notebooks na ordem correta, incluindo a criação das views finais.

Os notebooks também podem ser executados manualmente, um a um, na ordem numérica das pastas.

## Exemplo de saída

Resultado real de `vw_dim_vendedor` após a execução completa da pipeline:

![Saída de dim_vendedor](diagrams/exemplo_saida_gold.png)

Amostra de `vw_dim_cliente`:

| customer_id | nome_cliente | segmento_cliente | porte_cliente | cidade | estado_uf | regiao | status_cliente |
|---|---|---|---|---|---|---|---|
| C0001 | Cliente 1 | Não informado | Grande | Florianópolis | SC | Sul | Não informado |
| C0002 | Cliente 2 | Educação | Grande | Curitiba | PR | Sul | Ativo |
| C0003 | Cliente 3 | Varejo | Não informado | Curitiba | PR | Sul | Não informado |
| C0004 | Cliente 4 | Saúde | Não informado | Uberlândia | MG | Sudeste | Não informado |

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [`docs/ambiente.md`](docs/ambiente.md) | Databricks Free Edition e suas particularidades |
| [`docs/bronze.md`](docs/bronze.md) | As 9 fontes e o que cada uma tinha de errado |
| [`docs/silver.md`](docs/silver.md) | Limpeza, normalização e regras de deduplicação |
| [`docs/gold.md`](docs/gold.md) | Modelo dimensional final (dimensões e fatos) |
| [`docs/problemas-execucao.md`](docs/problemas-execucao.md) | Bugs que só apareceram rodando no Databricks |
| [`docs/validacoes-e-limitacoes.md`](docs/validacoes-e-limitacoes.md) | Validações aplicadas, limitações e próximos passos |
| [`docs/resumo-executivo.md`](docs/resumo-executivo.md) | Versão condensada de tudo acima ([.pptx](docs/resumo-executivo.pptx)) |

## Notebooks

```
notebooks/
├── 00_run_tudo.ipynb      orquestrador, roda tudo em sequência
├── 00_setup/              cria schema, volume e valida upload
├── 01_bronze/             ingestão crua das 9 fontes
├── 02_silver/             limpeza e normalização, um notebook por fonte
└── 03_gold/               modelo dimensional final, exemplos de KPI e views
```
