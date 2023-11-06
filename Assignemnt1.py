import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = pd.read_csv('wine.csv')

X = data.drop('Customer_Segment', axis=1)
y = data['Customer_Segment']

scaler = StandardScaler()
X_Scaled = scaler.fit_transform(X)

pca = PCA(n_components = 2)
X_pca = pca.fit_transform(X_Scaled)


plt.figure(figsize=(10,6))
plt.scatter(X_pca[:,0],X_pca[:,1],c=y,cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: Wine Dataset')
plt.colorbar(label='Wine Class')
plt.show()
