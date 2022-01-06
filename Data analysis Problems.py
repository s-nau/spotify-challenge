# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:15:25 2022

@author: shimm
"""
from os import chdir
import pandas as pd
import numpy as np
import matplotlib as mlp
chdir(r"C:\Users\shimm\Downloads")
#%%
# =============================================================================
                                        # a
# =============================================================================
data = pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
m = np.mean(data["order_amount"])
#3145.128
# as we can see that this is what we get for the AOV,
#%%
# we need to divide by the number of orders for each time, element wise division
dived = np.divide(data["order_amount"], data["total_items"]) 
# element wise division
real_m = np.mean(dived)
# 387.7428
#%%
# =============================================================================
                                                # b
# =============================================================================
# The metric that I would report for this data set would be the median of
# the order_amount/total_items. The reason that I would use the median is because
# it will give a lot more information than the mean as it will not be affected
# as much by the outliers. 
# Further, it gives a good summary of most of the information in the data. 
# =============================================================================
                                        # c
# =============================================================================
median = np.median(dived)
#153.0
