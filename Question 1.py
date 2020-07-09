# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:04:50 2020

@author: pc
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

#Load dataset

covid_data=pd.read_excel('H:/8th semester/Data Sciences/covidDatabaseIndia.xls')
covid_data.info()
covid_data.shape

#Co-relation b/w two features (Q1-a)
covid_data.corr()
covid_data_deceased=covid_data[covid_data['Current Status']=='Deceased']

sns.scatterplot(x="Age Bracket",y="Current Status",hue="Gender",data=covid_data_deceased)

#City wise current status (Q1-b)

covid_data_Ap=covid_data[covid_data['Detected State']=='Andhra Pradesh']
covid_data_bihar=covid_data[covid_data['Detected State']=='Bihar']
covid_data_gujarat=covid_data[covid_data['Detected State']=='Gujarat']

sns.swarmplot(x='Patient Number',y='Current Status',hue='Detected State',data=covid_data_Ap)
sns.swarmplot(x='Patient Number',y='Current Status',hue='Detected State',data=covid_data_gujarat)
sns.swarmplot(x='Patient Number',y='Current Status',hue='Detected State',data=covid_data_bihar)


#Max & Min DEceased n Recovered days (Q1-c)

#Recovered
covid_data_dec=covid_data[covid_data['Current Status']=='Recovered']
covid_data_dec['Date Announced'].value_counts().plot.bar(title='Recovered Days/Time')


#Deceased
covid_data_dec=covid_data[covid_data['Current Status']=='Deceased']
covid_data_dec['Date Announced'].value_counts().plot.bar(title='Deceased Days/Time')


