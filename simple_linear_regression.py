# -*- coding: utf-8 -*-
"""Simple Linear Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MTnrlJoW0lokLPMQRCxdT8Hv7CmwELW7
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

data = pd.read_csv('/content/headbrain.csv')
data.head()

data.shape

X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

mean_X = np.mean(X)
mean_Y = np.mean(Y)

n = len(X)

num =0
denom = 0
for i in range(n):
    num += (X[i]-mean_X)* (Y[i]-mean_Y)
    denom +=(X[i]-mean_X)**2
m = num/denom
c = mean_Y - (m*mean_X)

print(m,c)

min_x = np.min(X)-100
max_x = np.max(X)+100
x = np.linspace(min_x,max_x,1000)
y = m*x+c

plt.scatter(X,Y,color='r')
plt.plot(x,y,color='b')
plt.title('Simple Linear Regression')
plt.xlabel('Head size (in cm^3)')
plt.ylabel('Brain weight (in grams)')