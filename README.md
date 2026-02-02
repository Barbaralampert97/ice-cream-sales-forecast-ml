# 🍦 Ice Cream Revenue Prediction with Machine Learning

## 📌 Descrição do Projeto

Este projeto aplica técnicas de **Machine Learning supervisionado** para prever o **faturamento (Revenue)** de vendas de sorvete com base na **temperatura ambiente (Temperature)**. A proposta é analisar como variações climáticas impactam diretamente a demanda por sorvetes e utilizar modelos de regressão para estimar receitas futuras, auxiliando no planejamento de estoque e na tomada de decisão estratégica no varejo.

O modelo foi desenvolvido em Python utilizando bibliotecas de ciência de dados e aprendizado de máquina, com foco em simplicidade, explicabilidade e aplicabilidade acadêmica e profissional.

---

## 🎯 Objetivo

Desenvolver e comparar modelos de regressão capazes de prever o faturamento de vendas de sorvete a partir da temperatura, permitindo:

* Antecipar picos e quedas de demanda
* Apoiar o planejamento de produção e estoque
* Reduzir desperdícios
* Simular cenários de faturamento em diferentes condições climáticas

---

## 📂 Dataset

O projeto utiliza o arquivo **Ice Cream.csv**, que contém as seguintes variáveis:

* **Temperature (°C):** Temperatura ambiente registrada no dia
* **Revenue:** Faturamento obtido com a venda de sorvetes no mesmo período

Essas variáveis permitem modelar a relação entre condições climáticas e desempenho comercial por meio de algoritmos de regressão.

---

## 🧠 Abordagem de Machine Learning

### Tipo de Aprendizado

Este é um problema de **Aprendizado Supervisionado**, pois o conjunto de dados contém:

* Uma variável de entrada conhecida (Temperature)
* Um valor de saída conhecido (Revenue)

O modelo aprende a relação entre essas variáveis a partir de exemplos históricos.

### Tipo de Problema

* **Regressão** → a variável alvo (Revenue) é um valor numérico contínuo.

---

## 🤖 Modelos Utilizados

* **Regressão Linear**
  Modelo base para entender a relação matemática entre temperatura e faturamento.

* **Random Forest Regressor**
  Modelo mais robusto que combina múltiplas árvores de decisão para capturar padrões não lineares.

Os modelos são comparados utilizando métricas de desempenho.

---

## 📊 Avaliação

As métricas utilizadas são:

* **MAE (Mean Absolute Error)** → erro médio absoluto das previsões
* **R² (Coeficiente de Determinação)** → quanto do comportamento do faturamento é explicado pela temperatura

---

## ⚙️ Tecnologias

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/ice-cream-revenue-prediction
   ```

2. Instale as dependências:

   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

---

## 📈 Exemplo de Uso

Entrada:

* Temperature = 32°C

Saída do modelo:

* Revenue previsto = R$ 1.950,00 (valor estimado)

---

## 📚 Estrutura do Projeto

```
ice-cream-revenue-prediction/
│
├── data/
│   └── Ice Cream.csv
├── main.py
├── models/
├── results/
└── README.md
```

---

## 🏁 Conclusão

Este projeto demonstra como técnicas de regressão em Machine Learning podem ser aplicadas para modelar o impacto de variáveis ambientais no desempenho de vendas, oferecendo uma solução simples, interpretável e escalável para apoio à gestão comercial.

---

## 🔮 Trabalhos Futuros

* Adicionar mais variáveis (dia da semana, feriados, promoções, umidade)
* Integrar API de previsão do tempo
* Criar uma interface web para simulação de cenários
* Testar modelos avançados (Gradient Boosting, XGBoost, Redes Neurais)

---

## 👩‍💻 Autora

Barbara Lampert

Projeto desenvolvido para fins acadêmicos e portfólio em Ciência de Dados e Machine Learning.
