import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle

def ingest_data():
    fields_pickle = open('../data/fields', 'rb')
    field_players = pickle.load(fields_pickle)
    fields_pickle.close()
    field_players = field_players.drop(['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Born'], axis=1)
    return field_players


def standardize(array):
    array = array.apply(pd.to_numeric, errors='coerce')
    avg = np.mean(array, axis=0)
    std_dev = np.std(array, axis=0)
    standardized_array = (array - avg) / std_dev
    standardized_array = np.round(standardized_array, 3)
    return standardized_array


def covariance_matrix(array):
    cov_matrix = np.cov(array, rowvar=False)
    cov_matrix = np.round(cov_matrix, 3)
    return cov_matrix

x = ingest_data()
x_standard = standardize(x)
cov = covariance_matrix(x_standard)
param, vec = np.linalg.eig(cov)
#param = np.sort(param)
sorted_indices = np.argsort(param)[::-1]
sorted_eigenvalues = param[sorted_indices]
sorted_eigenvectors = vec[:, sorted_indices]
plt.figure(figsize=(8, 5))
plt.bar(range(1, len(sorted_eigenvalues) + 1), sorted_eigenvalues)
plt.xlabel('Numer składowej głównej')
plt.ylabel('Wartość własna')
plt.title('Scree Plot')
plt.show()
print(param)

N = 15
selected_eigenvectors = sorted_eigenvectors[:, :N]
new_data = np.dot(x_standard, selected_eigenvectors)
print(new_data)
# TODO - wybrac N nowych wartosci i stworzyc na ich podstawie klasyfikator
