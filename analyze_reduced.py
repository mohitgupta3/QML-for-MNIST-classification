import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import itertools


train_fname = 'train_pca_reservoir_output_concatenated_samples0thru600_FIXED_LABELS.pickle'

with open(
    train_fname,
    'rb'
) as infile:
    train = pickle.load(infile)

test_fname = 'test_pca_reservoir_output_concatenated_samples0thru300_FIXED_LABELS.pickle'

with open(
    test_fname,
    'rb'
) as infile:
    test = pickle.load(infile)


X = train[0]
Y = train[1]
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
all_scores = []
cc = 0
for hyperparameters in itertools.product(
    [6, 8, 10, 12, 15, 20] + [None],
    list(range(2, 5)) + [.01, .5, .8],
    list(range(1, 5)) + [.01, .2, .4],
    ['sqrt', None, 1, 2, 3],
    [1234, 1012, 9999]
):
    if np.random.random() > 0.5:
        continue
    hyperparameters = dict(zip(
        [
            'max_depth',
            'min_samples_split',
            'min_samples_leaf',
            'max_features',
            'random_state'
        ],
        hyperparameters
    ))
    print(hyperparameters)

    clf = DecisionTreeClassifier(**hyperparameters)

    clf.fit(X, Y)

    train_acc = sum([
        int(guess==cor)
        for guess, cor in zip(clf.predict(X), Y)
    ]) / float(len(X))
    print('train accuracy: %s' % train_acc)

    X_t = test[0]
    Y_t = test[1]
    test_acc = sum([
        int(guess==cor)
        for guess, cor in zip(clf.predict(X_t), Y_t)
    ]) / float(len(X))
    print('test accuracy: %s' % test_acc)
    
    all_scores.append((test_acc, train_acc, hyperparameters))
    cc += 1

with open(
    'treeClassifierAllScoresHyperparameterSearch.pickle',
    'wb'
) as outfile:
    pickle.dump(all_scores, outfile)