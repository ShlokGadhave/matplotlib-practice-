import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
plt.plot(df["Date"],df["Amount"])
plt.show()
