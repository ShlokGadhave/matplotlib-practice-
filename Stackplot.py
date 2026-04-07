import matplotlib.pyplot as plt 
days=[1,2,3,4,5,6,7]
NOP1=[10,30,40,50,60,70,80]
NOP2=[20,45,76,87,20,12,15]
NOP3=[30,50,70,34,56,23,45]
plt.stackplot(days,NOP1,NOP2,NOP3,baseline="sym",labels=["WEEK1",'WEEK2','WEEK3'])
plt.legend()
plt.show()