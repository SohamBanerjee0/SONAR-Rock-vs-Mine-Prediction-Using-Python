# -*- coding: utf-8 -*-
"""SonarROCKorMINEPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qwBJ5VGmviyKOx79w0L1Q5WUxcr345WG

IMPORT THE DEPENDENCIES
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""DATA COLLECTION AND PROCESSING"""

sonar_data =  pd.read_csv('/content/sonar.all-data.csv')
sonar_data.head()

"""NUMBER OF EXAMPLES OF ROCK AND MINE"""

sonar_data['R'].value_counts()

sonar_data.groupby('R').mean()

"""MEAN VALUE FOR EITHER ROCK OR MINE"""

x=sonar_data.drop(columns='R', axis=1)
y=sonar_data['R']
print(x)
print(y)

"""Heat Map Generation and Finding out the Corelation between independent variables"""

correlation = sonar_data.corr()
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='RdPu')

"""TRAINING AND TEST DATA

SIZE = 0.036 TRAIN--- 0.825 , TEST--- 0.875
"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.036,stratify=y,random_state=1)
print(x.shape,x_train.shape,x_test.shape)
print(x_train,y_train)

"""MODEL TRAINING --> LOGISTIC REGRESSION"""

model=LogisticRegression()
model.fit(x_train,y_train)

"""ACCURACY ON TRAINING DATA"""

predict1=model.predict(x_train)
training_data_accuracy_score=accuracy_score(predict1,y_train)
print('Accuracy on training data=',training_data_accuracy_score)

"""ACCURACY ON TEST DATA"""

predict2=model.predict(x_test)
test_data_accuracy_score=accuracy_score(predict2,y_test)
print('Accuracy on test data',test_data_accuracy_score)

"""MAKING A PREDICTION SYSTEM"""

input_data=(0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032)
input_data_as_numpy=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy.reshape(1,-1)
predict3=model.predict(input_data_reshaped)
print(predict3)

if(predict3[0]=='R'):
  print("THE OBJECT IS A ROCK")
else:
  print("THE OBJECT IS A MINE")

