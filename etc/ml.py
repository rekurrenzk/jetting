


import numpy as np


    #define matricies via arrays for number of hydrocarbons in molecules (x) and heat release when burned kj/mol (y)

A = np.array([[1, -890], [2, -1411], [3, -1560], [4, -2220], [5, -2878], [6, -3537]])

X = A[:, 0] #hydrocarbons
y = A[:, 1] #heat release
m = len(y)

X = np.stack([np.ones(m), X], axis=1)

#params:
alpha = 0.01
numIter = 1000
theta = np.zeros(2)


for _ in range(numIter):

    h = np.dot(X, theta)
    error = h-y
    gradient = np.dot(X.T, error) / m
    theta = theta - alpha * gradient

print(f"optimized theta is {theta}")