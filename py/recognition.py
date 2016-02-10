#!/bin/env python
import sys, cv2, os, numpy as np
sys.path.append('face detection')
from detection import *

path = 'people/'

people = [person for person in os.listdir(path)]

#people = ['maureen', 'rodrigo', 'arthur', 'gerard']

recognizer = cv2.face.createEigenFaceRecognizer()

images = []
labels = []
labels_people = {}
for i,person in enumerate(people):
	labels_people[i] = person
	for image in os.listdir(path + person):
		images.append(cv2.imread(path + person + '/' + image,0))
		labels.append(i)


recognizer.train(images,np.array(labels))

# input = 'faces data/'
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# for image in os.listdir(input):
# 	print input + image
# 	img = cv2.imread(input + image, 0)
# 	prediction , conf = recognizer.predict(img)
# 	print 'Prediction: ' + str(prediction)
# 	print 'Confidence: ' + str(conf)
# 	cv2.imshow('image',img)
# 	cv2.waitKey(0)

video = cv2.VideoCapture(0)
while(True):
	ret, frame = video.read()
	frame_gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces_coord = detect_frontal_face(frame_gr)
	if len(faces_coord):
		face  = cut_faces(frame, faces_coord)
		face = normalize_faces(face, color=True)[0]
		pred, conf = recognizer.predict(face)
		frame = draw_faces(frame,faces_coord)
		print 'Prediction: ' + labels_people[pred]
		print 'Confidence: ' + str(round(conf)) 	


	cv2.imshow('Video', frame)
	if cv2.waitKey(100) & 0xFF == 27:
		break
video.release()
cv2.destroAllWindows()

