import numpy as np
import pandas as pd

# read file into numpy array
pca_reduction_matrix = np.loadtxt('data/pca-reduction-matrix.csv', delimiter=',')
print(pca_reduction_matrix.shape)

# read file into pandas dataframe
df = pd.read_csv('data/onehot.csv')

# drop the first column
df = df.drop('Name', axis=1)

# # drop the Class column
# df = df.drop('Class', axis=1)

# extract first record
data = (df.iloc[0].values)[1:]


# multiply the data with matrix to reduce the dimension
reduced_data = np.matmul(data, pca_reduction_matrix.T)

# print the reduced data
print(reduced_data)

# multiply all the data with matrix to reduce the dimension
reduced_data = np.matmul(df.values[:,1:], pca_reduction_matrix.T)

# export the reduced data to a file
np.savetxt('data/reduced-data.csv', reduced_data, delimiter=',')