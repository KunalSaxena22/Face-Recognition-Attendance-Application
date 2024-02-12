# Face-Recognition-Attendance-Systems
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Recognition Attendance Application</title>
</head>

<body>

    <h1>Face Recognition Attendance Application</h1>

    <h2>Abstract</h2>
    <p>In this project, we're using individuals' faces to automatically mark attendance, which is crucial for schools and colleges. Instead of the traditional method of calling out names or roll numbers, which takes time, we're employing image processing techniques like face detection and recognition. This means locating faces in images and matching them with stored faces in a database to mark attendance efficiently.</p>

    <h2>Introduction</h2>
    <p>Attendance is crucial for both teachers and students in educational institutions. Traditional methods of taking attendance, like calling out names or roll numbers, are time-consuming and energy-draining. Automatic attendance systems like biometric and RFID have been introduced but still face time constraints and queues. This project presents an automatic attendance system that seamlessly integrates with teaching processes. It eliminates the need for manual identification methods and can be implemented during exams or other teaching activities. Students can easily enroll in the system through a user-friendly interface, avoiding unnecessary stress and disruption.</p>

    <h2>Problem Statement</h2>
    <p>Traditional methods of marking student attendance pose several challenges. These include disruptions to the teaching process, distractions during exams, and difficulties in managing attendance sheets in large classes. The proposed face recognition attendance system aims to simplify attendance tracking by eliminating manual methods like calling names or passing around attendance sheets. It also addresses issues like fraudulent attendance and eliminates the need for manual counting by instructors.</p>

    <h2>Aims and Objectives</h2>
    <p>The objective of this project is to develop face recognition attendance system. Expected achievements in order to fulfill theobjectives are:</p>
    <ul>
        <li>To detect the face segment from the video frame.</li>
        <li>To extract the useful features from the face detected.</li>
        <li>To classify the features in order to recognize the facedetected.</li>
        <li>To record the attendance of the identified student.</li>
    </ul>

    <h2>Student Attendance System</h2>
    <p>Arun Katara et al. (2017) discussed the drawbacks of various biometric systems like RFID cards, fingerprints, iris recognition, and voice recognition. While RFID cards are simple, they're prone to fraudulent use. Fingerprint systems are accurate but slow, causing queues during verification. Iris recognition, though accurate, raises privacy concerns due to detailed data collection. Voice recognition, while available, is less accurate. Hence, face recognition emerges as a preferred option for student attendance systems.</p>

    <h2>Digital Image Processing</h2>
    <p>Digital Image Processing involves manipulating digital images for human perception, efficient storage, and machine applications. It revolves around improving pictorial information, storage, transmission, and autonomous machine usage.</p>

    <h2>Image Representation in a Digital Computer</h2>
    <p>Images are represented as 2D light intensity functions. They're discretized into grids and quantized for brightness levels, forming matrices of pixels or pels. Typical images are sized 256x256 or 1024x1024 pixels, quantized to 8 or 24 bits for black-and-white or colored images respectively.</p>

    <h2>Steps in Digital Image Processing</h2>
    <p>Digital image processing comprises acquiring images through sensors, preprocessing to enhance quality, segmentation to identify object parts, selecting features for computer processing, recognition and interpretation of objects, and maintaining a knowledge base for efficient processing and inter-module cooperation.</p>

    <h2>Local Binary Patterns Histogram</h2>
    <p>Local Binary Pattern (LBP) is a straightforward yet effective texture operator used for labeling image pixels based on the surrounding pixel values. It was introduced in 1994 and is widely used for texture classification. Combining LBP with Histograms of Oriented Gradients (HOG) has shown significant improvements in detection performance. By using LBP with histograms, we can represent face images with a simple data vector.</p>

    <h3>LBPH Algorithm Overview</h3>
    <p><strong>Parameters:</strong> Radius: Determines the size of the circular local binary pattern around each pixel. Neighbors: Defines the number of sample points used to construct the pattern. Grid X and Grid Y: Determine the number of cells in the horizontal and vertical directions, respectively, for grid division.</p>
    <p><strong>Training the Algorithm:</strong> The algorithm is trained using a dataset containing facial images and corresponding IDs for recognition.</p>
    <p><strong>Applying the LBP Operation:</strong> This step involves creating an intermediate image by highlighting facial characteristics using a sliding window approach based on the defined parameters.</p>

    <h2>Design Requirements</h2>
    <h3>Software Implementation</h3>
    <ul>
        <li><strong>OpenCV:</strong> Utilized OpenCV 3, a versatile library for image processing with functions including gradient computation, contour detection, Hough transforms, histogram operations, segmentation, filtering, face detection, interest point detection, video processing, and photography. Installation involved copying a script to the Raspberry Pi directory and executing it via terminal commands.</li>
        <li><strong>Python IDE:</strong> Employed Spyder, a feature-rich Python Integrated Development Environment (IDE) for code development. Spyder was chosen for its rich feature set and lightweight nature compared to alternatives like PyCharm. Installation was done via command line.</li>
    </ul>

    <h3>Hardware Implementation</h3>
    <ul>
        <li><strong>Raspberry Pi 3:</strong> Utilized Raspberry Pi 3 Model B+ with a 1.4GHz 64-bit quad-core processor, dual-band wireless LAN, Bluetooth 4.2/BLE, Gigabit Ethernet, extended GPIO header, HDMI, USB ports, camera and display interfaces, stereo output, composite video port, and microSD slot. Installation involved running a bash script via command line.</li>
        <li><strong>Webcam:</strong> Employed ELP HD 8 Megapixel USB CMOS board camera module with a Sony IMX179 sensor, compatible with Windows, Linux, Mac, and Android systems. It features high resolution, UVC support, and compatibility with various software and hardware.</li>
        <li><strong>Power Source:</strong> Used a Mi 10000 mAH Power Bank for powering the system.</li>
    </ul>

</body>

</html>
