{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Setup\n",
    "\n",
    "Cria o schema e o volume utilizados pelos arquivos brutos e pelas tabelas\n",
    "das três camadas (bronze, silver, gold).\n",
    "\n",
    "Ambiente: Databricks Free Edition (sucessora da Community Edition, com\n",
    "diferenças relevantes de arquitetura):\n",
    "\n",
    "- Não há criação manual de cluster; o compute é serverless e é atribuído\n",
    "  automaticamente na primeira execução de célula.\n",
    "- Unity Catalog é obrigatório, não há `hive_metastore`. Arquivos brutos são\n",
    "  armazenados em um Volume, não em DBFS de uso geral."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "catalog_name = \"workspace\"\n",
    "schema_name = \"case_dados\"\n",
    "volume_name = \"raw_files\"\n",
    "\n",
    "RAW_PATH = f\"/Volumes/{catalog_name}/{schema_name}/{volume_name}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "spark.sql(f\"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name}\")\n",
    "spark.sql(f\"CREATE VOLUME IF NOT EXISTS {catalog_name}.{schema_name}.{volume_name}\")\n",
    "spark.sql(f\"USE CATALOG {catalog_name}\")\n",
    "spark.sql(f\"USE SCHEMA {schema_name}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Após a execução da célula anterior, os 9 arquivos fonte devem ser enviados\n",
    "manualmente: Catalog > workspace > case_dados > Volumes > raw_files >\n",
    "Upload to this volume.\n",
    "\n",
    "Caso o volume não seja exibido na lista, atualizar o painel do Catalog."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "display(dbutils.fs.ls(RAW_PATH))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "esperados = {\n",
    "    \"erp_pedidos_cabecalho_2025.csv\",\n",
    "    \"erp_pedidos_itens_2025.csv\",\n",
    "    \"crm_clientes_export.xlsx\",\n",
    "    \"cadastro_produtos_api_dump.json\",\n",
    "    \"comercial_canais.xlsx\",\n",
    "    \"vendedores.csv\",\n",
    "    \"legado_regioes_pipe.txt\",\n",
    "    \"logistica_entregas.json\",\n",
    "    \"atendimento_ocorrencias.ndjson\",\n",
    "}\n",
    "\n",
    "encontrados = {f.name for f in dbutils.fs.ls(RAW_PATH)}\n",
    "faltando = esperados - encontrados\n",
    "\n",
    "if faltando:\n",
    "    print(\"Arquivos faltantes:\", faltando)\n",
    "else:\n",
    "    print(\"Os 9 arquivos fonte estão presentes no volume.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}