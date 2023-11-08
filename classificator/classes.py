from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

import classificator.pca as pca
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#classifier = RandomForestClassifier()  # Przykład: Random Forest
classifier = SVC()
#classifier = KNeighborsClassifier()

# param_grid = {                                      #KNeighborsClassifier   75,70%
#     'n_neighbors': [3, 5, 7, 9, 11, 13, 15, 20],    #11
#     'weights': ['uniform', 'distance'],             #uniform
#     'algorithm': ['auto', 'ball_tree', 'kd_tree'],  #auto
#     'leaf_size': [10, 20, 30, 100],                 #11
#     'p': [1, 2]                                     #1
# }

param_grid = {                                        #SVC - 81,54%
    'C': [0.1, 1, 10],                                #1
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],   #poly
    #'gamma': ['scale', 'auto', 0.1, 1, 10],           #
    'degree': [0, 1, 2],                              #2
    'coef0': [0.0, 1.0, 2.0],                         #2.0
    'shrinking': [True, False],                       #True
    'decision_function_shape': ['ovo', 'ovr']         #ovo
}


data, labels = pca.get_pca(15)
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
grid_search = GridSearchCV(classifier, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_
print("Najlepsze parametry:", best_params)
best_classifier = grid_search.best_estimator_
y_pred = best_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Dokładność modelu: {:.2f}%".format(accuracy * 100))