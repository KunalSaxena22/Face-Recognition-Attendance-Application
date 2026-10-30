# AttendVision — AttendX Face Recognition Attendance System

AttendVision (the desktop application is titled **AttendX – Next-Gen Attendance System**) is a Python desktop project for student registration, webcam face-sample capture, LBPH model training, attendance recording, dashboard summaries, and attendance email notifications.

It is built for learning and demonstration with Python, Tkinter, OpenCV, and local CSV, JSON, and Excel files.

> **Project status:** This is a learning/demo application, not a production-ready biometric or student-information system. Read the security and privacy notes before using real student data.

## Features

- **Administrator registration and login** through the desktop interface.
- **Student registration** with student ID, name, roll number, and email address, including duplicate-ID checks.
- **Face sample capture** using a webcam and Haar Cascade face detection.
- **Model training** using OpenCV Local Binary Patterns Histograms (LBPH). The model is saved in the TrainingImage folder as Trainner.yml.
- **Attendance recognition** using the trained LBPH model, recording a recognized student once per session.
- **Excel attendance reports** with student ID, name, date, and time.
- **Dashboard** showing student totals, present/absent counts, attendance percentage, and recent records.
- **Camera check** for webcam access and face detection.
- **Email notifications** for present/absent status using Gmail SMTP.

## Technology

| Area | Technology |
|---|---|
| Language and desktop UI | Python, Tkinter |
| Face detection | OpenCV Haar Cascade |
| Face recognition | OpenCV LBPH (cv2.face) |
| Image processing | OpenCV, NumPy, Pillow |
| Student records | CSV |
| Administrator data | JSON |
| Attendance reports | Pandas, Excel (.xlsx), OpenPyXL |
| Email | smtplib, Gmail SMTP over SSL |

## How it works

1. Start the application and create an administrator account.
2. Sign in and register students.
3. Capture face samples for each student using the webcam.
4. Train the LBPH recognition model from the captured samples.
5. Start an attendance session. The application detects faces, predicts a student ID, and records each recognized student once in that session.
6. Press **Q** to close the attendance camera. When attendance was recorded, an Excel report is saved in the Attendance folder.
7. Review the dashboard and use email notifications only with appropriate test data until the privacy issue described below is addressed.

The recognition decision uses a threshold derived from the LBPH prediction distance. The displayed percentage is an application-specific score; it is **not** a scientifically measured recognition-accuracy rate.

## Requirements

- Windows desktop environment.
- Python 3.10 is the compatibility baseline reflected by the CPython 3.10 binary files currently included in this repository. Other Python versions have not been verified.
- Webcam for face capture, camera checking, and attendance recognition.
- Python dependencies are pinned in `requirements.txt`.
- Tkinter, normally included with the standard Windows Python distribution.

The OpenCV contrib distribution is required for the `cv2.face` LBPH recognizer. Install only `opencv-contrib-python`; do not install `opencv-python` alongside it because both distributions provide the `cv2` package.

## Setup and run

Clone the repository:

~~~powershell
git clone https://github.com/KunalSaxena22/Face-Recognition-Attendance-Application.git
cd Face-Recognition-Attendance-Application
~~~

Create a Python 3.10 virtual environment and install the pinned dependency set. These commands call the virtual environment's Python executable directly, so activation is not required:

~~~powershell
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
~~~

Start the application from the repository root:

~~~powershell
.\.venv\Scripts\python.exe main.py
~~~

On the login screen, choose **Create New Account** to register the first administrator, then sign in.

## Data and generated files

The application creates or uses these paths relative to the project directory:

| Path | Purpose |
|---|---|
| StudentDetails/NewRegisterInfo.json | Administrator account data |
| StudentDetails/StudentDetails.csv | Registered student details |
| TrainingImage/ | Captured face samples |
| TrainingImage/Trainner.yml | Trained LBPH model |
| Attendance/ | Generated attendance Excel reports |
| haarcascade_frontalface_default.xml | Haar Cascade face detector |

Do not commit real student data, captured face images, trained models derived from real people, credentials, or attendance reports to a public repository.

## Email and privacy warning

The email feature connects to Gmail using SMTP over SSL on port 465. It asks for a sender email address and password/App Password at runtime. Never commit credentials to Git or place them in source code.

**Important:** The current email implementation attaches the selected attendance Excel workbook to each student's email. The workbook may contain records for multiple students. Do not use this feature with real student records until the attachment behavior is changed or reviewed to prevent disclosure.

## Security, privacy, and limitations

- **Plain-text administrator passwords:** passwords are currently stored and checked in StudentDetails/NewRegisterInfo.json as plain text. This is not suitable for accounts protecting real or sensitive information.
- **Biometric and student information:** face images, student details, model files, and attendance reports can be sensitive personal data. Obtain appropriate consent and institutional approval, restrict access, and define retention and deletion practices before real-world use.
- **Recognition limitations:** lighting, camera quality, pose, image quality, and training samples can affect recognition. The displayed score is not a guarantee of identity or a measured accuracy metric. Attendance should have a manual review/correction process.
- **Demo status:** the local JSON/CSV/Excel storage and current authentication design have not been presented as a secure institutional deployment.

## License

The original AttendVision application source code authored by the project maintainer is licensed under the [MIT License](LICENSE).

This license does not replace or relicense third-party dependencies, bundled Python packages, external libraries, or assets whose rights belong to other authors. Those components remain subject to their own copyright notices and license terms. Check the applicable license before redistributing any third-party component or asset.

## Contributing

Bug reports, reproducible issue descriptions, documentation improvements, and tested pull requests are welcome. Do not include real student information, face images, credentials, or attendance exports in issues or pull requests. Describe the problem, the change, and the steps used to test it.

## Maintainer

**Kunal Saxena**  
GitHub: [@KunalSaxena22](https://github.com/KunalSaxena22)
