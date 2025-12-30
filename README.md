# Forense de Filesystem em Servidor Local

Este repositório documenta um estudo técnico de **forense de dados em filesystem
legado**, com foco em **diagnóstico, governança e redução de ruído**, sem qualquer
ação destrutiva.

O objetivo não é reorganizar, apagar ou migrar dados, mas **entender o que
realmente existe em um ambiente antes de tomar decisões**.

Todo o processo foi conduzido em **modo somente leitura**, com dados anonimizados
e scripts genéricos, tendo caráter **didático e técnico**.

---

## Motivação

Servidores locais tendem a acumular, ao longo do tempo:

- backups sobre backups
- versões manuais
- estruturas profundas de diretórios
- código misturado a dados
- ausência de inventário confiável

Antes de qualquer iniciativa de limpeza, migração ou modernização, surge a
pergunta fundamental:

> **O que realmente temos aqui?**

---

## Abordagem

A análise seguiu uma abordagem incremental e segura:

- levantamento completo de arquivos
- normalização e extração de metadados
- análise exploratória com DuckDB
- classificação progressiva para redução de ruído
- identificação de código autoral relevante

Nenhum arquivo foi apagado, movido ou executado.

---

## Escala analisada (ordem de grandeza)

- ~340 mil arquivos
- ~38 mil diretórios
- profundidade média: 10–11 níveis
- profundidade máxima: 20 níveis
- ~21 mil arquivos Python identificados
- <30 scripts autorais relevantes após filtros

---

## Ferramentas utilizadas

- Python
- DuckDB
- Pandas
- SQL
- VSCode

---

## Principais aprendizados

- Volume não é sinônimo de complexidade real
- Shadow IT costuma ser sintoma, não vilão
- Governança começa com inventário
- Diagnóstico técnico evita decisões às cegas

---

Este repositório registra **processo e raciocínio técnico**, não um ambiente real.