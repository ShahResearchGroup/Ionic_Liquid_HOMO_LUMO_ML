# Ionic_Liquid_HOMO_LUMO_ML

The repository contains the raw data and model for the results
published in the article "Mapping the frontier orbital energies of
imidazolium-based cations using machine learning"

Authors: Pratik Dhakal, Wyatt Gassaway, Jindal K. Shah

Correpsonding author: jindal.shah@okstate.edu

doi: 10.1063/5.0155775

The repository contains the following folders:

Training_Data
------------
    train_data_collection.csv: SMILES along with HOMO and LUMO
	energies in eV from DFT calculations

HOMO_Model:
-----------
     scaler_x.save: scaling of features
     scaler_y_save: scaling of the target property (HOMO values)
     final_data_homo.csv: SMILES with corresponding features and the
     HOMO energy predictions
	 best_xgboost_model.joblib: Xgboost model for HOMO energy predictions
	
	
LUMO_Model
	scaler_x.save: scaling of features
     scaler_y_save: scaling of the target property (HOMO values)
     final_data_homo.csv: SMILES with corresponding features and the
     LUMO energy predictions
	 best_xgboost_model.joblib: Xgboost model for LUMO energy predictions
	


External_Data_Set
---------------

Files containing HOMO and LUMO energies of isomers not exposed to the
models.

  cmcn.txt: SMILES of [CmCnim] and HOMO and LUMO energy predictions
  from the model
  
All_Isomers
---------

HOMO and LUMO energies of the entire isomer space (Figure 1)

calculated_xgboost_homo: HOMO energy predictions
calculated_xgboost_lumo: LUMO energy predictions

nomenclature: C10IIMIC10I.csv.csv: Isomers of [C10C10im] cations



