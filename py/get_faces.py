#get_faces.py
#!/bin/env python
import cv2, os, sys
sys.path.append('face detection')
from detection import *

name = 'people/' + sys.argv[1]

if not os.path.exists(name):
	os.mkdir(name)
	counter = 1
else:
	files = os.listdir(name)
	if files:
		counter = int(files[-1].split('.')[0]) + 1
	else:
		counter = 1

video = cv2.VideoCapture(0)

cv2.namedWindow('Video Feed', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Saved Face', cv2.WINDOW_NORMAL)
while True:

	ret, frame = video.read()

	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face_coord = detect_frontal_face(frame_gray)
	if len(face_coord) > 0:
		frame = draw_faces(frame,face_coord)
		face = cut_faces(frame_gray,face_coord)
		face = normalize_faces(face)[0]
		cv2.imshow('Saved Face',face)
		cv2.imwrite(name + '/' + str(counter) + '.jpg' ,face)
		print 'Images Saved:' + str(counter)
		counter += 1
    
	cv2.imshow('Video Feed',frame)

	if cv2.waitKey(500) & 0xFF == 27:
		break

video.release()
cv2.destroyAllWindows()
