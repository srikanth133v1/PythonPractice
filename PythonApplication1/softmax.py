import numpy as np;

def softmax(L):
    exp_L = np.exp(L)
    sum_expL = sum(exp_L)
    result = []
    for i in exp_L:
        #result.append(float(i)/sum_expL)
        result.append(i*1.0/sum_expL)
    return result
    pass


print(softmax([1,2]))