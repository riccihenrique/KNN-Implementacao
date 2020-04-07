import pandas as pd
import numpy as np
from KNearestNeighbors import KNN

dataset = pd.read_csv('iris.csv')
X = np.array(dataset).tolist()
y = []

for row in X: # Remove a ultima coluna, que são os rótulos e adiciona em y
    y.append(row[len(row) - 1])
    del row[len(row) - 1]

knn = KNN(X, y, k=5)
print(knn.predict([[3, 0.5, 5, 1.3]]))
