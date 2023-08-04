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

dt=pd.DataFrame()
dpss=pd.DataFrame()


c=0

dfs = [pd.read_csv(f,sep=",") for f in files]

final_data = pd.concat(dfs,ignore_index=True)

print(final_data.info())


print(final_data.nlargest(10,['LUMO_ev']))


print(final_data.nsmallest(10,['LUMO_ev']))





fig,ax = plt.subplots()
sns.set(style="darkgrid")
ax= sns.violinplot(x="Type", y="LUMO_ev", data=final_data)

ax.set_xlabel('Type',fontdict=font)
ax.set_ylabel('LUMO/eV',fontdict=font)
plt.grid()
plt.tight_layout()
plt.show()


