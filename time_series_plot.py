import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# Prints a 1D array with indices as date
ts= pd.Series(np.random.randn(180), index=pd.date_range('1/1/2018',periods=180))
# print(ts)

# Prints a 2D array of dimension 180 X 3 .So basically we get list of 180 datas for 3 inputs with same index
df= pd.DataFrame(np.random.randn(180,3),index=ts.index,columns=['A','B','C'])
# print(df)
df.cumsum().plot()
plt.show()

# Basically we use it for examining flow of sensex or nifty over the years