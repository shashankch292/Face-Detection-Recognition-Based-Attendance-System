import cv2,os

def detect_faces(f_cascade, color_img, scaleFactor=1.1):
	img_copy = color_img.copy()

	gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

	faces = f_cascade.detectMultiScale(gray, scaleFactor = scaleFactor, minNeighbors=10)

	for (x,y,w,h) in faces:
		cv2.rectangle(img_copy, (x,y), (x+w,y+h), (0,255,0), 2)

	return img_copy


files = os.listdir(os.path.join(os.getcwd(),'test-data'))
files.sort()

haar_file = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

for file in files:
	test_img = cv2.imread('test-data/'+file)	

	test_img = detect_faces(haar_file,test_img)

	cv2.imshow(file,test_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()