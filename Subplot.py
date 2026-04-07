import matplotlib.pyplot as plt 
x1 = [1,2,3,4,5,6]
y1= [3,5,6,7,8,9]
plt.subplot(2,2,1) # row,column,plot
plt.title("age")
plt.suptitle("Employee Data")
plt.plot(x1,y1)

x2 = [23,45,6,7,78]
y2 = [12,13,55,67,32]
plt.subplot(2,2,2)
plt.title("Gender")
plt.bar(x2,y2)
plt.savefig("Subplot.png")
plt.show()
