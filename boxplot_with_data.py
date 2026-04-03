import matplotlib.pyplot as plt 
import pandas as pd 
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
plt.boxplot(df["Amount"])
plt.show()
