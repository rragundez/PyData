#!/bin/env python
#build_dataset.py
sys.path.append('face_detection')
from get_images import builder
import os, shutil, cv2, sys

'''This file will extract all the images with certain extensions
 inside a given directory. It will also extract images in subdirectories'''

root_path = '/media/rodrigo/CHIPMUNKS/Photos/'
dst_path = 'faces_data/'
# specify which subfolders to look into
folders = ['2014','2015']
extensions = ['jpg']


faces_builder = builder(root_path_mau, dst_path)
images_path = faces_builder.get_images_path(folders)
faces = faces_builder.get_faces(images_path)
# normalize faces to size, grayscale and histogram equalization
faces_norm = faces_builder.normalize_faces(faces)
faces_builder.save_faces(faces_norm)
