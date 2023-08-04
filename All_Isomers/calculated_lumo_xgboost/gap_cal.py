from typing_extensions import final
import pandas as pd
import glob, os
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors
import joblib
import sys
import import_ipynb
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.ticker as mtick

plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "medium"

plt.rcParams['axes.linewidth'] = 3.2
plt.rcParams['xtick.major.size'] = 7

plt.rcParams['ytick.major.size'] = 7

plt.rcParams['xtick.labelsize'] = 14 
plt.rcParams['ytick.labelsize'] = 14

#######font parameters for the figure
font = {'weight': 'bold',
        'size': 18,
        }

files = glob.glob('*.csv')
dfs = [pd.read_csv(f,sep=",") for f in files]
final_data = pd.concat(dfs,ignore_index=True)



files2 = glob.glob('*.csv')
dfs2 = [pd.read_csv(f,sep=",") for f in files2]
final_data2 = pd.concat(dfs2,ignore_index=True)


print(final_data.info())
print(final_data2.info())
