# Importing the Libraries 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset 
dataset = pd.read_csv('grads.csv')

# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'na', strategy = 'mean', axis = 0)
imputer.fit[:, 3].values

#Add example
