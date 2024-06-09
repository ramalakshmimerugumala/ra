# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HErDXv0CS9qmZuf1w_ceW0SxegCA9qkn
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic=pd.read_csv('train.csv')
titanic.head()

titanic.shape

sns.countplot(x='Survived',data=titanic)

sns.countplot(x='Survived',hue='Sex',data=titanic,palette='winter')

sns.countplot(x='Survived',hue='Pclass',data=titanic,palette='PuBu')

titanic['Age'].plot.hist()

titanic['Fare'].plot.hist(bins=20,figsize=(10,5))

sns.countplot(x='SibSp',data=titanic,palette='rocket')

titanic['Parch'].plot.hist()

sns.countplot(x='Parch',data=titanic,palette='summer')

titanic.isnull().sum()

sns.heatmap(titanic.isnull(),cmap='spring')

sns.boxplot(x='Pclass',y='Age',data=titanic)

titanic.head()

titanic.drop('Cabin',axis=1,inplace=True)

titanic.head(3)

titanic.dropna(inplace=True)

sns.heatmap(titanic.isnull(),cbar=False)

titanic.isnull().sum()

titanic.head(2)

pd.get_dummies(titanic['Sex']).head()

sex=pd.get_dummies(titanic['Sex'],drop_first=True)
sex.head(3)

embark=pd.get_dummies(titanic['Embarked'])
embark.head(3)

embark=pd.get_dummies(titanic['Embarked'],drop_first=True)
embark.head(3)

Pc1=pd.get_dummies(titanic['Pclass'],drop_first=True)
Pc1.head(3)

titanic=pd.concat([titanic,sex,embark,Pc1],axis=1)
titanic.head(3)

titanic.drop(['Name','PassengerId','Ticket'],axis=1,inplace=True, errors='ignore')
titanic.head(3)

x=titanic.drop('Survived',axis=1)
y=titanic['Survived']

from sklearn.model_selection import train_test_split

from sklearn.model_selection import train_test_split
X=titanic.drop('Survived',axis=1)
y=titanic['Survived']
from sklearn.model_selection import train_test_split
# Assuming X and y are already defined as in your previous code
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=4)

from sklearn.model_selection import train_test_split
# Define X and y before using them
X = titanic.drop('Survived', axis=1)  # Assuming 'titanic' is a DataFrame you have defined
y = titanic['Survived']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=4)

from sklearn.linear_model import LogisticRegression
lm=LogisticRegression()

# Convert all column names to strings
x_train.columns = x_train.columns.astype(str)

# Now try fitting the model again
lm.fit(x_train,y_train)

# Convert all column names in x_test to strings
x_test.columns = x_test.columns.astype(str)

# Now try predicting again
predections = lm.predict(x_test)

from sklearn.metrics import classification_report

from sklearn.metrics import classification_report

from sklearn.metrics import confusion_matrix

