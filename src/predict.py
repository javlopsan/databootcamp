

import os
import sys
import numpy as np
import pandas as pd

from datetime import datetime

import pickle

#fijamos el directorio de trabajo en el del archivo.py

os.chdir(os.path.dirname(os.path.realpath(__file__)))

current_dir = os.path.dirname(os.path.realpath(__file__)) 
filename = os.path.join(current_dir, 'model\production\\gs_ADA_20230213114200') 


with open(filename, 'rb') as archivo_entrada:
    loaded_model = pickle.load(archivo_entrada)


X_test=pd.read_csv('data\\X_test.csv',index_col='customerID')

predi_model=loaded_model.predict(X_test)

prediname=str(datetime.now().strftime('data\\predi_model'+'_'+'%Y%m%d%H%M%S'+'.csv'))

# predi_model.tofile(prediname, sep = ',') 

import csv

with open(prediname, 'w', newline='') as student_file:
    writer = csv.writer(student_file)
    writer.writerow(predi_model)


