import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import random
import os
import sys
import datetime
sys.path.append(os.path.abspath(".."))
import config

def pointplot(dataset,var_trend,var_y,var_hue, controlplotshow=True, file_location = True):
    ax =sns.pointplot(x=var_trend,y=var_y,hue=var_hue,data=dataset,ci=None)
    ax.set_title(' the {2} of {0} among {1}'.format(var_hue,var_trend,var_y))
    if file_location:
        plt.savefig("{}/{}status_among_{}_point_chart_created_time_{}.jpg".format(config.pointchart_path, var_y, var_trend, datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")), 
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
    time_list = ["2012", "2013", "2014"]
    time = list()
    for i in range(len(speed)):
        lable.append(random.choice(label_list))
    for i in range(len(speed)):
        time.append(random.choice(time_list))        
    df = pd.DataFrame({'speed': speed,'lifespan': lifespan, 'lable' : lable, 'time' : time})
    #test function
    pointplot(df, "time", "lifespan", "lable", file_location = True)
    pass