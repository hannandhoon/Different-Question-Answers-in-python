# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:45:26 2020

@author: pc
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

covid_countries=pd.read_csv('H:/8th semester/Data Sciences/covid_19_countries.csv')
covid_countries.head()
covid_countries.shape
covid_countries.isnull().values.any()
covid_countries.isnull().sum()

total_countries=covid_countries['Country/Region'].nunique()
print("Total Countries= " + str(total_countries))


covid_data_confirmed=covid_countries['Confirmed'].sum()
covid_data_death=covid_countries['Deaths'].sum()
covid_data_recovered=covid_countries['Recovered'].sum()

total_active_cases=covid_data_confirmed-(covid_data_death+covid_data_recovered)
print("Total Active Cases= " + str(total_active_cases))


print(sales_data[sales_data['File_Type'] == 'Historical']['SKU_number'].count())
print(covid_countries[covid_countries['']