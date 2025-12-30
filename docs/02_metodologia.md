# Metodologia

A análise foi conduzida seguindo princípios simples e conservadores, comuns
em processos de forense e engenharia de dados.

---

## Princípios adotados

1. **Somente leitura**
   Nenhum arquivo foi apagado, movido, alterado ou executado.

2. **Baixo impacto operacional**
   Toda a análise foi realizada a partir de listas e metadados, sem interação
   direta com o ambiente produtivo.

3. **Redução progressiva de ruído**
   O objetivo não foi analisar tudo de uma vez, mas eliminar camadas de ruído
   até identificar os elementos realmente relevantes.

---

## Etapas do processo

### 1. Levantamento do filesystem
- geração de lista plana de arquivos
- tratamento de encoding legado
- normalização de caminhos

### 2. Ingestão em banco analítico
- uso do DuckDB como motor SQL local
- estruturação dos dados em tabela única
- extração de extensão e profundidade

### 3. Análise exploratória
- distribuição de extensões
- análise de profundidade de diretórios
- identificação de padrões estruturais

### 4. Investigação de código
- identificação de arquivos Python
- separação entre código autoral e bibliotecas
- exclusão de ambientes virtuais e backups históricos

### 5. Consolidação
- redução do universo analisado
- classificação funcional dos scripts relevantes
- registro dos aprendizados

O processo privilegiou **clareza, rastreabilidade e segurança**, não velocidade.
