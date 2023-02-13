import numpy as np
import pandas as pd
import movecolumn as mc
import os
import sys

#from diccionarios import *



def data_report(df):
    # Sacamos los NOMBRES
    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    # Sacamos los TIPOS
    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    # Sacamos los MISSINGS
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])

    # Sacamos los VALORES UNICOS
    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])

    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)


    return concatenado

def incr(t,m,c):
    r=0
    if  c==0: r=0
    elif t/c>m: r=1
    elif t/c<m:r=2
    return r

def list_features(df):
    features = []

    for c in df.columns:
        t = str(df[c].dtype)
        if "object"  in t:
            features.append(c)
    return features

def transfor(tt,dict1,dict2,dict3):
    ''' tt debe ser el dataframe a tratar
        t desde indicar "tr" para Train y "te" para test'''
    
    tt.drop(columns='Unnamed: 0', inplace=True)

    '''    dict_MultiLine={
                'No': 0,
                'Yes':1,
                'No phone service': 0
                }

    dict_ONLServ={
                'No': 0,
                'Yes':1,
                'No internet service': 0
                }'''
    
    # aplicamos los diccionarios a ciertas variables

    tt = tt.replace({'PhoneService': dict1}, regex=True)
    tt = tt.replace({'PaperlessBilling': dict1}, regex=True)
    if 'Churn'in tt.columns:
        tt = tt.replace({'Churn': dict1}, regex=True)


    # transformamos la varibale TotalCharges a float teniendo en cuenta que hay valores vacios, que son los clientes de Tenure=0


    tt['TotalCharges']=tt['TotalCharges'].apply(lambda x:x.replace(' ','0') if ' ' in x else x)
    tt['TotalCharges']=tt['TotalCharges'].astype(float)

    tt = tt.replace({'MultipleLines': dict1}, regex=True)

    list_com=['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV', 'StreamingMovies']
    
    for i in list_com:

        tt = tt.replace({i:dict2}, regex=True)

    tt=pd.get_dummies(tt,columns = ['InternetService'], prefix=['Int'], dtype='int')
    
    tt['n_pp']=tt['PhoneService']+np.where(tt['Int_No']==0,1,0)
    tt['n_pin']=tt['OnlineSecurity']+tt['OnlineBackup']+tt['DeviceProtection']+tt['TechSupport']+tt[ 'StreamingTV']+tt[ 'StreamingMovies']
    tt['Type_Int']=np.where(tt['Int_DSL']==0,1,0)+np.where(tt['Int_Fiber optic']==0,2,0)

    tt['incr']=0

    for i in range(len(tt.index)):
        tt['incr'][i]=incr(tt['TotalCharges'][i],tt['MonthlyCharges'][i],tt['tenure'][i])


    features=list(dict3.keys())

    tt['PaymentMethod']=tt['PaymentMethod'].apply(lambda x:x.replace(' (automatic)','') if ' (automatic)' in x else x)

    for i in features:

        tt = tt.replace({i: dict3.get(i)}, regex=True)

    if 'Churn'in tt.columns:
        mc.MoveToLast(tt,'Churn')

  
    
    return tt
    

'''def ponlop(tt):
    
        tt['tenure']=np.log1p(tt['tenure'])
        tt['MonthlyCharges']=np.log1p(tt['MonthlyCharges'])
        tt['TotalCharges']=np.log1p(tt['TotalCharges'])'''

def dire(ruta):
        current_dir = os.path.dirname(os.path.realpath(__file__)) 
        filename = os.path.join(current_dir, ruta) 
        return filename