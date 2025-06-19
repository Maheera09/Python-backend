import os

#########Read a file###################
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close() 

########Write to a file ############33
f = open("dele.txt", "a")
f.write("\nThis is new data for demo file three")
f.close()


os.remove("dele.txt") 