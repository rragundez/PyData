<img align="right" width="40%" src="http://pydata.org/amsterdam2016/static/images/pydata-logo-amsterdam-2016.png" alt="PyData Amsterdam Logo">
# PyData Tutorial

This repository is created with the intention for people who will attend the PyData tutorial to have a look at the code prior to the tutorial

# Building a Face Recognition System with OpenCV in the blink of an Eye

<img align="right" width="30%" src="http://www.qualogy.com/wp-content/themes/qua/images/q_logo.png" alt="Qualogy Logo">

This notebook was created for the tutorial during the PyData Meeting:
- Author: <font color='red'>Rodrigo Agundez from Qualogy Solutions</font>
- Place: Amsterdam, Papaverweg 265
- Date: Saturday, March 12, 2016
- Time: 16:15
- Room: 2

The goal of this tutorial is to build a simple face recognition system with the use of the opencv library. This tutorial is separated in three parts:
- Basic manipulation techniques of images and video using OpenCV.
- Building our data set of images.
- Training the classification model provided by OpenCV.
- Recognize never seen images by the model.
- Recognize faces from a live video feed.
- Try to trick the face recognition to classify other types of objects.

### A bit about OpenCV
OpenCV is an open source computer vision and machine learning software library.
The library includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to:
<div style="float: left; width: 40%; margin-top: 16px; margin-bottom: 16px">
<ul style="align: left; list-style-type:square">
  <li>Detect Faces</li>
  <li>Recognize Faces</li>
  <li>Identify Objects</li>
  <li>Classify human actions in videos</li>
  <li>Track camera movement</li>
  <li>Track moving objects</li>
</ul>
</div>
<div style="float: right; width: 60%; margin-top: 16px; margin-bottom: 16px">
<ul style="align: left; list-style-type:square">
  <li>Extract 3D models of objects</li>
  <li>Produce 3D point clouds from stereo cameras</li>
  <li>Stitch images together to produce a high resolution image of an entire scene</li>
  <li>Find similar images from an image database</li>
  <li>Remove red eyes from images taken using flash</li>
  <li>Follow eye movements</li>
</ul>
</div>

It has C++, C, Python, Java and MATLAB interfaces and supports Windows, Linux, Android and Mac OS. 

### Requiered Packages for this tutorial
<ul style="list-style-type:square">
  <li>OpenCV (cv2)</li>
  <li>Numpy</li>
  <li>os</li>
  <li>matpotlib</li>
</ul>
