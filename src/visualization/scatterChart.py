import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import sys
import datetime
sys.path.append(os.path.abspath(".."))
import config

def scatterplot(dataset,var_x,var_y, controlplotshow=True, filelocation = True):
    dataset.plot.scatter(x= var_x, y= var_y,title='the relationship between {}and {}'.format(var_x,var_y))
    if filelocation:
        plt.savefig("{}/the_relationship_between{}_and_{}_scatterchart_created_time_{}.jpg".format(config.scatterchart_path, var_x, var_y, datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")), 
                    bbox_inches = 'tight', pad_inches = 0.5)

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