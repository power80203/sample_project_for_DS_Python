import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import os

script_dir = os.path.dirname(__file__)
rel_path = "../../reports/figures/line_chart/"
abs_file_path = os.path.join(script_dir, rel_path)

def pointplot(dataset,var_x,var_y,var_hue, controlplotshow=True):
    ax =sns.pointplot(x=var_x,y=var_y,hue=var_hue,data=dataset,ci=None)
    ax.set_title('不同%s各年%s表現'%(var_hue,var_y))
    plt.savefig('%s不同%s各年%s表現.png'%(abs_file_path,var_hue,var_y),\
    bbox_inches = 'tight', pad_inches = 0.5)
    if controlplotshow:
        plt.show()
    else:
        plt.close()  
