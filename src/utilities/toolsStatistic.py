import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import random
from scipy import stats

class Statistic:

    def __init__(self):
        pass

    @staticmethod
    def computing_CV(df, var_targe):
        targe_list = df[var_targe]
        cv = stats.variation(targe_list)

        return cv

if __name__ == "__main__":
    #generate test data
    speed = np.random.randint(0,10,size = 100)
    lifespan = np.random.randint(0,10,size = 100)
    label_list = ['a', 'b','c','d', 'e']
    lable = list()
    for i in range(len(speed)):
        lable.append(random.choice(label_list))
    df = pd.DataFrame({'speed': speed,'lifespan': lifespan, 'lable' : lable})
    #test function
    statistic = Statistic()
    print(statistic.computing_CV(df, 'speed'))
    pass