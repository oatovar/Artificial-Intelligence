#!/usr/bin/env python3

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

dataset = pd.read_csv("./wdbc.data", header=None) # Import the dataset into a pandas dataframe
x = dataset.iloc[:, 2:].values # Grab the input values which are attributes 3-32 or index 2-31 in an array
y = dataset.iloc[:, 1].values # Grab the output which is the 2nd attribute or index 1 in an array

classifier_sigmoid = MLPClassifier(activation='logistic', solver='lbfgs')
classifier_tanh = MLPClassifier(activation='tanh', solver='lbfgs')
classifier_relu = MLPClassifier(activation='relu')
classifier_soft_plus = MLPClassifier(activation='identity')

classifier_sigmoid.fit(x,y)
classifier_tanh.fit(x,y)
classifier_relu.fit(x,y)
classifier_soft_plus.fit(x,y)

# 10-Fold Cross Validation occurs here for every algo.
score_sigmoid = cross_val_score(classifier_sigmoid, x, y, cv=10)
score_tanh = cross_val_score(classifier_tanh, x, y, cv=10)
score_relu = cross_val_score(classifier_relu, x, y, cv=10)
score_soft_plus = cross_val_score(classifier_soft_plus, x, y, cv=10)

print("Validation for Sigmoid Activation Accuracy: %0.2f (+/- %0.2f)" % (score_sigmoid.mean(), score_sigmoid.std() * 2))
print("Validation for Tanh Activation Accuracy: %0.2f (+/- %0.2f)" % (score_tanh.mean(), score_tanh.std() * 2))
print("Validation for Relu Accuracy: %0.2f (+/- %0.2f)" % (score_relu.mean(), score_relu.std() * 2))
print("Validation for Softplus Accuracy: %0.2f (+/- %0.2f)" % (score_soft_plus.mean(), score_soft_plus.std() * 2))