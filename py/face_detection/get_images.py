#get_images.py
from detection import *
import os, shutil, cv2, sys

class builder(object):

	def __init__(self,root='',dst=''):
		self.origin = root
		self.destination = dst

	def get_images_path(self, folders, extensions=['jpg'], max=10000):
		images_path = []
		for folder in folders:
			print 'Getting Images from ' + self.origin + folder
			for path, _, file_names in os.walk(self.origin + folder):
				images_path.extend([path + '/' + x 
								for x in file_names
								if x.split('.')[1].lower() 
								in extensions])
				if len(images_path) > max:
					break

		print '\n Images retrieved: ' + str(len(images_path))
		return images_path[:max]

	def normalize_faces(self, faces, size=(100,100)):
		for i, face in enumerate(faces):
			face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
			if face.shape < size:
				face_norm = cv2.resize(face,size,
										interpolation = cv2.INTER_AREA)
			else:
				face_norm = cv2.resize(face,size,
										interpolation = cv2.INTER_CUBIC)
			faces[i] = cv2.equalizeHist(face_norm)
		return faces



		return faces

	def save_faces(self, faces, start):
		print '\nSaving images...'
		names = [fname.split('.')[0] for fname in os.listdir(self.destination)]
		for i, face in enumerate(faces):
			cv2.imwrite(self.destination + str(start + 915 + i) + '.jpg',face)
			print 'Image saved: ' + self.destination + str(start + 915 + i) + '.jpg'

	def get_faces(self, images_path):
		print 'Images to analyze: ' +  str(len(images_path))
		count = 0
		for i, image in enumerate(images_path):
			print 'Analyzing Image: ' + str(i+1) + '/' + str(len(images_path))
			print '           Path: ' + image
			frame = cv2.imread(image)
			frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		   	faces_coord = detect_frontal_face(frame_gray)
		   	if len(faces_coord) == 0:
		   		(h, w) = frame_gray.shape
				center = (w / 2, h / 2)
				M = cv2.getRotationMatrix2D(center, 90, 1)
				frame = cv2.warpAffine(frame, M, (h, w))
				frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		   		faces_coord = detect_frontal_face(frame_gray)
		   		if len(faces_coord) == 0:
					(h, w) = frame_gray.shape
					center = (w / 2, h / 2)
					M = cv2.getRotationMatrix2D(center, 90, 1)
					frame = cv2.warpAffine(frame, M, (h, w))
					frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			   		faces_coord = detect_frontal_face(frame_gray)
				   	if len(faces_coord) == 0:
						(h, w) = frame_gray.shape
						center = (w / 2, h / 2)
						M = cv2.getRotationMatrix2D(center, 90, 1)
						frame = cv2.warpAffine(frame, M, (h, w))
						frame_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
				   		faces_coord = detect_frontal_face(frame_gray)
			print 'Total faces found: ' + str(count) + '\n'
			if len(faces_coord) != 0:
				faces = self.normalize_faces(cut_faces(frame,faces_coord))
				self.save_faces(faces,count)
				count  = count + len(faces_coord)
		#return faces
			