import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os
import random


def box_plot(dataset,var_x,var_y,topf=None, controlplotshow=True, file_location = False):
    df_new = dataset.groupby(by=var_x)[var_y].mean()
    ax = sns.boxplot(x=var_x,y=var_y,data=dataset,order=df_new.sort_values(ascending = True)[:topf].index)
    plt.xticks(rotation=45)
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
    box_plot(df, "lable", "speed")
    pass