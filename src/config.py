import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

#取得本檔案的絕對路徑#
filedirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))





#########################################################
# logging file

logging_main_path = r"{}/reports/logFile".format(filedirpath)



#########################################################
# figures location

barchart_path = r"{}/reports/figures/barchart".format(filedirpath)
boxchart_path = r"{}/reports/figures/boxplot".format(filedirpath)
piechart_path = r"{}/reports/figures/piechart".format(filedirpath)
pointchart_path = r"{}/reports/figures/pointchart".format(filedirpath)
scatterchart_path = r"{}/reports/figures/scatterchart".format(filedirpath)






if __name__ == "__main__":
    print(barchart_path)


    pass