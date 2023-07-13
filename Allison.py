#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:32:33 2023

@author: twhittock3
"""

# import modules
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt



# read data
data_in = pd.read_csv('F06B3188CF17-05-Jul-2023-21-10-00.csv', header = None, 
                      skiprows = 1, delimiter = ',').values

# extract variables
date = data_in[:,0]
vocs = data_in[:,1]
temp = data_in[:,3]



# loop through all our dates, convert them to datetime objects
for i in range(0, len(date)):
    
    date[i] = datetime.strptime(date[i], '%Y-%m-%d %H:%M:%S')


#fig = plt.figure(figsize = (10,5))

fig1, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx()
fig1.set_size_inches(10,5)

ax1.plot(date, vocs, color = 'darkviolet', lw = 2)
ax2.plot(date, temp, color = 'firebrick', lw = 2)

plt.savefig('test.png', dpi = 200)
plt.show()




