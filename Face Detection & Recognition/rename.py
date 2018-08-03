import os

path = os.path.join(os.getcwd(),'test-data')
files = os.listdir(path)
files.sort()
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1