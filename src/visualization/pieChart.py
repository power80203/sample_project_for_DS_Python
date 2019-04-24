#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import seaborn as sns
import random

def pie_chart(dataset,var_aim, topf = None, controlplotshow=True, file_location = False):
    dataset[var_aim].value_counts()[:topf].plot(kind='pie',autopct='%.2f%%', title="%s樣本分布情形"%var_aim)
    plt.axis('equal')
    if file_location:
        plt.savefig(file_location, bbox_inches = 'tight', pad_inches = 0.5)
    if controlplotshow:
        plt.show()
    else:
        plt.close()  

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
    pie_chart(df, "lable")
    pass