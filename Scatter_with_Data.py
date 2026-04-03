import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_excel("expense3.xlsx")
df=pd.DataFrame(data)
group_by=df.groupby("Payment Mode")["Amount"].sum()
plt.scatter(group_by.index,group_by.values)
plt.show()

