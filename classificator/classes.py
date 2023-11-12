from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import classificator.pca as pca
import pickle


def fit_parameters(grid, classifier):
    data, labels = pca.get_pca(15)
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    grid_search = GridSearchCV(classifier, grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    best_classifier = grid_search.best_estimator_
    y_pred = best_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return best_params, best_classifier, accuracy


def save_models():
    data, labels = pca.get_pca(15)
    X_train, _, y_train, _ = train_test_split(data, labels, test_size=0.2, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=11, weights='uniform', algorithm='auto', leaf_size=10, p=1)
    svc = SVC(C=1, kernel='poly', gamma='scale', degree=2, coef0=2.0, shrinking=True)
    rfc = RandomForestClassifier(n_estimators=200, criterion='entropy', max_depth=None, min_samples_split=5, min_samples_leaf=2, max_features='sqrt', bootstrap=True)
    gnb = GaussianNB(var_smoothing=1e-05)
    mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', alpha=0.001)
    dtc = DecisionTreeClassifier(criterion='gini', splitter='best')
    knn.fit(X_train, y_train)
    svc.fit(X_train, y_train)
    rfc.fit(X_train, y_train)
    gnb.fit(X_train, y_train)
    mlp.fit(X_train, y_train)
    dtc.fit(X_train, y_train)
    knn_pickle = open('../models/knn', 'wb')
    pickle.dump(knn, knn_pickle)
    knn_pickle.close()
    svc_pickle = open('../models/svc', 'wb')
    pickle.dump(svc, svc_pickle)
    svc_pickle.close()
    rfc_pickle = open('../models/rfc', 'wb')
    pickle.dump(rfc, rfc_pickle)
    rfc_pickle.close()
    gnb_pickle = open('../models/gnb', 'wb')
    pickle.dump(gnb, gnb_pickle)
    gnb_pickle.close()
    mlp_pickle = open('../models/mlp', 'wb')
    pickle.dump(mlp, mlp_pickle)
    mlp_pickle.close()
    dtc_pickle = open('../models/dtc', 'wb')
    pickle.dump(dtc, dtc_pickle)
    dtc_pickle.close()
    data_pickle = open('../models/data', 'wb')
    pickle.dump(data, data_pickle)
    data_pickle.close()
    labels_pickle = open('../models/labels', 'wb')
    pickle.dump(labels, labels_pickle)
    labels_pickle.close()

grid_knn = {                                                        # KNeighborsClassifier                      75,70%
    'n_neighbors': [3, 5, 7, 9, 11, 13, 15, 20],                    # 11
    'weights': ['uniform', 'distance'],                             # uniform
    'algorithm': ['auto', 'ball_tree', 'kd_tree'],                  # auto
    'leaf_size': [10, 20, 30, 100],                                 # 10
    'p': [1, 2]                                                     # 1
}

grid_svc = {                                                        # SVC                                       81,54%
    'C': [0.1, 1, 10],                                              # 1
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],                 # poly
    'gamma': ['scale', 'auto'],                                     # scale
    'degree': [0, 1, 2],                                            # 2
    'coef0': [0.0, 1.0, 2.0],                                       # 2.0
    'shrinking': [True, False],                                     # True
    'decision_function_shape': ['ovo', 'ovr']                       # ovo
}

grid_rfc = {                                                        # RandomForestClassifier                    80,14%
    'n_estimators': [100, 200],                                     # 200
    'criterion': ['gini', 'entropy'],                               # entrophy
    'max_depth': [None, 10, 30],                                    # None
    'min_samples_split': [2, 5, 10],                                # 5
    'min_samples_leaf': [1, 2, 4],                                  # 2
    'max_features': ['sqrt', 'log2'],                               # sqrt
    'bootstrap': [True, False]                                      # True
}

grid_gnb = {                                                        # GaussianNB                                63,08%
    'var_smoothing': [1e-5, 1e-7, 1e-9, 1e-11, 1e-13, 1e-15]        # 1e-05
}

grid_mlp = {                                                        # MLPClassifier                             80,84%
    'hidden_layer_sizes': [(30,), (50,), (100,), (150,), (200,)],   # (100,)
    'activation': ['identity', 'logistic', 'tanh', 'relu'],         # relu
    'solver': ['sgd', 'adam'],                                      # adam
    'alpha': [0.001, 0.0001, 0.00001]                               # 0.001
}

grid_dtc = {                                                        # DecisionTreeClassifier                    72,43%
    'criterion': ['gini', 'entrophy', 'log_loss'],                  # gini
    'splitter': ['best', 'random'],                                 # best
}

# params, model, acc = fit_parameters(grid_dtc, DecisionTreeClassifier())
# print("Najlepsze parametry:", params)
# print("Dokładność modelu: {:.2f}%".format(acc * 100))
# save_models()
