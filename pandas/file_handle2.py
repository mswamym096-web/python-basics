with open("log.txt", "w") as fileobject:
    for i in range(100):
        if i % 2 == 0:
            fileobject.write("i am updating errors\n")
        else:
            fileobject.write("success....\n")


even_count = 0
odd_count = 0
with open("log.txt", "r") as fileobject:
    for line in fileobject:
        if "success...." in line:
            odd_count += 1
        else:
            even_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)