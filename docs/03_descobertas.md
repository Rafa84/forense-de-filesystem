# Descobertas

Este capítulo consolida os principais achados obtidos a partir da análise
exploratória do filesystem, com foco em **escala**, **estrutura** e **sinal real
escondido no ruído**.

---

## Escala do ambiente analisado

O levantamento inicial revelou um ambiente de grande volume e complexidade
estrutural:

- Aproximadamente **340.000 arquivos**
- Cerca de **38.000 diretórios**
- Profundidade média entre **10 e 11 níveis**
- Profundidade máxima observada: **20 níveis de diretório**

Esses números indicam um filesystem que cresceu de forma orgânica ao longo
do tempo, sem políticas claras de retenção, versionamento ou organização
estrutural.

---

## Profundidade como fator crítico

Durante a análise, ficou evidente que a **profundidade excessiva** dos caminhos
representa um problema mais relevante do que o volume absoluto de arquivos.

Caminhos muito profundos impactam diretamente:

- desempenho de operações de leitura
- tempo de backup e restauração
- indexação por ferramentas de busca
- confiabilidade de scripts e automações
- usabilidade para usuários finais

Em vários casos, a profundidade observada é consequência de:
- versionamento manual
- backups encadeados
- ausência de ciclo de vida definido para arquivos

---

## Distribuição por tipo de arquivo

A análise por extensão mostrou uma forte concentração em arquivos documentais,
como PDFs, imagens e planilhas.

Esse padrão é típico de ambientes operacionais e administrativos, onde o
filesystem acaba sendo utilizado como repositório primário de informação,
em vez de apenas armazenamento intermediário.

Apesar do grande volume, a maioria desses arquivos não apresenta risco técnico
direto, mas contribui para a **entropia estrutural** do ambiente.

---

## Presença de código no filesystem

Um ponto de destaque foi a identificação de arquivos de código misturados
ao restante do conteúdo.

Foram encontrados aproximadamente:

- **21.000 arquivos Python (.py)** distribuídos ao longo do filesystem

À primeira vista, esse número sugere um ambiente fortemente dependente de
automação. No entanto, análises posteriores mostraram que essa percepção
é enganosa.

---

## Separação entre ruído e sinal (Python)

Após aplicação de filtros para exclusão de:

- bibliotecas de terceiros (`site-packages`)
- ambientes virtuais (`venv`, `__pycache__`)
- cópias redundantes
- backups históricos

o universo de arquivos Python foi reduzido de forma significativa.

O conjunto final identificado como **scripts autorais relevantes** ficou
limitado a **poucas dezenas de arquivos**.

Isso representa uma redução superior a **99,8%** em relação ao volume inicial
de arquivos Python encontrados.

Esse padrão reforça uma lição comum em engenharia de dados:
> grandes volumes frequentemente escondem um núcleo funcional pequeno,
> porém crítico.

---

## Código funcional fora do fluxo formal

Os scripts autorais identificados apresentaram características comuns:

- foco em automações locais
- processamento de arquivos e planilhas
- geração de relatórios operacionais
- apoio direto a atividades de negócio

Em geral, tratam-se de soluções criadas para resolver problemas reais,
fora de um fluxo formal de desenvolvimento de sistemas.

Esse tipo de automação é frequentemente classificado como **Shadow IT**,
não como ato de desorganização, mas como resposta prática a necessidades
operacionais não atendidas no momento adequado.

---

## Complexidade percebida vs. complexidade real

Um dos principais aprendizados desta análise foi a diferença entre:

- **complexidade percebida**, baseada em volume e profundidade
- **complexidade real**, baseada em lógica, dependências e impacto operacional

Após a redução progressiva de ruído, ficou claro que:

- o risco técnico estava concentrado em um conjunto pequeno de artefatos
- decisões baseadas apenas em volume levariam a conclusões equivocadas
- diagnóstico técnico é essencial antes de qualquer ação corretiva

---

## Síntese das descobertas

Em resumo, o estudo revelou que:

- grandes filesystems tendem a esconder poucos elementos realmente críticos
- profundidade excessiva é um forte indicativo de ausência de governança
- código autoral pode existir fora dos fluxos formais sem ser imediatamente visível
- reduzir ruído é pré-requisito para qualquer decisão consciente

Essas descobertas reforçam a importância de **inventário e análise exploratória**
como primeiro passo em iniciativas de governança de dados e modernização de
ambientes legados.