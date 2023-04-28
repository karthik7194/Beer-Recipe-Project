# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:28:55 2020

@author: Karthik Subramani
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
beer_map = pd.read_excel('201013_Bierrezeptliste_English.xlsx', header=[0,1])
data = pd.read_excel('201013_Bierrezeptliste_English.xlsx', header=[1])
X = data.iloc[:, 3:9].copy()
y = data['Surname']
X_le = preprocessing.LabelEncoder()
X['Aroma'] = X_le.fit_transform(X.Aroma.values)
y_le = preprocessing.LabelEncoder()
y = y_le.fit_transform(y.values.astype(str))
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(X, y)

def predict_beer(input_values, beer_map, data, y_le, neigh):
    suggested_beer = y_le.inverse_transform(neigh.predict(input_values))
    index = data.loc[data['Surname'] == suggested_beer[0]].index
    print(beer_map.iloc[index])

while(1):
    input_values = []
    input_values.append(float(input('Enter Deflection volume [L](1-3000): ')))
    input_values.append(float(input('Enter Alc [% vol](3-10): ')))
    input_values.append(float(input('Enter Bitter value [IBU](10-90): ')))
    input_values.append(float(input('Enter Color [EBC](5-180): ')))
    input_values.append(X_le.transform([input('Enter Aroma (very low, low, moderate, strong or very strong): ')])[0])
    input_values.append(float(input('Enter Carbonation [g / l](1-7): ')))
    predict_beer([input_values], beer_map, data, y_le, neigh)