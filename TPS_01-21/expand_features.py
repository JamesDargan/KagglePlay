'''
This script creates a new train and test dataset with additional features.

Generated Features
var^2: Squared variable
var*var: Multiplicative Interaction Term
var-add-var: Bivariate Addition
var-div-var: Ratio Interaction Term

Output:
- train.csv
- test.csv
'''



import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# Import provided datasets downloaded from Kaggle
train = pd.read_csv('./data/train.csv', index_col='id')
test = pd.read_csv('./data/test.csv', index_col='id')

features = train.columns.drop('target')
target = train.loc[:,['target']]
train.drop(columns = ['target'], inplace = True)


poly2 = PolynomialFeatures(degree = 2, include_bias=False)
ss = StandardScaler()

train_exp = train.copy()
train_exp = poly2.fit_transform(train_exp)
train_exp = pd.DataFrame(train_exp, index = train.index, columns = poly2.get_feature_names(features))


for feat in features:
    for feat2 in features:
        if feat[4:] < feat2[4:]:
            train_exp[feat + '-add-' + feat2] = train_exp[feat] + train_exp[feat2]
            train_exp[feat + '-div-' + feat2] = train_exp[feat]/train_exp[feat2]
            train_exp[feat2 + '-div-' + feat] = train_exp[feat2]/train_exp[feat]

feat_exp = train_exp.columns
train_exp = ss.fit_transform(train_exp)
train_exp = pd.DataFrame(train_exp, index = train.index, columns = feat_exp)
train_exp.columns = train_exp.columns.str.replace(' ', '_')



test_exp = test.copy()
test_exp = poly2.transform(test_exp)
test_exp = pd.DataFrame(test_exp, index = test.index, columns = poly2.get_feature_names(features))


for feat in features:
    for feat2 in features:
        if feat[4:] < feat2[4:]:
            test_exp[feat + '-add-' + feat2] = test_exp[feat] + test_exp[feat2]
            test_exp[feat + '-div-' + feat2] = test_exp[feat]/test_exp[feat2]
            test_exp[feat2 + '-div-' + feat] = test_exp[feat2]/test_exp[feat]


test_exp = ss.fit_transform(test_exp)
test_exp = pd.DataFrame(test_exp, index = test.index, columns = feat_exp)
test_exp.columns = test_exp.columns.str.replace(' ', '_')



# Save files to data subdirectory
train_exp.to_csv('./data/train_exp.csv')
test_exp.to_csv('./data/test_exp.csv')
