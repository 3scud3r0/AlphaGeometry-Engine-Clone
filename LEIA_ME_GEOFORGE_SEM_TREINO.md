# GeoForge sem treinamento neural — atualização determinística

Esta atualização **não reproduz integralmente AlphaGeometry 2** e **não promete resolver toda a matemática**. Ela acrescenta uma rota de solução que não requer pesos neurais, ajustes de modelo nem GPU: inferência DDAR local, identidade polinomial exata com testemunhos, álgebra afim racional, saturação algébrica limitada, contraexemplos racionais e construções algébricas exatas.

## 1. Instalação

Mantenha `geoforge.py`, `geoforge_7fases_benchmark.py`, o diretório `geoforge_upgrade_suite/` e os scripts de benchmark na mesma pasta.

```bash
python -m pip install numpy sympy scipy pytest
```

PyTorch é opcional para o resolvedor determinístico; o treinamento demonstrativo pré-existente usa PyTorch.

## 2. Demonstrar um teorema sem treinamento

```bash
python geoforge.py upgrade prove-deterministic \
  --given 'midp d a b' \
  --given 'midp e a c' \
  --given 'ncoll a b c' \
  --goal 'para d e b c' \
  --timeout 5 \
  --out minha_prova.json

python geoforge.py upgrade check-deterministic --path minha_prova.json
```

Saídas semânticas: `proved` significa prova com certificado reproduzido; `counterexample` significa contraexemplo racional para aquele enunciado; `conditional` significa identidade algébrica cuja conclusão depende de uma condição lateral ainda não demonstrada; `unknown` significa que a busca, no orçamento configurado, não encontrou prova nem contraexemplo; `invalid_problem` significa que a entrada contém certas contradições explícitas conhecidas. **`unknown` não significa que a conjectura seja falsa.**

## 3. Refutar uma afirmação falsa

```bash
python geoforge.py upgrade prove-deterministic \
  --given 'para a b c d' \
  --goal 'perp a b c d' \
  --timeout 3
```

Uma coordenada racional só é apresentada como contraexemplo quando todos os dados são validados exatamente e a meta é falsa. Observações numéricas não são convertidas em provas universais.

## 4. Construções algébricas exatas

Crie `construcoes.json`:

```json
{
  "points":{"a":[0,0],"b":[4,0],"c":[0,4]},
  "steps":[
    {"name":"m","operator":"midpoint","args":["a","b"]},
    {"name":"h","operator":"orthocenter","args":["a","b","c"]},
    {"name":"o","operator":"circumcenter","args":["a","b","c"]}
  ]
}
```

Execute:

```bash
python geoforge.py upgrade construct-exact --input construcoes.json --out pontos_exatos.json
```

Este comando constrói pontos para a configuração fornecida; ele não demonstra que uma relação é universalmente verdadeira para todo diagrama admissível.

## 5. Regressões e benchmark permanente

```bash
python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode quick
python EXECUTAR_BENCHMARK_GEOFORGE_SEM_TREINO.py --mode stress
python geoforge_7fases_benchmark.py --mode quick --gate
```

A suíte ampliada contém 5.400 testes gerados de forma determinística em nove famílias, separados da suíte principal para permitir execução independente. O comando de estresse executa também os testes históricos e um mini-benchmark de 12 casos.

```bash
python -m geoforge_upgrade_suite.generate_untrained_matrix
python -m pytest -q geoforge_upgrade_suite/matrix_untrained
python -m geoforge_upgrade_suite.deterministic_benchmark --source geoforge.py
```

Em uma execução local, 2.688 testes existentes e novos da suíte principal, 5.400 testes da matriz e 12 de 12 casos do mini-benchmark passaram. O auditor anterior de 450 requisitos também passou nos testes rápidos e continuou apontando requisitos sem evidência. **Nenhum benchmark oficial de AlphaGeometry 2 foi reproduzido**.

## 6. Técnicas efetivamente implementadas

* `deterministic_ideal.py`: Buchberger limitado sobre Q[x], propagação de proveniência polinomial, certificados de identidade e replay independente.
* `affine_certificate.py`: eliminação de equações lineares sobre racionais, transformação de consequências polinomiais em certificados referenciando as premissas originais.
* `saturation_solver.py`: técnica de Rabinowitsch para polinômios garantidamente não nulos a partir de hipóteses formais, com verificação independente da identidade localizada.
* `deterministic_solver.py`: portfólio sem treinamento, controle de orçamento, registro de hipóteses de não degenerescência, contraexemplos racionais, respostas tipadas e revalidação das afirmações.
* `exact_constructions.py`: pontos algébricos exatos, retas/círculos, interseções com ramos, pés, centros, reflexões e verificação de realização concreta.
* `geoforge.py`: regras dedutivas adicionais cujo certificado inclui explicitamente fatos de não degenerescência usados nos passos.
* `generate_untrained_matrix.py` e `matrix_untrained/`: gerador, manifesto SHA-256 e 5.400 casos de regressão.

## 7. Limites matemáticos e engenharia ainda pendentes

1. A linguagem geométrica e a biblioteca de regras não cobrem todos os predicados e teoremas do AG2.
2. A prova de pertencimento a um ideal polinomial não resolve, por si só, todas as hipóteses de ordem ou o radical real de um ideal.
3. A saturação utiliza limites de tempo, quantidade de termos e tamanho da base; algumas provas válidas retornarão `unknown`.
4. O contraexemplo por busca usa diagramas racionais gerados, podendo não encontrar testemunhos existentes.
5. A busca simbólica não substitui automaticamente a criatividade da busca SKEST nem garante 30/30 em olimpíadas.
6. Nenhuma porcentagem de conclusão das sete fases é inferida apenas de quantidade de linhas ou testes sintéticos aprovados.
7. Os testes oficiais IMO-AG-30, IMO-AG-50 e IMOSL-AG-30 permanecem sem avaliação comparável nesta entrega.

## 8. Contagem transparente de linhas

O projeto atualizado contém aproximadamente 77,9 mil linhas Python incluindo **44.472 linhas de testes gerados**. O algoritmo acrescentado é muito menor que isso. A quantidade de testes materializados não deve ser confundida com novas regras matemáticas ou paridade com AlphaGeometry 2.
