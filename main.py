
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/Ice Cream.csv')

# Definir X (DataFrame) e y (Séries)
X = df[['Temperature']]
y = df['Revenue']

# Dividir os dados em Treino e Teste:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print('Tamanho do conjunto de treino:', X_train.shape)
print ('Tamanho do conjunto de teste: ', X_test.shape)

# Criando o modelo de Regressão Linear
model = LinearRegression()

# Treinando o modelo
model.fit(X_train, y_train)

# o predict pega cada valor do X_test e vai colocar na formula que o modelo aprendeu no treino:
y_pred = model.predict(X_test)
print(y_pred)