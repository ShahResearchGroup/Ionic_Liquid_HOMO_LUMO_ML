import pandas as pd
import glob, os
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors
import joblib
import sys



files = glob.glob('*.csv')


dpss=pd.DataFrame()


c=0

for i in files:
    print(i)
    dos1 = pd.read_csv(i,sep=",",index_col=False)
    temp_name= i.strip('.csv')
    dt=pd.DataFrame()
    dt = dos1.iloc[:,:]
    dt['system'] = temp_name
    print(dt)
    dt.to_csv('name_change/'+temp_name+'.csv',index=False,sep=';')