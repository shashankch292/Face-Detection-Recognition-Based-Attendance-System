import cv2,os
import numpy as np

def detect_face(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')

	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=6)

	if(len(faces)==0):
		return None

	return faces


def prepare_training_data(data_folder_path):
	dirs = os.listdir(data_folder_path)

	faces = []
	labels = []

	for dir_name in dirs:
		if not dir_name.startswith('s'):
			continue

		label = int(dir_name.replace('s',''))

		subject_dir_path = os.path.join(data_folder_path, dir_name)

		subject_image_names = os.listdir(subject_dir_path)

		for image_name in subject_image_names:
			if image_name.startswith('.'):	#ignore system files like .DS_Store
				continue

			image_path = os.path.join(subject_dir_path,image_name)

			image = cv2.imread(image_path)

			# cv2.imshow('Training on image...', image)
			# cv2.waitKey(10)

			facess = detect_face(image)
			if facess is None:
				continue
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			(x,y,w,h) = facess[0]
			face = gray[y:y+w, x:x+h]

			if face is not None:
				faces.append(face)
				labels.append(label)

	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()

	return faces, labels


def draw_rectangle(img, rect):
	(x,y,w,h) = rect
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)


def draw_text(img, text, x, y):
	cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)


def predict(test_img):
	img = test_img.copy()
	faces = detect_face(img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face_list=[]

	for i in range(len(faces)):
		rect = faces[i]
		(x,y,w,h) = rect
		face = gray[y:y+w, x:x+h]

		label, confidence = face_recognizer.predict(face)
		face_list.append(subjects[label])

	return face_list

def find_faces(filepath):
	test_img = cv2.imread(filepath)
	face_list = predict(test_img)
	return face_list

subjects = ['', '1505210048','1505213029','1505210044']

faces, labels = prepare_training_data('training-data')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))
