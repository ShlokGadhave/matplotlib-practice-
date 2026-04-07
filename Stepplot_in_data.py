import matplotlib.pyplot as plt 
import pandas as pd 
data=pd.read_excel("expense.xlsx")
df=pd.DataFrame(data)
group=df.groupby("Date")["Amount"].sum() #stepplot is used only for numeric
plt.step(group.index,group.values)
plt.show()