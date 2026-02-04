
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Importanto métricas para avaliação do modelo
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score


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


# Avaliando o modelo

# Model Score (R²) - mede o qnt a temperatura consegue explicar o faturamento
r2 = model.score(X_test, y_test)  
print('\nR² do modelo:', r2)

r2_test = r2_score(y_test, y_pred)
print('R² Score:', r2_test)

# Erro Médio Absoluto (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae:.2f}')

# Erro Percentual Absoluto Médio (MAPE)
mape = mean_absolute_percentage_error(y_test, y_pred)
print('Mean Absolute Percentage Error (MAPE): %.2f' % mape)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error (MSE): {mse:.2f}')

# Exemplo de previsão para uma temperatura específica
nova_temperatura = pd.DataFrame({'Temperature':[30]})
previsao = model.predict(nova_temperatura)

print(f'\nPrevisão de faturamento para a temperatura de {nova_temperatura["Temperature"][0]} °C é de {previsao[0]:.2f}')