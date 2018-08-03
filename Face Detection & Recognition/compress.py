from PIL import Image
import os

basewidth = 600

path = os.path.join(os.getcwd(),'test-data')
files = os.listdir(path)

files.sort()

for file in files:
	img = Image.open('test-data/'+file)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save('test-data/'+file) 