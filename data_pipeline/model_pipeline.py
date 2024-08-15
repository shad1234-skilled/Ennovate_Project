#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import pandas as pd
import numpy as np
import json


# In[2]:


def load_saved_columns(json_path='columns.json'):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data['data_columns']

def load_model(model_path='lr_model.pickle'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict_price(model,location,sqft,bath,bhk,data_columns):    
    
    x = np.zeros(len(data_columns))
    x[data_columns.index('total_sqft')] = sqft
    x[data_columns.index('bath')] = bath
    x[data_columns.index('bhk')] = bhk
    loc_index = data_columns.index(location) if location in data_columns else -1
        
    x_df = pd.DataFrame([x], columns=data_columns)

    return model.predict(x_df)[0]


# In[ ]:




