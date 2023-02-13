# Tratamiento de datos
# ==============================================================================

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder
import movecolumn as mc




# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
import matplotlib.font_manager
from matplotlib import style
style.use('ggplot') or plt.style.use('ggplot')
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score,accuracy_score,recall_score,precision_score,f1_score
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from hyperopt import STATUS_OK, Trials, fmin, hp, tpe
import pickle
import datetime
from datetime import datetime


# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

# importación de funciones y diccionarios
# ==============================================================================

import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)



import utils.funciones_churn as fc
import utils.diccionarios as dcc

#fijamos el directorio de trabajo en el del archivo.py

os.chdir(os.path.dirname(os.path.realpath(__file__)))


#cargamos los datos de entrenammiento

'''current_dir = os.path.dirname(os.path.realpath(__file__)) 
filename = os.path.join(current_dir, 'data\\X_train.csv') '''

X_train=pd.read_csv('..\\data\\X_train.csv',index_col='customerID')

'''current_dir = os.path.dirname(os.path.realpath(__file__)) 
filename = os.path.join(current_dir, 'data\\y_train.csv') '''

y_train=pd.read_csv('..\\data\\y_train.csv',index_col='customerID')


#parametrización de los modelos
from sklearn import decomposition
sc = StandardScaler()
pca = decomposition.PCA()
X=X_train
n_components = list(range(1,X.shape[1]+1,1))
dtreeCLF = DecisionTreeClassifier()

reg_log = Pipeline(steps = [
    ("imputer", SimpleImputer()),
    ("selectkbest", SelectKBest()),
    ("scaler", StandardScaler()),
    ("reglog", LogisticRegression())
])
reg_log_param = {
    'selectkbest__k': [18,20,22],
    "imputer__strategy": ['mean', 'median'],
    "reglog__penalty": ['l1', 'l2'],
    "reglog__C": np.logspace(0, 4, 10)}


rfc = Pipeline(steps=[
    ("selectkbest", SelectKBest()),
    ("rfc",RandomForestClassifier())
])

rfc_param = {    
    'selectkbest__score_func':[f_classif],
    'selectkbest__k': [22],
    "rfc__n_estimators": [800],
    "rfc__max_features": [5,9],
    "rfc__max_depth": [2,3,4,5,6],
    'rfc__criterion' : ['gini']
}



svm = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("selectkbest", SelectKBest()),
    ("svm", SVC())
])


svm_param = {
    'selectkbest__k': [22],
    'svm__kernel': ['poly'],
    'svm__C': [0.1],
    'svm__degree': [4],
    'svm__gamma': ['auto']
}

knn = Pipeline(steps = [    
    ("knn_scaler", StandardScaler()),
    ("selectkbest", SelectKBest()),
    ("knn", KNeighborsClassifier())
])

knn_param = {
    'selectkbest__k': [22],
    'knn__leaf_size': [30],
    'knn__n_neighbors':[5],
    'knn__p' : [2]

    
}

Dtree = Pipeline(steps = [ 

    ("sc", sc),
    ("pca", pca),
    ("DtreeCLF", DecisionTreeClassifier())
])

Dtree_param = {
    "DtreeCLF__criterion": ["gini", "entropy"], 
    "DtreeCLF__max_depth": [5,6],
    "DtreeCLF__min_samples_leaf": [1]
}

XGB = Pipeline(steps = [ 

    ("XGB_scaler", StandardScaler()),
    ("selectkbest", SelectKBest()),
    ("XGB", XGBClassifier())
])

XGB_param = {
        'selectkbest__k': [22],
        'XGB__max_depth': [6,10],
        'XGB__gamma': [ 1,5,9],
        'XGB__reg_alpha' :[ 50,100],
        'XGB__reg_lambda' : [ 1],
        'XGB__colsample_bytree' :[ 1],
        'XGB__min_child_weight' : [1],
        'XGB__n_estimators': [150,180, 250],
        'XGB__seed': [0]
    }
ADA = Pipeline(steps = [ 

    ("ADA_scaler", StandardScaler()),
    ("selectkbest", SelectKBest()),
    ("ADA", AdaBoostClassifier())
])

ADA_param = {
        'selectkbest__k': [22],
        'ADA__n_estimators': [100,150,180,250],
        'ADA__base_estimator': [DecisionTreeClassifier(max_depth=6)],
        'ADA__random_state':[0]}

#p configuración de gridsearchcv

gs_reg_log = GridSearchCV(reg_log,
                         reg_log_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)


gs_rfc = GridSearchCV(rfc,
                         rfc_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)

gs_svm = GridSearchCV(svm,
                         svm_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)

gs_knn = GridSearchCV(knn,
                         knn_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)

gs_Dtree = GridSearchCV(Dtree,
                         Dtree_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)

gs_XGB = GridSearchCV(XGB,
                         XGB_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)

gs_ADA = GridSearchCV(ADA,
                         ADA_param,
                         cv = 10,
                         scoring = 'recall',
                         verbose = 1,
                         n_jobs = -1)

#configuración del bucle de entrenamiento

grids = {"gs_reg_log": gs_reg_log,
        "gs_rfc": gs_rfc,
        "gs_svm": gs_svm,
        "gs_knn": gs_knn,
        "gs_dtree": gs_Dtree,
        "gs_XGB": gs_XGB,
        "gs_ADA": gs_ADA
        }   



# implementación del bucle de entrenamiento

for nombre, grid_search in grids.items():
    grid_search.fit(X_train, y_train.values.ravel())
    
    modelname=str(datetime.now().strftime(nombre+'_'+'%Y%m%d%H%M%S'))


    with open(modelname, 'wb') as archivo_salida:
        pickle.dump(grid_search, archivo_salida)

    archivo_salida.close()

