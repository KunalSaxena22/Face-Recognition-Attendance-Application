
# Face Recognition Attendance Application

### Abstract

In this project, we're using individuals' faces to automatically mark attendance, which is crucial for schools and colleges. Instead of the traditional method of calling out names or roll numbers, which takes time, we're employing image processing techniques like face detection and recognition. This means locating faces in images and matching them with stored faces in a database to mark attendance efficiently.


### Introduction

Attendance is crucial for both teachers and students in educational institutions. Traditional methods of taking attendance, like calling out names or roll numbers, are time-consuming and energy-draining. Automatic attendance systems like biometric and RFID have been introduced but still face time constraints and queues. This project presents an automatic attendance system that seamlessly integrates with teaching processes. It eliminates the need for manual identification methods and can be implemented during exams or other teaching activities. Students can easily enroll in the system through a user-friendly interface, avoiding unnecessary stress and disruption.

### Problem Statement

Traditional methods of marking student attendance pose several challenges. These include disruptions to the teaching process, distractions during exams, and difficulties in managing attendance sheets in large classes. The proposed face recognition attendance system aims to simplify attendance tracking by eliminating manual methods like calling names or passing around attendance sheets. It also addresses issues like fraudulent attendance and eliminates the need for manual counting by instructors.

### Aims and Objectives

The objective of this project is to develop face recognition attendance system. Expected 
achievements in order to fulfill theobjectives are:
 To detect the face segment from the video frame.
 To extract the useful features from the face detected.
 To classify the features in order to recognize the facedetected.
 To record the attendance of the identified student.

### Student Attendance System

Arun Katara et al. (2017) discussed the drawbacks of various biometric systems like RFID cards, fingerprints, iris recognition, and voice recognition. While RFID cards are simple, they're prone to fraudulent use. Fingerprint systems are accurate but slow, causing queues during verification. Iris recognition, though accurate, raises privacy concerns due to detailed data collection. Voice recognition, while available, is less accurate. Hence, face recognition emerges as a preferred option for student attendance systems.

### Digital Image Processing

Digital Image Processing involves manipulating digital images for human perception, efficient storage, and machine applications. It revolves around improving pictorial information, storage, transmission, and autonomous machine usage.

### Image Representation in a Digital Computer

Images are represented as 2D light intensity functions. They're discretized into grids and quantized for brightness levels, forming matrices of pixels or pels. Typical images are sized 256x256 or 1024x1024 pixels, quantized to 8 or 24 bits for black-and-white or colored images respectively.

### Steps in Digital Image Processing

Digital image processing comprises acquiring images through sensors, preprocessing to enhance quality, segmentation to identify object parts, selecting features for computer processing, recognition and interpretation of objects, and maintaining a knowledge base for efficient processing and inter-module cooperation.

### Local Binary Patterns Histogram

Local Binary Pattern (LBP) is a straightforward yet effective texture operator used for labeling image pixels based on the surrounding pixel values. It was introduced in 1994 and is widely used for texture classification. Combining LBP with Histograms of Oriented Gradients (HOG) has shown significant improvements in detection performance. By using LBP with histograms, we can represent face images with a simple data vector.

### LBPH Algorithm Overview
#### Parameters:
Radius: Determines the size of the circular local binary pattern around each pixel.
Neighbors: Defines the number of sample points used to construct the pattern.
Grid X and Grid Y: Determine the number of cells in the horizontal and vertical directions, respectively, for grid division.
#### Training the Algorithm:
The algorithm is trained using a dataset containing facial images and corresponding IDs for recognition.
#### Applying the LBP Operation:
This step involves creating an intermediate image by highlighting facial characteristics using a sliding window approach based on the defined parameters.

### Design Requirements
#### Software Implementation
**OpenCV**: Utilized OpenCV 3, a versatile library for image processing with functions including gradient computation, contour detection, Hough transforms, histogram operations, segmentation, filtering, face detection, interest point detection, video processing, and photography. Installation involved copying a script to the Raspberry Pi directory and executing it via terminal commands.

**Python IDE**: Employed Spyder, a feature-rich Python Integrated Development Environment (IDE) for code development. Spyder was chosen for its rich feature set and lightweight nature compared to alternatives like PyCharm. Installation was done via command line.

## Documentation

[Connect me on LinkedIn](https://www.linkedin.com/in/kunal-saxena-engineer/)



