import matplotlib.pyplot as plt
y=[200,300,400,600,700]
x=["Day1","Day2","Day3","Day4","Day5"]
y1=[350,400,650,720,800]
plt.plot(x,y,ls="--",color="black",label="Week1")
plt.plot(x,y1,ls="--",color="red",label="Week2",alpha=0.2) #alpha is trapsnercy lies btw 0 and 1 
plt.legend()
plt.show()