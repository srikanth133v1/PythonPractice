import numpy as np
import pandas as p
arr = np.random.rand(3)
print(arr)
arrSeries = p.Series(arr, index=["First", "Second", "t"])
print(arrSeries)
print(type(arrSeries))
print(arrSeries.index)

arr2d = np.random.rand(3,2)
print(arr2d)
print(type(arr2d))
df2d = p.DataFrame(arr2d)
print(df2d)