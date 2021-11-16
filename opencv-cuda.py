import os

print("\n1. ")
os.system("sudo apt update")
os.system("sudo apt upgrade")
print("-------------------------------------------------------")
print("\n2. ")
os.system("sudo apt install build-essential cmake pkg-config unzip yasm git checkinstall")
print("-------------------------------------------------------")
print("\n3. ")
os.system("sudo apt install libjpeg-dev libpng-dev libtiff-dev")
print("-------------------------------------------------------")
print("\n4. ")
os.system("sudo apt install libavcodec-dev libavformat-dev libswscale-dev libavresample-dev")
os.system("sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev")
os.system("sudo apt install libxvidcore-dev x264 libx264-dev libfaac-dev libmp3lame-dev libtheora-dev ")
os.system("sudo apt install libfaac-dev libmp3lame-dev libvorbis-dev")
print("-------------------------------------------------------")
print("\n5. ")
os.system("sudo apt install libopencore-amrnb-dev libopencore-amrwb-dev")
print("-------------------------------------------------------")
print("\n6. ")
os.system("sudo apt-get install libdc1394-22 libdc1394-22-dev libxine2-dev libv4l-dev v4l-utils")
os.system("cd /usr/include/linux")
os.system("sudo ln -s -f ../libv4l1-videodev.h videodev.h")
os.system("cd ~")
print("-------------------------------------------------------")
print("\n7. ")
os.system("sudo apt-get install libgtk-3-dev")
print("-------------------------------------------------------")
print("\n8. ")
os.system("sudo apt-get install python3-dev python3-pip")
os.system("sudo -H pip3 install -U pip numpy")
os.system("sudo apt install python3-testresources")
print("-------------------------------------------------------")
print("\n9. ")
os.system("sudo apt-get install libtbb-dev")
print("-------------------------------------------------------")
print("\n10. ")
os.system("sudo apt-get install libatlas-base-dev gfortran")
print("-------------------------------------------------------")
print("\n11. ")
os.system("sudo apt-get install libprotobuf-dev protobuf-compiler")
os.system("sudo apt-get install libgoogle-glog-dev libgflags-dev")
os.system("sudo apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")

print("-------------------------------------------------------")



continues = """
os.system("cd ~/Downloads")
os.system("wget -O opencv.zip https://github.com/opencv/opencv/archive/refs/tags/4.5.2.zip")
os.system("wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/refs/tags/4.5.2.zip")
os.system("unzip opencv.zip")
os.system("unzip opencv_contrib.zip")
os.system("sudo pip install virtualenv virtualenvwrapper")
os.system("sudo rm -rf ~/.cache/pip")
$ echo "Create a virtual environtment for the python binding module (OPTIONAL)"
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/.cache/pip
$ echo "Edit ~/.bashrc"
$ export WORKON_HOME=$HOME/.virtualenvs
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv cv -p python3
$ pip install numpy

$ echo "Procced with the installation"
$ cd opencv-4.5.2
$ mkdir build
$ cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=ON \
-D ENABLE_FAST_MATH=1 \
-D CUDA_FAST_MATH=1 \
-D WITH_CUBLAS=1 \
-D WITH_CUDA=ON \
-D BUILD_opencv_cudacodec=OFF \
-D WITH_CUDNN=ON \
-D OPENCV_DNN_CUDA=ON \
-D CUDA_ARCH_BIN=7.5 \
-D WITH_V4L=ON \
-D WITH_QT=OFF \
-D WITH_OPENGL=ON \
-D WITH_GSTREAMER=ON \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D OPENCV_PC_FILE_NAME=opencv.pc \
-D OPENCV_ENABLE_NONFREE=ON \
-D OPENCV_PYTHON3_INSTALL_PATH=~/.virtualenvs/cv/lib/python3.8/site-packages \
-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
-D OPENCV_EXTRA_MODULES_PATH=~/Downloads/opencv_contrib-4.5.2/modules \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D INSTALL_C_EXAMPLES=OFF \
-D BUILD_EXAMPLES=OFF ..


------------------------------------------------------------------
-D WITH_CUDNN=ON \
-D OPENCV_DNN_CUDA=ON \
-D CUDA_ARCH_BIN=7.5 \

--   NVIDIA CUDA:                   YES (ver 11.2, CUFFT CUBLAS FAST_MATH)
--     NVIDIA GPU arch:             75
--     NVIDIA PTX archs:
-- 
--   cuDNN:                         YES (ver 8.2.0)
------------------------------------------------------------------

$ nproc
$ make -j8
$ sudo make install

$ sudo /bin/bash -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
$ sudo ldconfig

$ sudo cp -r ~/.virtualenvs/cv/lib/python3.8/site-packages/cv2 /usr/local/lib/python3.8/dist-packages

$ echo "Modify config-3.8.py to point to the target directory" 
$ sudo nano /usr/local/lib/python3.8/dist-packages/cv2/config-3.8.py 

``` 
    PYTHON_EXTENSIONS_PATHS = [
    os.path.join('/usr/local/lib/python3.8/dist-packages/cv2', 'python-3.8')
    ] + PYTHON_EXTENSIONS_PATHS
``` 

"""

print(continues)

