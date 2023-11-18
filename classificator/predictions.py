from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle


def make_prediction(alg, i):
    file_pickle = open('../models/'+alg, 'rb')
    chosen_model = pickle.load(file_pickle)
    file_pickle.close()
    data_pickle = open('../models/data', 'rb')
    data = pickle.load(data_pickle)
    data_pickle.close()
    labels_pickle = open('../models/labels', 'rb')
    labels = pickle.load(labels_pickle)
    labels_pickle.close()
    player = [data[i]]
    position = chosen_model.predict(player)
    return position[0], labels[i]

#a, b = make_prediction('dtc', 2)
