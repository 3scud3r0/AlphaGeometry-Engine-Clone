# Estado real da modularização (16/10/2026)

Este PR adiciona os caminhos de módulo propostos em `docs/ROADMAP_AG2_E_UNIVERSALIDADE.md`. **Não é uma reprodução integral do AlphaGeometry 2.** A criação de arquivos, classes ou funções não é evidência de desempenho nos benchmarks oficiais.

## O que é testável agora
- AST tipada e parser conservador para parte dos predicados e formato com coordenadas;
- grafo indexado de fatos, unificação **somente** com justificativa, guardas exatos de degenerescência;
- eliminação racional com testemunho de combinação linear e um solver restrito de ângulos que evita pivôs fracionários não seguros;
- quatro regras declarativas conservadoras com verificação independente (base média, colinearidade por ponto médio com extremos distintos, simetrias de congruência e paralelismo);
- provas JSON `geoforge.proof.v1` verificáveis, exemplos de inferência e rejeição de certificados falsificados;
- adaptadores das bibliotecas matemáticas e de dados já existentes;
- geração de candidatos auxiliares, orçamento global e workspace compartilhado que exige provas;
- validadores de datasets e carregadores de benchmarks que **exigem arquivos externos** e não inventam resultados.

## O que continua NÃO comprovado
1. Compatibilidade completa com todos os predicados, construções e casos especiais do AG2.
2. Equivalência de deduções e desempenho com `google-deepmind/alphageometry2` DDAR2.
3. SKEST real (compartilhamento eficiente de vários modelos e árvores distribuídas).
4. Modelo de linguagem com dados e pesos comparáveis aos usados na pesquisa.
5. CAD/quantifier elimination completo e provador universal de desigualdades.
6. Verificação em IMO-AG-30, IMO-AG-50 e IMOSL-AG-30 segundo os protocolos publicados.
7. Generalização para geometria arbitrária e cobertura de problemas fora de fragmentos decidíveis.

O objetivo da divisão em módulos é tornar essas lacunas explícitas e testáveis. O exemplo `midline` é apenas um **teste local de sanidade**, não uma medição olímpica.

## Comandos

```sh
python -m pip install -r requirements.txt
python -m pytest -q tests_modular/
python geoforge_modular_cli.py prove \
  --given "midp d a b" --given "midp e a c" --given "ncoll a b c" \
  --goal "para d e b c" --out proof.json
python geoforge_modular_cli.py check --path proof.json
```

## Referência de paridade
- https://github.com/google-deepmind/alphageometry2
- https://github.com/google-deepmind/alphageometry2/blob/main/ddar.py
- https://github.com/google-deepmind/alphageometry2/blob/main/elimination.py

A implementação pública inclui o motor simbólico, não os modelos proprietários e toda a infraestrutura de treinamento/busca. Paridade com o sistema completo requer reproduzir capacidades e resultados verificáveis, não simplesmente portar arquivos.

## Latest update — vendored public DDAR2 symbolic core

The PR additionally includes the original source files `ddar.py`, `elimination.py`,
`numericals.py`, `parse.py`, `test.py` and `LICENSE` from
`google-deepmind/alphageometry2` in `vendor/alphageometry2_symbolic/`.
They are distributed under the upstream Apache-2.0 license with a provenance manifest.
A new `geoforge_prover/ddar2_reference.py` invokes the reference implementation
in a separate Python process, with a timeout and explicit status codes.

**Claims permitted:** this repository now contains the publicly released AG2 DDAR
symbolic source and can invoke it for formalized problems with coordinates.

**Claims not permitted:** the GeoForge independent solver is not yet semantically
equivalent to that source, no Gemini weights are included, no published SKEST
full-system search has been reproduced, and 30/30 IMO-AG-30 has not been
verified in the target repository.

Local adapter subprocess tests passed 5/5 in a mock upstream environment;
the real reference-example CI job must finish before declaring its success.
