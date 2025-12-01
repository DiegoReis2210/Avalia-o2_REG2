# Avaliação2_REG2
## SME0823 - Modelos de Regressão e Aprendizado Supervisionado II
Diego Deliberalli Reis - 15574238

Um estudo clínico busca investigar fatores associados ao número de espirros diários apresentados por indivíduos com rinite alérgica no período em que as plantas mais liberam o pólen no ar. Para cada participante, foram coletadas as seguintes variáveis:

- nsneeze: número de espirros observados em um dia (variável resposta de contagem).
- alcohol: consumo de bebida alcoólica nas 24 horas anteriores (0 = não, 1 = sim).
- antihist: uso de anti-histamínico no dia da observação (0 = não, 1 = sim).
- smoker: indicador de tabagismo (0 = não fumante, 1 = fumante).
- age: idade do paciente (anos).
- pollen: índice quantitativo de concentração de pólen no ar no dia da observação.


1. Desenvolva uma breve análise exploratória dos dados e avalie as primeiras impressões sobre a associação entre a variável nsneeze e as demais.

2. Ajuste um modelo de Poisson para explicar nsneeze em função das covariáveis alcohol, antihist, smoker, age e pollen. Não é necessário incluir interações. Apresente e interprete:
  - a estimativa dos coeficientes,
  - sua significância estatística.

3. Verifique se há indícios de superdispersão no modelo de Poisson ajustado no item 2 por, pelo menos, dois métodos diferentes. Interprete os resultados e conclua se o modelo de Poisson é adequado em termos de dispersão.

4. Caso seja detectada superdispersão, ajuste um modelo Binomial Negativo com a mesma estrutura de regressão do item 2. Compare os ajustes de Poisson e Binomial Negativa por meio de:
  - desvio (deviance),
  - AIC,
  - gráficos de resíduos componentes do desvio.
  - 
Discuta qual modelo é mais adequado para descrever o número de espirros, justificando sua resposta com base nas métricas e nos diagnósticos gráficos.

5. Com base no modelo considerado mais adequado, estime e interprete o efeito médio marginal:
  - do consumo de álcool (alcohol) sobre o número médio de espirros,
  - do uso de anti-histamínico (antihist).
    
6. Separe os dados em dois subconjuntos, treinamento com 70% das observações e teste com 30% das observações. Com base apenas no conjunto de treinamento, ajuste os modelos Poisson e Binomial Negativo com a mesma estrutura de covariáveis dos itens anteriores. No conjunto de teste, calcule, para cada modelo:
  - o Erro Quadrático Médio (EQM) entre os valores observados de nsneeze e as predições do número médio de espirros;
  - o Erro Absoluto Médio (EAM).

Compare os valores de EQM e EAM obtidos para os diferentes modelos e discuta: qual deles apresenta melhor desempenho preditivo fora da amostra; em que medida as conclusões baseadas em critérios de ajuste (deviance, AIC) coincidem ou não com aquelas baseadas nas medidas de desempenho preditivo (EQM e EAM).

7. Utilizando o modelo escolhido por você, faça previsões do número esperado de espirros para os seguintes perfis:

- Indivíduo A:

alcohol = 0,

antihist = 1,

smoker = 0,

age = 30 anos,

pollen = valor correspondente a um dia de baixa concentração.


- Indivíduo B:

alcohol = 1,

antihist = 0,

smoker = 1,

age = 50 anos,

pollen = valor correspondente a um dia de alta concentração.
