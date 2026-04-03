import matplotlib.pyplot as plt 
import numpy as np 
x=np.random.randint(1,10,50)
y=np.random.randint(10,100,50)
color=np.random.randint(10,100,50)
size=np.random.randint(10,100,50)
plt.scatter(x,y,cmap="viridis",c=color,s=size) #virdis=colormap examples are hot,gist_earth
plt.colorbar()
plt.show()