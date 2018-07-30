import numpy as np

def cross_entropy(Y,P):
    Y = np.float(Y)
    P = np.float(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

print(cross_entropy(1,0.7))
