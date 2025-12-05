import matplotlib.pyplot as plt

fig,axis = plt.subplots(3,3,figsize=(8,5))

axis[0,0].set_title("scatter")
age = [1,2,3,4]
salary= [100,200,300,400]
axis[0,0].scatter(age,salary,marker="o",color="green")
axis[0,0].set_xlabel('age')
axis[0,0].set_ylabel('salary')

axis[0,1].set_title("bargraph...")
age = [1,2,3,4]
salary= [100,200,300,400]
axis[0,1].bar(age,salary,color="green")
axis[0,1].set_xlabel('age')
axis[0,1].set_ylabel('salary')


axis[1,0].set_title("line...")
age = [1,2,3,4]
salary= [100,200,300,400]
axis[1,0].plot(age,salary,color="green")
axis[1,0].set_xlabel('age')
axis[1,0].set_ylabel('salary')
plt.show()


