# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:30:26 2021

@author: garci

cute_histograms.py


              |          |    _)      |                                       
    __| |   | __|  _ \   __ \  |  __| __|  _ \   _` |  __| _` | __ `__ \   __|
   (    |   | |    __/   | | | |\__ \ |   (   | (   | |   (   | |   |   |\__ \\
  \___|\__,_|\__|\___|  _| |_|_|____/\__|\___/ \__, |_|  \__,_|_|  _|  _|____/
                                               |___/                          

                             by Andrew Garcia                                                                                                        

"""
print(__doc__)


import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--file_path", default = 'my_spreadsheets/',
                help="path where all your csv files may be. \
                Please update the default with your common folder.")
ap.add_argument("-f", "--filename", default = 'untitled-1.csv',
                help = "enter the name of your file with the .csv extension at the end (e.g. spreadsheet.csv)")

args = vars(ap.parse_args())

x = pandas.read_csv(args["file_path"]+args["filename"])
print(x)

columns = int(input('How many columns?:'))

for i in range(columns):
    plt.figure(x.columns[i]); plt.hist(x.iloc[:,i]); plt.show()