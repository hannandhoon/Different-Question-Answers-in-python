# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:22:46 2020

@author: pc
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

#Load Data
train_data=pd.read_csv('H:/8th semester/Data Sciences/train.csv')

#print top values
train_data.head()
train_data.head(15)

#Print bottom values
train_data.tail()

#Overall data shape and info
train_data.shape
train_data.info()

#Data types
train_data.describe()
train_data.describe(include='all')

#Unique values in dataset
train_data.nunique()
train_data.iloc[:,1:3]
train_data.iloc[1:2,1:4]

#Number of 'RM' & 'RL' values
print(train_data[train_data['MSZoning'] == 'RM']['Id'].count())
print(train_data[train_data['MSZoning'] == 'RL']['Id'].count())

#Random plotting
sns.set(color_codes=True)
x = np.random.normal(size=100)
sns.distplot(x);

#bar-plot
train_data['MSZoning'].value_counts().plot.bar(title="MS-Zonning")
train_data['YrSold'].value_counts().plot.bar(title="Year Sold")

#joint-plot
sns.jointplot(x="MSSubClass", y="LotArea", data=train_data);
sns.jointplot(x="HouseStyle", y="CentralAir", data=train_data);

#swarm-plot
sns.swarmplot(x="MSSubClass", y="LotArea", data=train_data)


#factor-plot
sns.set_context("paper")
sns.factorplot("BedroomAbvGr","BsmtFullBath","Street", data=train_data, kind="bar", palette="muted", legend=True)
sns.factorplot()

#Dist-plot
sns.distplot(train_data['YearBuilt'].dropna(),bins=30,hist=True ,kde=False)

#scatter-plot
sns.set(style="darkgrid")
sns.scatterplot(x="HouseStyle", y="LotArea", data=train_data);


#Line-Plot
train_data.corr()
sns.lineplot(x='GrLivArea', y='SalePrice', data=train_data)

#Box-plot
sns.boxplot(x='HouseStyle',y='LotArea',data=train_data)




#Find missing values
train_data.isnull().values.any()
train_data.isnull().sum()
train_data['LotFrontage'].fillna(0, inplace=True)


#Understanding: 
#1) It has 1460 observations and 81 features.
#2) It has object type,integer type and float type values
#3) It did have null values in Lot area, which is filled with 0
#4)nunique values are too big to compare. minimum nunique value is 5.
#6)Co-relation between features is not good and usually in negative. the best co-relation is between GrLivArea & Sale Price ie 0.7
#7)