#!/usr/bin/env python3

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

dataset = pd.read_csv("./wdbc.data", header=None) # Import the dataset into a pandas dataframe
x = dataset.iloc[:, 2:].values # Grab the input values which are attributes 3-32 or index 2-31 in an array
y = dataset.iloc[:, 1].values # Grab the output which is the 2nd attribute or index 1 in an array

classifier_linear = SVC(gamma='scale', kernel='linear')
classifier_rbf = SVC(gamma='scale', kernel='rbf')

score_linear = cross_val_score(classifier_linear, x, y, cv=10)
score_rbf = cross_val_score(classifier_rbf, x, y, cv=10)

print("Linear Kernel Accuracy: %0.2f (+/- %0.2f)" % (score_linear.mean(), score_linear.std() * 2))
print("RBF Kernel Accuracy: %0.2f (+/- %0.2f)" % (score_rbf.mean(), score_rbf.std() * 2))