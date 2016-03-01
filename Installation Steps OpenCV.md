<img margin-top="50px" align="right" width="20%" src="http://www.apulus.com/wp-content/uploads/2014/11/OpenCV-Logo.png" alt="OpenCV Logo">
# Steps to install OpenCV 3.0.0 on Ubuntu and OSX (Python 2.7)

<p>Unfortunately OpenCV needs to be compiled from source which can get a bit messy. Here I list the steps that I followed
on Ubuntu 14.04.</p>
<p>We will compile the standard OpenCV source files PLUS the extra modules that contain the face recognition classes
needed for the tutorial</p>
<p>This steps will download the files in your home folder and will deleted them once installation is finished</p>

## Installing pre-requisite packages
`$ apt-get update`<br>
`$ apt-get -y upgrade`<br>
`$ apt-get install -y build-essential cmake git pkg-config libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libgtk2.0-dev
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran python2.7-dev`<br>
`$ pip install numpy`

## Downloading source files
`$ cd ~; git clone https://github.com/Itseez/opencv_contrib.git`<br>
`$ cd opencv_contrib; git checkout 3.0.0`<br>
`$ cd ~; git clone https://github.com/Itseez/opencv.git`<br>
`$ cd opencv; git checkout 3.0.0; mkdir build; cd build`<br>

## Compiling source files
```bash
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D BUILD_EXAMPLES=ON ..
```
`$ make -j4` (The number is amout of processor cores in your system)<br>
`$ sudo make install`<br>
`$ sudo ldconfig`

## Check compiled file
`$ cd /usr/local/lib/python2.7`<br>
Check inside `dist-packages` or `site-packages` that the cv2.so exists. The folder containing the file will be 
used if using a virtual enviroment. In my case it is `dist-packages`, in the following section change the path
to `site-packages` if necessary.

## In case you are using a virtual enviroment
We will make a soft link to the compiled OpenCV<br>
`$ ln -s /usr/local/lib/python2.7/dist-packages/cv2.so 
<PATH TO VIRTUAL ENVIROMENT>/lib/python2.7/site-packages/cv2.so`

## Test
Outside or inside the virtualenv. If it works outside and not inside then check the creation of the soft link command,
most probably there is some mistake in the path.<br>
`$ python`<br>
`>>> import cv2` (if successful you have compiled OpenCV correctly congrats!)<br>
`>>> import cv2.face` (if successfull you also have the extra modules, you are fully set up!)

## Remove downloaded files (Optional)
If you plan to develop your own applications then you might want to keep them.<br>
`$ rm -rf ~/opencv ~/opencv_contrib`
