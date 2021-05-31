###################################################################
#1.(A)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
from scipy.stats import skew
from scipy import stats
import math
data = pd.read_csv("C:/Users/usach/Desktop/Statistical Datasets/Q1_a.csv")
data1=data[['speed','dist']]
data1.describe()
data1.skew()
data1.kurtosis()
a=stats.kurtosis(data1)
b=stats.skew(data1)
plt.plot(a,b)
stats.describe(data1)
###########################################################################
#1.(b)
data = pd.read_csv("C:/Users/usach/Desktop/Statistical Datasets/Q2_b.csv")
data2=data[['SP','WT']]
data2.kurtosis()
data2.skew()
data2.describe()
stats.describe(data2)
x=stats.kurtosis(data)
y=stats.skew(data)
plt.plot(x,y)

