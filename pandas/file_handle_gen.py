def loadfile(filename):
    with open(filename,"r") as files:
        
        for f in files:
          yield f
          
for content in loadfile("log.txt"):
    print(content)
        