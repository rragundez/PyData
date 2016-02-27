""" This module contains functions to manipulate images. Sush as:
- cut_face
- cut_face_ellipse
- normalize_intensity
- resize
"""

import numpy as np
import cv2

#!/usr/bin/env python
# operations.py

def resize(images, size=(100, 100)):
    """ Function to resize the number of pixels in an image.

    To achieve a standarized pixel number accros different images, it is
    desirable to make every picture of the same pixel size. By using an OpenCV
    method we increase or reduce the number of pixels accordingly.

    :param image: image to be resized.
    :param size: desired size for the output image
    :type image: numpy array of 2 or three dimensions
    :type size: tuple containing the size
    :return: the image with the acoordingly pixel size
    :rtype: numpy array of 2 dimensions
    """
    images_norm = []
    for image in images:
        is_color = len(image.shape) == 3
        if is_color:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # using different OpenCV method if enlarging or shrinking
        if image.shape < size:
            image_norm = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
        else:
            image_norm = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
        images_norm.append(image_norm)

    return images_norm


def normalize_intensity(images):
    """ This method normalizes the size and pixel intensity of an image.

    Each image has their own distribution of intensity pixels in grayscale.
    This function normalizes these intensities such that the image uses
    all the range of grayscale values.

    :param image: image to normalize, can be in color or grayscale
    :type image: numpy array of two (graycale) or three (color) dimensions.
    :return: the image in grayscale with the intensities normalized
    :rtype: numpy array of two dimensions.
    """
    images_norm = []
    for image in images:
        is_color = len(image.shape) == 3
        if is_color:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images_norm.append(cv2.equalizeHist(image))
    return images_norm


def cut_face_rectangle(image, face_coord):
    """ Cuts the image to just show the face.

    This function takes the rectangle coordenates around a detected face
    and cuts the original image returning only the detected face image.

    :param image: original image where face was detected
    :param face: rectangle containing (x,y,w,h)
    :type image: numpy array
    :type face: tuple
    :return: image of face only
    :rtype: numpy array
    """
    images_rectangle = []
    for (x, y, w, h) in face_coord:
        images_rectangle.append(image[y: y + h, x: x + w])
    return images_rectangle

def cut_face_ellipse(image, face_coord):
    """ Cuts the image to just show the face in an ellipse.

    This function takes the rectangle coordenates around a detected face
    or faces and cuts the original image with the face coordenates. It also
    surrounds the face with an ellipse making black all the extra
    background.
    or faces

    :param image: original image where faces were detected
    :param faces: object containing the detected face information
    :type image: numpy array
    :type faces: DetectedFace object
    :return: images containing only the face enclose by an ellipse
    :rtype: numpy array
    """
    images_ellipse = []
    for (x, y, w, h) in face_coord:
        center = (x + w / 2, y + h / 2)
        axis_major = h / 2
        axis_minor = w / 2
        mask = np.zeros_like(image)
        # create a white filled ellipse
        mask = cv2.ellipse(mask,
                           center=center,
                           axes=(axis_major, axis_minor),
                           angle=0,
                           startAngle=0,
                           endAngle=360,
                           color=(255, 255, 255),
                           thickness=-1)
        # Bitwise AND operation to black out regions outside the mask
        image_ellipse = np.bitwise_and(image, mask)
        images_ellipse.append(image_ellipse[y: y + h, x: x + w])

    return images_ellipse

def draw_face_rectangle(image, faces_coord):
    """ Draws a rectangle around the face found.
    """
    for (x, y, w, h) in faces_coord:
        cv2.rectangle(image, (x, y), (x + w, y + h), (206, 0, 209), 2)
    return image

def draw_face_ellipse(image, faces_coord):
    """ Draws an ellipse around the face found.
    """
    for (x, y, w, h) in faces_coord:
        center = (x + w / 2, y + h / 2)
        axis_major = h / 2
        axis_minor = w / 2
        cv2.ellipse(image,
                    center=center,
                    axes=(axis_major, axis_minor),
                    angle=0,
                    startAngle=0,
                    endAngle=360,
                    color=(206, 0, 209),
                    thickness=2)
    return image
