import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn.model_selection import validation_curve, train_test_split
from sklearn.model_selection import learning_curve
from sklearn.model_selection import cross_val_score 
from sklearn.neighbors import KNeighborsClassifier


def get_learning_curve(train_x, train_y, model, train_sizes = np.linspace(0.1 , 1.0, 10), cv =10, n_job = 1):
    
    train_sizes, train_scores, test_scores = learning_curve(estimator = model, X = train_x, y = train_y,
                   train_sizes = train_sizes, cv = cv, n_jobs = n_job)
    
    train_mean = np.mean(train_scores, axis = 1)
    train_std = np.std(train_scores, axis = 1)
    test_mean = np.mean(test_scores, axis = 1)
    test_std = np.std(test_scores, axis = 1)

    plt.plot(train_sizes, train_mean, color = 'blue', label = 'training accuracy')

    plt.fill_between(train_sizes, train_mean + train_std,
                    train_mean - train_std, alpha = 0.15, color = 'blue')
    
    plt.plot(train_sizes, test_mean, color = 'green', linestyle = '--',
             marker = 's', markersize = 5, label = 'validation accuracy')
    

    plt.fill_between(train_sizes, test_mean + test_std,
                    test_mean - test_std, alpha = 0.15, color = 'green')
    
    plt.grid()
    plt.xlabel('Number of training samples')
    plt.ylabel('Accuracy')
    plt.legend(loc = 'lower right')
    plt.ylim([0.8, 1.0])    
    plt.show()

def get_validation_curve(train_x, train_y, model, par_range, param_name,
                         cv =10, ):
    
    train_scores, test_scores = \
        validation_curve(estimator = model, X = train_x, y = train_y,
                         param_range = par_range,
                         param_name = param_name,
                         cv = cv)
    
    train_mean = np.mean(train_scores, axis = 1)
    train_std = np.std(train_scores, axis = 1)
    test_mean = np.mean(test_scores, axis = 1)
    test_std = np.std(test_scores, axis = 1)

    plt.plot(par_range, train_mean, color = 'blue', label = 'training accuracy')

    plt.fill_between(par_range, train_mean + train_std,
                    train_mean - train_std, alpha = 0.15, color = 'blue')
    
    plt.plot(par_range, test_mean, color = 'green', linestyle = '--',
             marker = 's', markersize = 5, label = 'validation accuracy')
    

    plt.fill_between(par_range, test_mean + test_std,
                    test_mean - test_std, alpha = 0.15, color = 'green')
    
    plt.grid()
    plt.xlabel(str(param_name))
    plt.ylabel('Accuracy')
    plt.legend(loc = 'lower right')
    plt.ylim([0.5, 1.0])    
    plt.show()

def k_fold(X, y, model, k = 5, scoring = 'accuracy'):
    scores = cross_val_score(model, X, y, cv= k, scoring= scoring)
    print(scores)
    print(scores.mean())

def k_fold_plot(X, y, k = 5, scoring = 'accuracy'):
    k_range = range(1, 31)
    k_scores = []
    for _k in k_range:
        knn = KNeighborsClassifier(n_neighbors= _k)
        loss = -cross_val_score(knn, X, y, cv= k, scoring = scoring)
        k_scores.append(loss.mean())

    plt.plot(k_range, k_scores)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Cross-Validated MSE')
    plt.show()



if __name__ == '__main__':
    from sklearn.datasets import load_iris
    knn = KNeighborsClassifier(5)
    iris = load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    # k_fold(X, y, knn, k = 10)
    # k_fold_plot(X,y)
    get_learning_curve(train_x = X_train, train_y = y_train, model = knn)
    param_range = [1,2,5,11]

    get_validation_curve(train_x = X_train, train_y = y_train, model = knn,
                         par_range = param_range, param_name = 'n_neighbors')


