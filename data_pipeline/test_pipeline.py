#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import pandas as pd
import numpy as np
import pickle
from model.model_pipeline import load_model, predict_price, load_saved_columns

class TestModelPipeline(unittest.TestCase):

    def setUp(self):
        self.model_path = r"C:\Users\lenovo\Desktop\Project\Ennovate_Test\pune_house_price_model.pickle"
        self.model = load_model(self.model_path)
        self.data_columns = load_saved_columns() 

    def test_load_model(self):
        self.assertIsNotNone(self.model)
    
    def test_predict_price(self):
        # Example values
        location = 'pashan'
        sqft = 1200
        bath = 2
        bhk = 2
        
        predicted_price = predict_price(self.model, location, sqft, bath, bhk, self.data_columns)
        self.assertIsInstance(predicted_price, float)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestModelPipeline)
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    run_tests()


# In[ ]:




