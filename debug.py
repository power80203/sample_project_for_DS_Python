#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
The purpose of this file is used for debug mode or test some trickies

"""

def pipelineTest():
    """
    description: just test pipeline
    -------------------------------------
    param:
    var1:
    var2
    -------------------------------------
    return:     
                
    """

    #########################################################
    #test source code __pipeline #
    #########################################################

    # Create a pipeline that standardizes the data then creates a model
    from pandas import read_csv
    from sklearn.model_selection import KFold
    from sklearn.model_selection import cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    # load data
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
    dataframe = read_csv(url, names=names)
    print(dataframe.head())
    array = dataframe.values
    X = array[:,0:8]
    Y = array[:,8]

    #########################################################
    # create pipeline
    estimators = []
    estimators.append(('standardize', StandardScaler()))
    estimators.append(('lda', LinearDiscriminantAnalysis()))
    model = Pipeline(estimators)

    # evaluate pipeline
    seed = 7
    kfold = KFold(n_splits=10, random_state=seed)
    results = cross_val_score(model, X, Y, cv=kfold)
    print(results.mean())

if __name__ == "__main__":

    # test range
    # k = range(0,100,10)
    # for i in k:
    #     print(i)
    import pandas as pd

    df = pd.read_csv(r"Churn_Modelling.csv")
    for x in df.values:
        RowNumber += 1
        print(RowNumber)


    pass