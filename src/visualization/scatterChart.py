import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import random

def scatterplot(dataset,var_x,var_y, controlplotshow=True, filelocation = False):
    dataset.plot.scatter(x= var_x, y= var_y,title='%s與%s成績關聯性'%(var_x,var_y))
    if filelocation:
        plt.savefig(filelocation, bbox_inches = 'tight', pad_inches = 0.5)

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
    scatterplot(df, "speed", "lifespan")
    pass