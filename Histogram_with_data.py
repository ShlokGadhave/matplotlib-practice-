import matplotlib.pyplot as plt 
import pandas as pd 
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
plt.hist(df["Payment Mode"],bins=10)
plt.show()