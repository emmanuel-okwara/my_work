#distribution of data kaggle
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
#loading data

loc = './train.csv'
data = pd.read_csv(loc,index_col='Id')

#histogram
plt.figure(figsize=(14,6))
sns.distplot(a=data.SalePrice,kde=False )#we use a to choose the column we would like to plot
#we use kde =False to tell the the graph to plot the histogram chart in the proper way
plt.show()

#density plot
#kernal density plot is a smooted version of a histogram graphs
#to make a kde plot you use sns.kdeplot command ,always set shade=True to color the area below the curve

plt.figure(figsize=(14,6))
sns.kdeplot(data=data.SalePrice,shade=True)
plt.show()