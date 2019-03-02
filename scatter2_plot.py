import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 

# We first set random no.s to x,y coordinates as some Random no.s also colors and marker sizes
N=45
x=np.random.randn(N)
y=np.random.randn(N)
color=np.random.randn(N)

# As by experience I know that random no.generation give very less values so I multiplied it by 30
size=(30*(np.random.randn(N)))**2

# alpha is for transparency
plt.scatter(x,y,c=color,s=size,alpha=0.5)
plt.show()