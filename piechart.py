import matplotlib.pyplot as plt 
brands=["Oneplus","Blueberry","Nokia","Iphone"]
a=[20,40,50,60]
color=["blue","red","green","black"]
ex=[0,0,0,0.1]
plt.pie(a,labels=brands,colors=color,explode=ex,shadow=True,autopct="%2f",startangle=180) #explode is used to hightlight the function 
plt.show()
#autoput is used to gives values of the data 
#startangle is used for starting angle of th pie hart 
