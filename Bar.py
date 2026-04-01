import matplotlib.pyplot as plt 
y=[45,60,78,89,67]
x=["Part1","Part2","Part3","Part4","Part5"]
color=["red","blue","green","yellow","black"]
plt.bar(x,y,color=color,edgecolor="black")
plt.xlabel("Parts of Harry potter",fontsize=17)
plt.ylabel("Popularity of Harry potter",fontsize=17)
plt.title("Harry Potter",fontsize=20)
plt.show()