#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
sys.path.append(os.path.abspath(".."))
import config


def create_logger(name, log_file, level=logging.INFO):
    """
    description: create logger to avoid wasting too many time in debuging 
    -------------------------------------
    param:
    var1:
    var2
    -------------------------------------
    return:

    ref: https://realpython.com/python-logging/
                
    """

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger





if __name__ == '__main__':
    #test logging
    # logging.debug('This is a debug message')
    # logging.info('This is an info message')
    # logging.warning('This is a warning message')
    # logging.error('This is an error message')
    # logging.critical('This is a critical message')
    


    logging.basicConfig(filename='{}/app.log'.format(config.logging_main_path) , filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')

  
    pass
    