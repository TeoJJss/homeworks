import os

dir=os.path.dirname(os.path.abspath(__file__))
file_dir=os.path.join(dir, "first.txt")
# file_dir="first.txt"

# QA
fileHandler=open(file_dir, 'w')
fileHandler.write('Hello World!\n')
fileHandler.close()

fileHandler=open(file_dir, 'a')
fileHandler.write('Hello World again!\n')
fileHandler.close()

# QB
fileHandler=open(file_dir, 'r')
content=fileHandler.read()
fileHandler.close()
print(content)