import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os


def barchart(dataset, var_x, var_y, topf=None, controlplotshow=True, filelocation = False):
    """
    description:
    -------------------------------------
    param:
    dataset: dataframe
    var_x: x-axis
    var_y: y-axis
    topf: set this one if u wanna filter onyl few levels of X variable
    controlplotshow: whether u wanna show up the plot
    filelocation: where we store the picture

    -------------------------------------
    return: there's no returned object     
                
    """
    df_new = dataset.groupby(by=var_x)[var_y].mean()
    df_new.sort_values(ascending= True)[:topf].plot(kind='bar',title='the average {} of {}'.format(var_x, var_y), rot=0)
    plt.xlabel(var_x)
    plt.ylabel(var_y)

    for counter, value in enumerate(df_new.sort_values(ascending= True)[:topf]):
        plt.text(counter,value, s="%.2f"%value,ha='center', va= 'bottom',fontsize=10)
    if filelocation:
        plt.savefig(filelocation, bbox_inches = 'tight', pad_inches = 0.5)
    if controlplotshow:
        plt.show()
    else:
        plt.close()

def barchart_onevar(dataset, var_x, y_title, filter = False, controlplotshow=True, filelocation = False):
    """
    description:
    -------------------------------------
    param:
    dataset: dataframe
    var_x: x-axis
    y_title: the title of y-axis
    filter: the filter of query 
    controlplotshow: whether u wanna show up the plot
    filelocation: where we store the picture

    -------------------------------------
    return: there's no returned object     
                
    """
    if filter:
        df_new = dataset.query(filter)[var_x].value_counts().sort_index()
    else:
        df_new = dataset[var_x].value_counts().sort_index()
    df_new.plot(kind='bar',title='the distribution of %s'%(var_x), rot=0)
    plt.xlabel(var_x)
    plt.ylabel(y_title)
    if filelocation:
        plt.savefig(filelocation, bbox_inches = 'tight', pad_inches = 0.5)
    if controlplotshow:
        plt.show()
    else:
        plt.close()

    

def histchart_for_continuous(dataset, var_x, y_title , controlplotshow=True, filelocation = False):
    dataset[var_x].plot.hist(title='the distribution of %s'%(var_x))
    plt.xlabel(var_x)
    plt.ylabel(y_title)
    if filelocation:
        plt.savefig( filelocation, bbox_inches = 'tight', pad_inches = 0.5)
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
    barchart(df,var_x = 'lable', var_y= 'speed', controlplotshow= False)
    barchart_onevar(df, "speed", "value",filter= "speed > 5" , controlplotshow= False)
    histchart_for_continuous(df, 'speed', 'value')
    pass