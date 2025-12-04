import matplotlib.pyplot as plt

data = {
    "India":[10,25,32,12,45,22,40],
    "Australia" :[11,22,33,44,55,66,77],
    "over":[1,2,3,4,5,6,7]
}

# plt.figure(figsize=(8,5))
# plt.plot(data["India"],data["over"],marker= "o",linestyle= "-",color="blue")
# plt.plot(data["Australia"],data["over"],marker= "o",linestyle= "-",color="red")
# plt.xlabel("over")
# plt.ylabel("Runs")
# plt.title("RUNS WITH OVERS")
# plt.show()

plt.figure(figsize=(8,5))
plt.bar(data["India"],data["over"],color="blue")
plt.bar(data["Australia"],data["over"],color="red")
plt.xlabel("over")
plt.ylabel("Runs")
plt.title ("RUNS WITH OVERS")
plt.show()