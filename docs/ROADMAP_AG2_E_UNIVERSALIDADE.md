# Roadmap: paridade AlphaGeometry 2 e escopo de geometria universal

**Situação inicial (16 de outubro de 2026):** este repositório contém protótipos e testes de partes dos componentes abaixo, mas **não** uma implementação integral equivalente ao AlphaGeometry 2. Nomes de arquivos nesta página descrevem **módulos propostos**; a existência de um nome não comprova sua implementação. A auditoria de 450 requisitos é uma lista de trabalho, e os relatórios históricos são evidência limitada.

## Definir primeiro o que significa sucesso

- **Paridade funcional de linguagem:** formalizar e realizar exatamente os problemas expressáveis pelo AG2, preservando relações, hipóteses e degenerescências.
- **Paridade de DDAR2:** obter consequências e provas válidas da mesma classe que o motor oficial, por comparação diferencial repetível com a implementação pública.
- **Paridade do sistema completo:** arquitetura neural e/ou estratégias alternativas de busca devem produzir certificados verificáveis, com protocolo de avaliação e orçamento comparáveis aos publicados.
- **Paridade de desempenho:** medir de maneira independente IMO-AG-30 (referência 30/30), IMO-AG-50 (42/50), IMOSL-AG-30 (20/30), e separar métricas por modelo, tempo e recursos. Não confundir testes gerados internamente com esses benchmarks.
- **'Resolução universal':** restringir o domínio antes de reivindicar completude. Problemas de geometria euclidiana formalizados como sentenças de primeira ordem sobre corpos reais fechados admitem decisão em princípio por eliminação de quantificadores, mas isso pode ser computacionalmente impraticável. Linguagens enriquecidas com construções arbitrárias, funções transcendentes e quantificação irrestrita podem escapar de tal enquadramento.

## Pacote `geoforge_core/`: semântica geométrica

| Arquivo proposto | O que falta codificar | Critério de aceitação |
|---|---|---|
| `geoforge_core/ast.py` | AST de pontos, retas, círculos, ângulos, segmentos, razões, expressões, lugares geométricos e quantificadores | Round-trip parser/serializer de corpus AG2 sem perda semântica |
| `geoforge_core/parser_ag2.py` | Parser AG2 completo, inclusive múltiplas definições e operadores de cálculo | Corpus de sintaxe oficial aceito e validado |
| `geoforge_core/type_system.py` | Tipagem, domínios, variáveis livres, condições laterais | Malformações rejeitadas com diagnósticos precisos |
| `geoforge_core/canonical.py` | Equivalências canônicas e α-renomeação de pontos | Fatos isomorfos unificados sem identificar não equivalentes |
| `geoforge_core/geometry_graph.py` | Objetos explícitos, índices de incidência e equivalências estruturais | Diferencial com grafos do DDAR2 |
| `geoforge_core/point_unification.py` | Duplos pontos/nomes, `overlap`, substituição segura | Provas exatas de igualdade de pontos sem confundir coincidências numéricas |
| `geoforge_core/constructions.py` | Construções completas, compostas e multi-restrição | Todos os construtores AG2 executados com condições de existência |
| `geoforge_core/nonconstructive.py` | Problemas de restrições simultâneas e satisfatibilidade | Construção/recusa correta em testes difíceis |
| `geoforge_core/loci.py` | Movimento, dependências e tipos de conclusão de lugar geométrico | Casos de loci provados para todas as configurações admissíveis |
| `geoforge_core/diagram_solver.py` | Otimização numérica para construir diagramas sob várias restrições | Taxa documentada de diagramas válidos, inclusive casos ambíguos |
| `geoforge_core/degeneracy.py` | Guardas de segmentos nulos, divisões, direção e incidência | Zero falsos positivos nos testes adversariais conhecidos |

## Pacote `geoforge_prover/`: dedução e certificados

| Arquivo proposto | O que falta codificar | Critério de aceitação |
|---|---|---|
| `geoforge_prover/ddar2_rules.py` | Biblioteca equivalente ao DDAR2 público com guardas exatos | Testes diferenciais oficiais por família de regra |
| `geoforge_prover/rule_compiler.py` | Regras declarativas e unificação indexada | Nenhuma regra com aplicação sem premissas válidas |
| `geoforge_prover/closure.py` | Saturação incremental, agenda de fatos e índices | Mesmas consequências com menor custo medido |
| `geoforge_prover/angle_ar.py` | Equações de direções e ângulos módulo π | Certificados algébricos matematicamente corretos |
| `geoforge_prover/loglength_ar.py` | Álgebra de log-comprimentos/razões não nulas | Identidades exatas, guardas de denominador |
| `geoforge_prover/length_ar.py` | Equações aditivas de comprimentos e constantes | Casos do AG2 `distseq` com certificados |
| `geoforge_prover/sparse_exact.py` | Eliminação exata e otimizações nativas | Equivalência com referência racional em testes aleatórios |
| `geoforge_prover/proof_kernel.py` | Pequeno verificador independente de fatos, condições e aritmética | Rejeitar certificados manipulados e premissas inventadas |
| `geoforge_prover/certificates.py` | DAG de prova autocontido com rastreamento de hipóteses | Replay por processo separado e versão estável do formato |
| `geoforge_prover/coordinate.py` | Estratégias de coordenadas, polinômios e saturação, com testemunhos | Não classificar `conditional` como `proved` |
| `geoforge_prover/quantifier_elimination.py` | Opção CAD/QE para fragmentos semialgébricos formalizados | Decisão correta em suíte de sentenças sobre corpos reais fechados |
| `geoforge_prover/inequalities.py` | Desigualdades, orientação, ordem, betweenness e convexidade | Provas formais com guardas e contraexemplos verificados |
| `geoforge_prover/inversion.py` | Teoremas inversivos e eixo radical, incluindo casos limite | Demonstrações certificadas em problemas de referência |
| `geoforge_prover/projective.py` | Razões cruzadas, coordenadas homogêneas, Pascal/Desargues | Testes sem divisões inválidas ou pontos indesejadamente no infinito |

## Pacote `geoforge_search/`: prova sem e com redes neurais

| Arquivo proposto | O que falta codificar | Critério de aceitação |
|---|---|---|
| `geoforge_search/construction_enumerator.py` | Busca completa sob limites explícitos sobre construções admissíveis | Repetibilidade e diversidade de operadores em problemas de referência |
| `geoforge_search/heuristics.py` | Proximidade à meta, lemas e controle de saturação | Ganho contra baseline aleatório em orçamento igual |
| `geoforge_search/backward_search.py` | Regressão de objetivos, subgoals e lemmas | Provas certificadas em problemas antes não resolvidos |
| `geoforge_search/multi_tree.py` | Árvores paralelas, estratégias múltiplas, fila de expansão | Nenhuma hipótese local compartilhada como fato global |
| `geoforge_search/skest.py` | SKEST: compartilhamento de conhecimento entre árvores com controles de proveniência | Comparação reproduzível com busca single-tree |
| `geoforge_search/model_adapter.py` | Interface opcional com LM treinado e decodificação geométrica | Propostas válidas em relação à gramática, latência medida |
| `geoforge_search/scheduler.py` | Orçamento global, cache, beam e distribuição de trabalhadores | Mesmo limite de tempo e memória em todos os baselines |
| `geoforge_search/counterexamples.py` | Busca exata de contraexemplos e minimização | Somente refutações que satisfazem hipóteses comprovadas |

## Pacote `geoforge_data/` e `geoforge_ml/`: dados e modelos

| Arquivo proposto | O que falta codificar | Critério de aceitação |
|---|---|---|
| `geoforge_data/diagram_generator.py` | Gerador aleatório grande, com construções completas | Distribuição e rejeição documentadas por família |
| `geoforge_data/dependency_difference.py` | Extração e poda de auxiliares, premissas mínimas | Reprovação independente de alegações de 'auxiliar necessário' não provadas |
| `geoforge_data/quality_gate.py` | Certificação de registros antes de gravar treino | Nenhum problema contaminado por passos não verificados |
| `geoforge_data/dedup.py` | Deduplicação estrutural, isomorfismo, splits por família | Auditoria de vazamento entre treino/teste |
| `geoforge_data/shards.py` | Retomada determinística distribuída em streaming | Mesmos hashes em execuções paralelas equivalentes |
| `geoforge_ml/tokenizer.py` | Vocabulário compatível com AG2, expressões e referências | Idas/voltas sem perda de sintaxe |
| `geoforge_ml/trainer.py` | Treino PyTorch/JAX escalável, logs, checkpoints e precisão mista | Reproduzir curvas e ablações em dados não contaminados |
| `geoforge_ml/inference.py` | Cache KV, inferência distribuída, batch e amostragem | Taxas de tokens/segundo medidas; propostas gramaticamente válidas |
| `geoforge_ml/analysis_strings.py` | S1/S2/S3 com separação entre hipóteses e observações | Sem infiltrar meta assumida como fato demonstrado |
| `geoforge_ml/value_model.py` | Política / avaliação de estados experimental | Aumentar solve@K sob orçamento fixo |

## Pacote `geoforge_formalization/`: entrada humana

| Arquivo proposto | O que falta codificar | Critério de aceitação |
|---|---|---|
| `geoforge_formalization/nl_parser.py` | Tradução verificável PT/EN → AST | Formatos difíceis sem supressão de hipóteses |
| `geoforge_formalization/latex.py` | Leitura/escrita de notação geométrica LaTeX | Round-trip de metas e hipóteses |
| `geoforge_formalization/diagram_reader.py` | Entrada opcional por imagem com reconciliação semântica | Não inferir propriedades apenas da aparência |
| `geoforge_formalization/verification.py` | Verificação de alinhamento texto ↔ enunciado formal | Falhas destacadas em vez de corrigidas silenciosamente |
| `geoforge_formalization/explanation.py` | Demonstração legível a partir de certificado | Todos os passos rastreáveis ao kernel |

## Pacote `geoforge_benchmarks/`: evidência externa e paridade

| Arquivo proposto | O que falta codificar | Critério de aceitação |
|---|---|---|
| `geoforge_benchmarks/official_loader.py` | Ingestão dos datasets oficialmente permitidos | Checksums e rastreabilidade da origem |
| `geoforge_benchmarks/ag1_ag2_diff.py` | Comparação do kernel com implementações públicas | Relatórios por regra e por construção |
| `geoforge_benchmarks/imo_ag_30.py` | Protocolo do IMO-AG-30 | 30 problemas corretamente formalizados e executados |
| `geoforge_benchmarks/imo_ag_50.py` | Protocolo do IMO-AG-50 | 50 problemas com relatórios de solução e recursos |
| `geoforge_benchmarks/imosl_ag_30.py` | Protocolo da shortlist | 30 problemas e provas verificadas |
| `geoforge_benchmarks/jgex_ag_231.py` | Compatibilidade com conjuntos clássicos | 231 problemas com cobertura formal documentada |
| `geoforge_benchmarks/contamination.py` | Auditoria contra memorização de enunciados e diagramas | Sem equivalências entre dados treinados e dados de teste |
| `geoforge_benchmarks/report.py` | Métricas de latência, memória, certificado, solve@K e intervalo de confiança | Relatório JSON versionado e publicamente reproduzível |
| `geoforge_benchmarks/independent_certifier.py` | Segundo verificador e replay das provas avaliadas | Toda contagem positiva com certificado aceito |

## Critérios de bloqueio de release

1. Corrigir qualquer falha de solidez antes de acrescentar heurísticas.
2. Exigir *proof replay* independente para resultados `proved`.
3. Não registrar `unknown`, falha de parser ou timeout como contraexemplo.
4. Não declarar paridade AG2 antes de importar os benchmarks oficiais e publicar orçamento comparável, scores e demonstrações auditáveis.
5. Não declarar universalidade fora de um fragmento lógico e recursos matemáticos explicitamente definidos.

## Fontes

- https://github.com/google-deepmind/alphageometry
- https://github.com/google-deepmind/alphageometry2
- https://www.jmlr.org/papers/volume26/25-1654/25-1654.pdf
