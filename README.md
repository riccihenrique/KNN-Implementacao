# KNN-Implementação

Implementação do algoritmo KNN em Python

### Parâmetros
dados: DataSet em formato list <br>
k: Distância dos vizinhos.

### Exemplo usando Pandas e CSV (Não esqueça de instalar as dependências)

import pandas as pd <br>
import numpy as np <br>
from KNearestNeighbors import KNN <br>

dataset = pd.read_csv('iris.csv') <br>
X = np.array(dataset).tolist() <br>
y = [] <br>

for row in X: # Remove a ultima coluna, que são os rótulos e adiciona em y <br>
     &#09y.append(row[len(row) - 1])
     &#09del row[len(row) - 1]

knn = KNN(X, y, k=5) <br>
print(knn.predict([[3, 0.5, 5, 1.3]])) <br>

### Dependências
pip install numpy <br>
pip install pandas <br>
