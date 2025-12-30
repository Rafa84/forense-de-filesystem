# Forense de Dados em Filesystem Legado

Este repositório documenta um estudo técnico de **forense de dados em servidor local (on-premise)**, realizado com foco em diagnóstico, governança e redução de ruído.

O objetivo deste projeto não foi realizar uma "limpeza" cega, mas sim aplicar **engenharia de dados** para entender a realidade de um ambiente legado antes de qualquer tomada de decisão.

---

## 🎯 O Problema
Ambientes de servidores de arquivos locais tendem a crescer organicamente ao longo de anos. O cenário analisado apresentava características comuns a esse tipo de infraestrutura:
- Centenas de milhares de arquivos acumulados.
- Profundidade excessiva de diretórios (aninhamento profundo).
- Mistura não gerenciada de dados operacionais, backups históricos e código.
- Ausência de um inventário técnico confiável.

O desafio: **Como diagnosticar o estado real desse ambiente sem interromper a operação e sem risco de perda de dados?**

## 🛠️ A Abordagem
A análise foi conduzida seguindo princípios de **auditoria técnica**:

1.  **Somente Leitura (Read-Only):** Nenhuma operação de escrita, deleção ou modificação foi realizada no servidor.
2.  **Análise Offline:** Os metadados foram extraídos para um ambiente local isolado.
3.  **Engenharia Analítica:** Uso de ferramentas de dados para processar e classificar o inventário.

### Stack Utilizada
- **Python:** Para varredura do filesystem, parsing de caminhos e classificação de scripts.
- **DuckDB:** Como motor SQL local para análise exploratória de grande volume de registros (metadados).
- **Pandas:** Para transformações finais e geração de relatórios.
- **SQL:** Para consultas de agregação e descoberta de padrões.

---

## 📂 Estrutura do Repositório

O projeto está organizado da seguinte forma:

- **`docs/`**: Documentação detalhada do racional técnico.
  - [01_contexto.md](docs/01_contexto.md): O cenário e a motivação.
  - [02_metodologia.md](docs/02_metodologia.md): O passo a passo da execução.
  - [03_descobertas.md](docs/03_descobertas.md): O que os dados revelaram.
  - [04_licoes_aprendidas.md](docs/04_licoes_aprendidas.md): Conclusões sobre legado e governança.

- **`scripts/`**: Códigos utilizados na análise (anonimizados para fins didáticos).
  - Scripts de varredura e ingestão no DuckDB.
  - Queries SQL para análise de extensões e profundidade.
  - Filtros Python para identificação de *Shadow IT* e código autoral.

- **`resultados/`**: Exemplos dos outputs gerados (tabelas agregadas e resumos).

---

## 🔍 Principais Aprendizados

1.  **Volume ≠ Complexidade:** A grande maioria dos arquivos em servidores legados costuma ser ruído (backups redundantes, bibliotecas de software, arquivos temporários).
2.  **Shadow IT como Sintoma:** A presença de scripts e automações fora do controle da TI geralmente indica gargalos operacionais reais que foram resolvidos pelas áreas de negócio.
3.  **Profundidade é Risco:** Estruturas de pastas muito profundas degradam performance de backup e dificultam migrações para a nuvem.
4.  **Diagnóstico Primeiro:** Ferramentas de engenharia de dados (como DuckDB) são extremamente eficazes para auditar infraestrutura tradicional.

---

## ⚠️ Disclaimer
Este repositório contém **scripts e documentos de estudo**. Todos os caminhos, nomes de arquivos e dados sensíveis foram anonimizados ou substituídos por exemplos genéricos para preservar a confidencialidade do ambiente original.
