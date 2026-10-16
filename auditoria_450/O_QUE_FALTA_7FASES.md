# Auditoria das 7 fases do GeoForge

**Arquivo:** `/mnt/data/geoforge.py`
**SHA-256:** `7d3744fa44a2ab30f5a4b4c2b13215514244191a5f0009e5ae55e18f3b15db7c`
**Data UTC:** 2026-10-16T14:16:34.271501+00:00 · **Modo:** quick

## Resultado verificável

- Testes funcionais: **45 passaram / 45 executados**.
- Falhas funcionais: **0**.
- Testes não executados por modo/dependência: **110**.
- Inventário de marcos: **450**.
- Com comportamento testado apenas parcialmente: **31**.
- Com símbolo identificado sem comprovação integral: **211**.
- Sem evidência estática encontrada: **208**.
- Marcos com testes falhando: **0**.
- Paridade AG2 comprovada: **NÃO**. Todas as fases concluídas: **NÃO**.

### Progresso por fase (não é porcentagem de conclusão)

| Fase | Nome | Testes passaram | Falharam | Marcos com evidência funcional | Só símbolo | Sem evidência |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Linguagem, grafo, álgebra exata e certificação | 26 | 0 | 18 | 73 | 8 |
| 2 | DDAR2, construções, numerics e lugares geométricos | 11 | 0 | 9 | 54 | 40 |
| 3 | Geração sintética, datasets e cobertura | 4 | 0 | 4 | 28 | 2 |
| 4 | Modelo neural, SKEST e análise simbólica | 0 | 0 | 0 | 17 | 61 |
| 5 | Infraestrutura, benchmark e avaliação externa | 3 | 0 | 0 | 29 | 29 |
| 6 | Matemática avançada e estratégias de pesquisa | 0 | 0 | 0 | 5 | 58 |
| 7 | Formalização natural, diagramas e interface | 1 | 0 | 0 | 5 | 10 |

## Tarefas de maior prioridade

Estas lacunas vêm de testes executados, ausências de evidência ou benchmarks não fornecidos.
- Nenhum teste executado apresentou falha funcional neste modo.
- **Fase 1, #006 aconst:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #007 rconst:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #065 CongruenceIndex:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #096 NativeLinearAlgebraBackend:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #170 TopologicalCertificate:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #174 AuxiliaryPointMinimizer:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #176 InvalidProofDetector:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 1, #181 FormalAssistantBridge:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #035 TriangleCenterConstructor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #037 TangentConstructor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #040 RotationConstructor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #041 HomothetyConstructor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #042 SimilarityConstructor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #043 EquilateralTriangleConstructor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #046 ConstructionDependencyGraph:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 2, #049 ConstructionEquivalenceChecker:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- Fase 2: outras **32** capacidades sem evidência estão no CSV.
- **Fase 3, #196 MultiAuxiliaryProblemSampler:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 3, #203 DatasetContaminationDetector:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #211 GPUTransformerBackend:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #213 SparseMixtureOfExperts:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #214 ExpertRouter:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #215 ExpertLoadBalancer:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #216 EfficientAttention:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #218 LongContextManager:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #219 DynamicGeometryTokenizer:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 4, #220 ProofReferenceTokenizer:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- Fase 4: outras **53** capacidades sem evidência estão no CSV.
- **Fase 5, #359 DistributedExecutionCoordinator:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #360 DDARWorkerPool:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #361 NeuralInferenceWorkerPool:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #362 GPUModelServing:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #363 DynamicBatchingEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #364 NativeGeometryCore:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #365 PythonNativeBindings:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 5, #366 SharedFactDatabase:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- Fase 5: outras **21** capacidades sem evidência estão no CSV.
- **Fase 6, #296 InversionGeometryEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #297 InversionTheoremLibrary:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #298 RadicalAxisEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #299 RadicalCenterTheorems:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #300 CirclePowerEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #301 MiquelTheoremEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #302 ProjectiveGeometryEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 6, #303 HomogeneousCoordinateSystem:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- Fase 6: outras **50** capacidades sem evidência estão no CSV.
- **Fase 7, #283 GeometricRelationExtractor:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #285 GeometricCoreferenceResolver:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #286 TopologyLanguageParser:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #288 FormalizationCandidateGenerator:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #289 FormalizationConsensusEngine:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #290 FormalizationConsistencyChecker:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #292 TextDiagramConsistencyChecker:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- **Fase 7, #293 MultilingualProblemInterface:** Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência.
- Fase 7: outras **2** capacidades sem evidência estão no CSV.

## Benchmarks externos

| Benchmark | Resultado | Evidência ausente / observação |
|---|---|---|
| IMO-AG-30 | **BLOCKED** | Dataset externo não fornecido; nenhuma taxa de sucesso é presumida. |
| IMO-AG-50 | **BLOCKED** | Dataset externo não fornecido; nenhuma taxa de sucesso é presumida. |
| IMOSL-AG-30 | **BLOCKED** | Dataset externo não fornecido; nenhuma taxa de sucesso é presumida. |
| JGEX-AG-231 | **BLOCKED** | Dataset externo não fornecido; nenhuma taxa de sucesso é presumida. |
| Teste diferencial oficial DDAR2 | **BLOCKED** | Checkout do DDAR2 oficial não fornecido ou incompleto (--official-dir). |

## Microbenchmarks locais (NÃO olímpicos)

| Operação | Amostras | Mediana (ms) | P95 (ms) | Ops/s |
|---|---:|---:|---:|---:|
| parser_fact | 10 | 0.004 | 0.0081 | 225260.75 |
| certified_proof_check | 3 | 0.0884 | 0.1032 | 11601.69 |
| symbolic_ddar_midline | 3 | 1.7467 | 5.2055 | 348.45 |

## Falhas e testes não realizados

- [NOT_RUN] F1-014: Auditoria diferencial algébrica aleatória. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-028: Comando oficial phase1-test. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-007: Resolvedor de restrições não lineares com ponto médio. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-012: Famílias de provas: cobertura real em sementes distintas. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-013: Prova longa de midline encadeada. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-015: Substituição de pontos coincidentes não cria fatos falsos. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-016: CLI ddar2-certified + arquivo de certificado. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-017: Parser reconhece formato de problema oficial. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-018: Comando phase23-test. Exige nível full; execução selecionada: quick.
- [NOT_RUN] F3-005: Escreve e audita shards com provas certificadas. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-006: Manifesto registra hash SHA-256 de cada shard. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-007: Alterar shard é detectado na auditoria. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-008: Retomada mantém dados anteriores e atualiza manifesto. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-009: Sem modo resume, diretório existente não é sobrescrito. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-010: Determinismo entre processos e hash randomization. Exige nível full; execução selecionada: quick.
- [NOT_RUN] F3-011: Confere distribuição por famílias. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-012: Provas e hipóteses verificadas no arquivo de saída. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-013: Geração CLI e auditoria CLI. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-014: Minerador estocástico não inventa prova. Exige nível full; execução selecionada: quick.
- [NOT_RUN] F4-001: Transformer pequeno: forward shape e gradientes finitos. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F4-002: Salva/carrega pesos sem alterar inferência. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F4-003: Solver dedutivo pequeno: resposta possui estado explícito. Exige nível full; execução selecionada: quick.
- [NOT_RUN] F6-001: Detecta interface polinomial (sem certificar implementação completa). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-01-000: Prova certificada e numérica de midline, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-01-007: Prova certificada e numérica de midline, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-01-023: Prova certificada e numérica de midline, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-01-101: Prova certificada e numérica de midline, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-02-000: Prova certificada e numérica de parallel_transitive, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-02-007: Prova certificada e numérica de parallel_transitive, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-02-023: Prova certificada e numérica de parallel_transitive, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-02-101: Prova certificada e numérica de parallel_transitive, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-03-000: Prova certificada e numérica de perp_pair, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-03-007: Prova certificada e numérica de perp_pair, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-03-023: Prova certificada e numérica de perp_pair, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-03-101: Prova certificada e numérica de perp_pair, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-04-000: Prova certificada e numérica de para_perp, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-04-007: Prova certificada e numérica de para_perp, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-04-023: Prova certificada e numérica de para_perp, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-04-101: Prova certificada e numérica de para_perp, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-05-000: Prova certificada e numérica de thales, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-05-007: Prova certificada e numérica de thales, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-05-023: Prova certificada e numérica de thales, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-05-101: Prova certificada e numérica de thales, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-06-000: Prova certificada e numérica de thales_converse, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-06-007: Prova certificada e numérica de thales_converse, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-06-023: Prova certificada e numérica de thales_converse, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-06-101: Prova certificada e numérica de thales_converse, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-07-000: Prova certificada e numérica de circle_center, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-07-007: Prova certificada e numérica de circle_center, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-07-023: Prova certificada e numérica de circle_center, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-07-101: Prova certificada e numérica de circle_center, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-08-000: Prova certificada e numérica de double_midline, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-08-007: Prova certificada e numérica de double_midline, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-08-023: Prova certificada e numérica de double_midline, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-08-101: Prova certificada e numérica de double_midline, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-09-000: Prova certificada e numérica de parallel_perpendicular_chain, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-09-007: Prova certificada e numérica de parallel_perpendicular_chain, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-09-023: Prova certificada e numérica de parallel_perpendicular_chain, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-09-101: Prova certificada e numérica de parallel_perpendicular_chain, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-10-000: Prova certificada e numérica de circle_angle_chain, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-10-007: Prova certificada e numérica de circle_angle_chain, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-10-023: Prova certificada e numérica de circle_angle_chain, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-10-101: Prova certificada e numérica de circle_angle_chain, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-11-000: Prova certificada e numérica de parallelogram_perpendicular_chain, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-11-007: Prova certificada e numérica de parallelogram_perpendicular_chain, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-11-023: Prova certificada e numérica de parallelogram_perpendicular_chain, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-11-101: Prova certificada e numérica de parallelogram_perpendicular_chain, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-12-000: Prova certificada e numérica de midpoint_parallelogram, seed 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-12-007: Prova certificada e numérica de midpoint_parallelogram, seed 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-12-023: Prova certificada e numérica de midpoint_parallelogram, seed 23. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-THEOREM-12-101: Prova certificada e numérica de midpoint_parallelogram, seed 101. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-00: Rotação, escala e translação de base média (0). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-01: Rotação, escala e translação de base média (1). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-02: Rotação, escala e translação de base média (2). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-03: Rotação, escala e translação de base média (3). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-04: Rotação, escala e translação de base média (4). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-05: Rotação, escala e translação de base média (5). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-06: Rotação, escala e translação de base média (6). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-07: Rotação, escala e translação de base média (7). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-08: Rotação, escala e translação de base média (8). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-09: Rotação, escala e translação de base média (9). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-10: Rotação, escala e translação de base média (10). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-11: Rotação, escala e translação de base média (11). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-12: Rotação, escala e translação de base média (12). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-13: Rotação, escala e translação de base média (13). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-14: Rotação, escala e translação de base média (14). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F2-META-15: Rotação, escala e translação de base média (15). Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-01: Certificado de base média alterado para perp d e b c. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-02: Certificado de base média alterado para para d e a c. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-03: Certificado de base média alterado para cong d e b c. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-04: Certificado de base média alterado para midp d e c. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-05: Certificado de base média alterado para cyclic a b c d. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-06: Certificado de base média alterado para perp a b a c. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-07: Certificado de base média alterado para coll d b c. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-MUT-08: Certificado de base média alterado para eqratio a b c d a c b d. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-00: Testemunho racional aleatório 0. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-01: Testemunho racional aleatório 1. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-02: Testemunho racional aleatório 2. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-03: Testemunho racional aleatório 3. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-04: Testemunho racional aleatório 4. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-05: Testemunho racional aleatório 5. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-06: Testemunho racional aleatório 6. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-07: Testemunho racional aleatório 7. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-08: Testemunho racional aleatório 8. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-09: Testemunho racional aleatório 9. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-10: Testemunho racional aleatório 10. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F1-ALG-11: Testemunho racional aleatório 11. Exige nível standard; execução selecionada: quick.
- [NOT_RUN] F3-STRESS-001: 128 tentativas sintéticas e auditoria completa de shards. Exige nível stress; execução selecionada: quick.
- [NOT_RUN] F1-STRESS-001: Auditoria algébrica diferencial ampliada (800 ensaios). Exige nível stress; execução selecionada: quick.
- [NOT_RUN] F2-STRESS-001: Cobertura de 12 famílias em 30 sementes adversariais. Exige nível stress; execução selecionada: quick.

## Referências externas

- [AG2_code](https://github.com/google-deepmind/alphageometry2)
- [AG2_test](https://github.com/google-deepmind/alphageometry2/blob/main/test.py)
- [AG1_code](https://github.com/google-deepmind/alphageometry)
- [AG2_paper](https://www.jmlr.org/papers/volume26/25-1654/25-1654.pdf)

## Interpretação obrigatória

- Ausência de símbolo é indício, não prova absoluta de ausência de funcionalidade.
- Presença de classe/rotina não certifica comportamento nem equivalência ao AG2.
- Passagem dos testes sintéticos não certifica desempenho em IMO, IMOSL ou JGEX.
- O repositório público do AG2 publica o núcleo DDAR, não todos os pesos e a busca neural.
- Completar 450 itens de engenharia não garante 100% de problemas matemáticos inéditos.

## Inventário COMPLETO de 450 requisitos (por fase)

### Fase 1: Linguagem, grafo, álgebra exata e certificação

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 001 | GeometryLexer | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 002 | GeometryParser | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 003 | GeometryAST | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 004 | GeometryTypeChecker | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 005 | GeometryCanonicalizer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 006 | aconst | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 007 | rconst | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 008 | acompute | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 009 | rcompute | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 010 | angeq | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 011 | distmeq | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 012 | distseq | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 013 | sameclock | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 014 | noverlap | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 015 | overlap | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 016 | lessthan | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 017 | cyclic_with_center | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 018 | LinearExpression | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 019 | LocusExpression | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 020 | FreePointPlaceholder | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 021 | NonConstructiveStatement | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 022 | GoalNormalizer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 023 | VariableScope | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 024 | DSLSerializer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 025 | AG1AG2Compatibility | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 051 | PointNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 052 | LineNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 053 | CircleNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 054 | SegmentNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 055 | AngleNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 056 | TriangleNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 057 | PredicateNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 058 | ConstructionNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 059 | ProofDependencyNode | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 060 | IncidenceIndex | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 061 | ParallelClassIndex | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 062 | PerpendicularityIndex | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 063 | EqualLengthIndex | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 064 | CyclicPointIndex | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 065 | CongruenceIndex | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 066 | SimilarityIndex | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 067 | GeometryUnionFind | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 068 | DoublePointEngine | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 069 | SymbolicPointSubstitution | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 070 | IncrementalFactPropagation | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 071 | ContradictionDetector | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 072 | GraphStateHasher | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 073 | PersistentGeometryState | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 074 | ExactRational | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 075 | SparseLinearExpression | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 076 | AngleEquationSystem | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 077 | AngleModuloPiSolver | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 078 | AngleConstantSolver | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 079 | LogDistanceEquationSystem | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 080 | DistanceEquationSystem | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 081 | RatioEquationSystem | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 082 | ExactGaussianElimination | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 083 | IncrementalRowReduction | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 084 | SparseMatrixBackend | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 085 | AlgebraicNormalForm | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 086 | EquationEntailment | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 087 | AlgebraicProofTrace | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 088 | AlgebraicContradictionCheck | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 089 | ZeroLengthGuard | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 090 | AngleDegeneracyGuard | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 091 | ExactConstantRepresentation | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 092 | PolynomialEquationInterface | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 093 | AlgebraicDependencyPruner | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 094 | ModularArithmeticAccelerator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 095 | ModularResultCertification | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 096 | NativeLinearAlgebraBackend | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 097 | AlgebraDifferentialTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 162 | ProofStep | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 163 | ProofCertificate | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 164 | ProofChecker | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 165 | AxiomRegistry | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 166 | TheoremRuleValidator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 167 | AlgebraicCertificateVerifier | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 168 | ConstructionCertificateVerifier | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 169 | NonDegeneracyCertificate | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 170 | TopologicalCertificate | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 171 | ProofDependencyDAG | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 172 | ProofTraceback | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 173 | ProofMinimizer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 174 | AuxiliaryPointMinimizer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 175 | ProofLengthOptimizer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 176 | InvalidProofDetector | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 177 | NumericalCounterexampleFinder | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 178 | ProofAssumptionAudit | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 179 | ProofPrettyPrinter | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 180 | ProofJSONExporter | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 181 | FormalAssistantBridge | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 182 | ProofReplayEngine | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 413 | ARITY: linguagem extensível | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 416 | LinSys: certificação algébrica exata | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 417 | stmt_rows: equações AG2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 418 | _prove: semântica e hipóteses | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 422 | r_simtri: assinatura de triângulos | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 426 | Closure.explain: certificados | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |

### Fase 2: DDAR2, construções, numerics e lugares geométricos

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 026 | ConstructionRegistry | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 027 | LineLineIntersection | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 028 | LineCircleIntersection | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 029 | CircleCircleIntersection | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 030 | IntersectionBranchResolver | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 031 | ParallelLineConstructor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 032 | PerpendicularLineConstructor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 033 | AngleBisectorConstructor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 034 | PerpendicularBisectorConstructor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 035 | TriangleCenterConstructor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 036 | CircleConstructor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 037 | TangentConstructor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 038 | MidpointAndRatioConstructor | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 039 | ReflectionConstructor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 040 | RotationConstructor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 041 | HomothetyConstructor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 042 | SimilarityConstructor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 043 | EquilateralTriangleConstructor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 044 | MultiConstraintConstruction | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 045 | ImplicitGeometrySolver | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 046 | ConstructionDependencyGraph | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 047 | ConstructionExistenceChecker | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 048 | ConstructionUniquenessChecker | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 049 | ConstructionEquivalenceChecker | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 050 | AuxiliaryPointValidator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 098 | DeductiveRuleRegistry | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 099 | DDAR1CompatibilityRules | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 100 | DDAR2RuleSet | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 101 | RuleConditionChecker | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 102 | TheoremInstantiationEngine | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 103 | SemiNaiveDeduction | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 104 | IndexedRuleMatching | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 105 | SimilarityShapeHasher | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 106 | CyclicAngleHasher | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 107 | TriangleCongruenceEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 108 | TriangleSimilarityEngine | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 109 | CircleTheoremEngine | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 110 | TriangleCenterTheorems | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 111 | MidpointTheorems | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 112 | ParallelismTheorems | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 113 | PerpendicularityTheorems | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 114 | TangentChordTheorems | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 115 | GeneralizedCentralAngleTheorem | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 116 | InscribedAngleTheorems | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 117 | ChordEqualityTheorems | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 118 | TriangleAngleBisectorTheorems | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 119 | PointEqualityDeduction | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 120 | GoalDirectedInference | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 121 | DeductiveFixedPointEngine | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 122 | InferenceCompletenessAudit | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 123 | GeometryConstraintCompiler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 124 | EquationResidualBuilder | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 125 | InequalityResidualBuilder | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 126 | RandomDiagramInitializer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 127 | ConstructiveDiagramInitializer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 128 | HeuristicDiagramInitializer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 129 | LocusBasedInitializer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 130 | MultipleDiagramCandidates | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 131 | DifferentiableGeometryLoss | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 132 | AdamGeometryOptimizer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 133 | GaussNewtonSolver | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 134 | LevenbergMarquardtSolver | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 135 | NonDegeneracyLoss | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 136 | ScaleNormalization | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 137 | TopologyConstraintEvaluator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 138 | MultipleSolutionHandler | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 139 | NumericalStabilityMonitor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 140 | AdaptivePrecisionEvaluator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 141 | IntervalGeometryValidator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 142 | DiagramBranchExplorer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 143 | ConstraintSatisfactionVerifier | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 144 | DiagramEnsemble | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 145 | MovingPoint | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 146 | FixedPoint | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 147 | MovementDependency | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 148 | LocusCircleThroughPoint | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 149 | LocusFixedRadiusCircle | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 150 | LocusLineThroughPoint | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 151 | LocusPerpendicularBisector | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 152 | LocusParallelLine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 153 | LocusPerpendicularLine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 154 | LocusPointOnFixedLine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 155 | LocusPointOnFixedCircle | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 156 | LocusFixedDistance | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 157 | LocusFixedDirection | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 158 | LocusFixedAngle | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 159 | MovementDependencyClosure | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 160 | LocusTheoremGenerator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 161 | LocusProofVerifier | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 414 | CONS: catálogo unificado com AGS | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 415 | num_check: proteger degenerescência | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 419 | Closure: núcleo DDAR2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 420 | Closure.add: checar premissas | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 421 | _merge: limitar perda de completude | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 423 | r_simtri_ang: orientação exata | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 424 | r_cycang: assinatura angular | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 425 | Closure.close: ponto fixo | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 438 | parse_goal: objetivos AG2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 439 | realize: restrições múltiplas | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 440 | add_aux: auxiliares compostos | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 446 | AGS: construções AG2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 447 | ag_build: não construtivo e overlap | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 448 | ag_goal: objetivos gerais | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |

### Fase 3: Geração sintética, datasets e cobertura

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 183 | RandomGeometryGenerator2 | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 184 | LargeDiagramSampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 185 | ConstructionDistributionSampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 186 | TheoremCandidateExtractor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 187 | DeepProofGenerator | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 188 | AuxiliaryConstructionExtractor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 189 | DependencyDifference2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 190 | ReverseTopologicalPruning | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 191 | PremiseMinimizer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 192 | GoalDiversitySampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 193 | LocusProblemSampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 194 | ComputeValueProblemSampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 195 | NonConstructiveProblemSampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 196 | MultiAuxiliaryProblemSampler | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 197 | DifficultyEstimator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 198 | CurriculumDatasetBuilder | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 199 | AuxiliaryBalanceSampler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 200 | ProofComplexityBalancer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 201 | GeometricFamilyDeduplicator | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 202 | GraphIsomorphismDeduplicator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 203 | DatasetContaminationDetector | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 204 | IndependentValidationSplit | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 205 | SyntheticDataQualityGate | VERIFIED_SUBSET | Expandir para toda a semântica, incluir casos adversariais e comparar com referências externas. |
| 206 | ShardedDatasetWriter | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 207 | StreamingDatasetReader | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 208 | DistributedDataGenerator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 209 | DatasetCheckpointing | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 210 | DatasetStatistics | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 427 | Cfg: suportar diagramas maiores | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 428 | build_diagram: geometria complexa | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 429 | make_records: diversidade de objetivos | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 430 | _one_goal: auxiliares e prova | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 431 | _dedupe_bucket: dedupe estrutural | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 433 | cmd_tokenize: nomes/constantes | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |

### Fase 4: Modelo neural, SKEST e análise simbólica

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 211 | GPUTransformerBackend | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 212 | TransformerDecoder2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 213 | SparseMixtureOfExperts | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 214 | ExpertRouter | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 215 | ExpertLoadBalancer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 216 | EfficientAttention | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 217 | KVCache | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 218 | LongContextManager | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 219 | DynamicGeometryTokenizer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 220 | ProofReferenceTokenizer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 221 | GeometryStructuredEmbedding | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 222 | FullProofLanguageModeling | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 223 | AuxiliaryPointPredictionHead | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 224 | MathematicalPretrainingAdapter | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 225 | MultimodalGeometryEncoder | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 226 | MixedPrecisionTraining | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 227 | DistributedTraining | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 228 | GradientAccumulation | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 229 | TrainingScheduler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 230 | TrainingCheckpointManager | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 231 | ModelEvaluationSuite | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 232 | ModelEnsemble | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 233 | NeuralInferenceServer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 234 | ModelDistillation | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 235 | InferenceQuantization | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 236 | SearchState | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 237 | SearchTree | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 238 | BeamSearch2 | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 239 | SharedKnowledgeWorkspace | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 240 | CrossTreeKnowledgeTransfer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 241 | InterestingFactExtractor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 242 | SharedFactProofValidator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 243 | SharedFactDependencyFilter | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 244 | MultipleModelSearch | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 245 | SingleAuxiliaryTree | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 246 | MultiAuxiliaryTree | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 247 | OperatorBalancedTree | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 248 | DeepNarrowSearch | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 249 | ShallowWideSearch | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 250 | SearchStrategyScheduler | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 251 | AsynchronousNeuralWorkers | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 252 | AsynchronousDDARWorkers | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 253 | DistributedJobQueue | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 254 | DynamicWorkerAllocation | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 255 | SearchTranspositionTable | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 256 | SearchStateCanonicalizer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 257 | SearchBranchPruner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 258 | ProofProgressScorer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 259 | CandidateNoveltyScorer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 260 | AuxiliaryConstructionRanker | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 261 | TopKSampler | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 262 | TemperatureSampler | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 263 | GrammarConstrainedDecoder | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 264 | MultiSampleDecoder | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 265 | AdaptiveSearchBudget | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 266 | GlobalSearchDeadline | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 267 | SearchMemoryManager | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 268 | SearchReplayLogger | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 269 | SearchEnsembleController | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 270 | CertifiedProofTermination | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 271 | PremiseDeductionAnalyzer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 272 | GoalAssumptionAnalyzer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 273 | NumericalRelationDiscoverer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 274 | AnalysisSetDifferencer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 275 | AnalysisSerializer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 276 | AnalysisContextEncoder | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 277 | NumericalFactConfidenceFilter | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 278 | GoalConditionIsolation | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 279 | AnalysisContextCompressor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 280 | AnalysisAblationEvaluator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 432 | VOCAB: expansão robusta | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 434 | Model: backend GPU e cache | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 435 | AdamW: treinamento distribuído | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 436 | cmd_train: aceleração GPU | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 441 | lm_propose: grammar constrained | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 442 | lm_propose: correção do contexto | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 443 | solve: SKEST | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 444 | solve: deadline global | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |

### Fase 5: Infraestrutura, benchmark e avaliação externa

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 359 | DistributedExecutionCoordinator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 360 | DDARWorkerPool | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 361 | NeuralInferenceWorkerPool | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 362 | GPUModelServing | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 363 | DynamicBatchingEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 364 | NativeGeometryCore | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 365 | PythonNativeBindings | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 366 | SharedFactDatabase | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 367 | TransactionalProofStorage | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 368 | DistributedCache | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 369 | MemoryMappedDataset | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 370 | DistributedCheckpointing | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 371 | WorkerFaultRecovery | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 372 | ResourceQuotaManager | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 373 | ClusterTelemetry | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 374 | PerformanceProfiler | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 375 | ProofSearchTraceDatabase | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 376 | ExperimentReproducibilityManager | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 377 | ContainerizedDeployment | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 378 | InferenceCostOptimizer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 379 | GeometryUnitTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 380 | ConstructionPropertyTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 381 | DeductionRuleTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 382 | AlgebraicSoundnessTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 383 | DegeneracyRegressionTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 384 | OrientationRegressionTests | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 385 | NumericVsSymbolicTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 386 | ProofCertificateTests | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 387 | AG1DifferentialTests | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 388 | AG2DDARDifferentialTests | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 389 | IMOAG30Benchmark | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 390 | IMOAG50Benchmark | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 391 | IMOSLAG30Benchmark | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 392 | JGEXAG231Benchmark | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 393 | ExternalGeometryBenchmarkAdapter | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 394 | UnseenProblemBenchmark | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 395 | BenchmarkContaminationAudit | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 396 | FormalizationCoverageReport | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 397 | DiagramConstructionReport | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 398 | DDAROnlySolveRate | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 399 | NeuralOnlyAblation | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 400 | NeuroSymbolicSolveRate | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 401 | SearchStrategyAblation | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 402 | ComputationalBudgetParity | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 403 | ProofVerificationRate | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 404 | FalsePositiveCounter | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 405 | SolverFailureClassifier | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 406 | PerProblemDiagnosticReport | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 407 | ConfidenceIntervalEvaluator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 408 | MultipleSeedBenchmark | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 409 | DeterministicReplay | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 410 | AdversarialGeometryTestSuite | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 411 | ContinuousIntegration | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 412 | PerformanceRegressionDetector | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 437 | parse_defs: construções compostas | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 445 | cmd_eval: avaliação externa | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 449 | cmd_agbench: buscar e provar | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 450 | cmd_selftest: regressão profunda | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |

### Fase 6: Matemática avançada e estratégias de pesquisa

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 296 | InversionGeometryEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 297 | InversionTheoremLibrary | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 298 | RadicalAxisEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 299 | RadicalCenterTheorems | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 300 | CirclePowerEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 301 | MiquelTheoremEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 302 | ProjectiveGeometryEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 303 | HomogeneousCoordinateSystem | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 304 | CrossRatioEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 305 | HarmonicDivisionEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 306 | PascalTheoremEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 307 | DesarguesTheoremEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 308 | PolynomialGeometryCompiler | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 309 | GroebnerBasisEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 310 | WuMethodEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 311 | PolynomialIdealReasoner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 312 | AlgebraicCoordinateProver | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 313 | ComplexPlaneGeometryEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 314 | VectorGeometryEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 315 | TrigonometricIdentityEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 316 | SymbolicEquationSubstitution | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 317 | NonlinearEquationSolver | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 318 | HybridProverRouter | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 319 | CrossMethodLemmaExchange | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 320 | GeometryInequalityAST | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 321 | OrderReasoningEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 322 | TriangleInequalityEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 323 | GeometricAMGMEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 324 | SumOfSquaresProver | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 325 | RealAlgebraicInequalitySolver | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 326 | BetweennessReasoner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 327 | ConvexityReasoner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 328 | InsideOutsideReasoner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 329 | OrientedAngleInequalityEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 330 | GeometricInequalityRuleLibrary | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 331 | QuantifiedGeometryLogic | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 332 | ParametricPointFamilies | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 333 | InductionProofEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 334 | Geometry3DLanguage | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 335 | SpatialIncidenceEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 336 | SpatialAngleDistanceEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 337 | SpatialTransformationEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 338 | DimensionAwareProofChecker | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 339 | HierarchicalProofPlanner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 340 | SubgoalGenerator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 341 | BackwardChainingEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 342 | BidirectionalProofSearch | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 343 | LemmaDiscoveryEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 344 | AuxiliaryConstructionPolicy | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 345 | NeuralValueFunction | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 346 | MonteCarloTreeSearch | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 347 | ProofGuidedReinforcementLearning | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 348 | SymbolicRewardModel | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 349 | FailedSearchLearning | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 350 | HardProblemReplayBuffer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 351 | CounterexampleGuidedSearch | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 352 | SearchDiversificationPolicy | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 353 | AdaptiveComputeAllocator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 354 | RecursiveProblemDecomposer | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 355 | ProofStrategyPortfolio | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 356 | VerifiedLemmaMemory | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 357 | NovelTheoremMiner | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 358 | AutomatedStrategySelection | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |

### Fase 7: Formalização natural, diagramas e interface

| ID | Requisito | Estado | Próxima ação |
|---:|---|---|---|
| 281 | NaturalLanguageGeometryParser | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 282 | MathematicalEntityRecognizer | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 283 | GeometricRelationExtractor | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 284 | GoalExtractor | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 285 | GeometricCoreferenceResolver | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 286 | TopologyLanguageParser | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 287 | NLToDSLTranslator | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 288 | FormalizationCandidateGenerator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 289 | FormalizationConsensusEngine | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 290 | FormalizationConsistencyChecker | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 291 | FormalizationCounterexampleTester | PARTIAL | Criar teste semântico independente, documentação de contrato e diferencial oficial. |
| 292 | TextDiagramConsistencyChecker | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 293 | MultilingualProblemInterface | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 294 | LaTeXGeometryParser | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |
| 295 | NaturalLanguageProofGenerator | MISSING | Implementar a capacidade, testá-la com casos positivos e adversariais e adicionar evidência. |

