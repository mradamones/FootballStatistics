import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import utils.modify_df as mod
import pickle


def ingest_data():
    fields_pickle = open('../data/fields', 'rb')
    field_players = pickle.load(fields_pickle)
    fields_pickle.close()
    field_players['Pos'] = field_players['Pos'].str.split(',').str[0]
    labels = field_players.pop('Pos')
    field_players = field_players.drop(['Player', 'Nation', 'Squad', 'Comp', 'Age', 'Born'], axis=1)
    return field_players, labels


def covariance_matrix(array):
    cov_matrix = np.cov(array, rowvar=False)
    cov_matrix = np.round(cov_matrix, 3)
    cov_matrix = np.real_if_close(cov_matrix)
    return cov_matrix


def get_pca(n):
    x, labels = ingest_data()
    x_standard = mod.standardize(x)
    cov = covariance_matrix(x_standard)
    param, vec = np.linalg.eig(cov)
    param = np.real(param)
    vec = np.real(vec)
    sorted_indices = np.argsort(param)[::-1]
    sorted_eigenvectors = vec[:, sorted_indices]
    selected_eigenvectors = sorted_eigenvectors[:, :n]
    new_data = np.dot(x_standard, selected_eigenvectors)
    return new_data, labels


# plt.figure(figsize=(8, 5))
# plt.bar(range(1, len(sorted_eigenvalues) + 1), sorted_eigenvalues)
# plt.xlabel('Numer składowej głównej')
# plt.ylabel('Wartość własna')
# plt.title('Scree Plot')
# plt.show()
# print(param)
get_pca(15)
