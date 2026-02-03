
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/Ice Cream.csv')

# Definir X (DataFrame) e y (Séries)
X = df[['Temperature']]
y = df['Revenue']

# Dividir os dados em Treino e Teste:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

print('Tamanho do conjunto de treino:', X_train.shape)
print ('Tamanho do conjunto de teste: ', X_test.shape)