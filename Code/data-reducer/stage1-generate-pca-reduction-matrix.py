import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Read the data 
df = pd.read_csv('data/onehot.csv')

# Drop the first column
df = df.drop('Name', axis=1)

# Drop the Class column
df = df.drop('Class', axis=1)

# print head
print(df.head())

# fit pca model
pca = PCA(n_components=15)
pca.fit(df)

# transform data
B = pca.transform(df)

# print the shape of the data
print("B.shape",B.shape)

# print the shape of the components
print("pca.components_.shape",pca.components_.shape)

# print head
print(df.head())

# store the components in a file
filename = "data/pca-reduction-matrix.csv"
np.savetxt(filename, pca.components_, delimiter=',')

print("Stored in file:", filename)