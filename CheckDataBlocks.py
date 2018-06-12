import os
import opusFC
import numpy
import pandas as pd
from ggplot import *
import csv

# Change current working directory to where OPUS files are stored in your computer
os.chdir('file path')

# Check currect working directory
cwd = os.getcwd()

file_list = os.listdir(os.curdir)

# print(file_list)

# Loop through files in file_list
L = []

del file_list[0]  # remove .DS_Store
# f = 'BEP.0'


SNM = []
INS = []
DAT = []
TIM = []
EXP = []
DUR = []
CNM = []
RES = []
ZFF = []
NPT = []
LWN = []
LXV = []
FXV = []
minY = []
maxY = []
dbs=[]


# loop of all files
count = 0



for f in file_list:
    try:
        dbs = opusFC.listContents(f)
        count += 1

        print(count,f)
        print(dbs)


        for i in dbs:

            data = opusFC.getOpusData(f, i)

            print(data.parameters)

    except ValueError:
        print('Cant process a non-Opus file', f)
    continue
