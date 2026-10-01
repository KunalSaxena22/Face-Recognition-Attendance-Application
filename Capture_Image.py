import tkinter as tk
import tkinter.messagebox as messagebox
import cv2
import os
import csv


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TRAINING_IMAGE_DIR = os.path.join(
    BASE_DIR,
    "TrainingImage"
)

STUDENT_DETAILS_DIR = os.path.join(
    BASE_DIR,
    "StudentDetails"
)

STUDENT_DETAILS_FILE = os.path.join(
    STUDENT_DETAILS_DIR,
    "StudentDetails.csv"
)

CASCADE_PATH = os.path.join(
    BASE_DIR,
    "haarcascade_frontalface_default.xml"
)


# ============================================================
# CREATE REQUIRED DIRECTORIES
# ============================================================

os.makedirs(TRAINING_IMAGE_DIR, exist_ok=True)
os.makedirs(STUDENT_DETAILS_DIR, exist_ok=True)


# ============================================================
# VALIDATION FUNCTIONS
# ============================================================

def is_valid_id(student_id):
    """
    Check whether the student ID contains only numbers.
    """

    return student_id.isdigit()


def is_valid_name(name):
    """
    Check whether the name contains alphabets and spaces.
    """

    cleaned_name = name.replace(" ", "")

    return bool(cleaned_name) and cleaned_name.isalpha()


def is_valid_roll_number(roll_no):
    """
    Roll number can contain letters and numbers.
    """

    return bool(roll_no) and roll_no.isalnum()


def is_valid_email(email):
    """
    Basic email validation.
    """

    if not email:
        return False

    if "@" not in email:
        return False

    domain = email.split("@")[-1]

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


# ============================================================
# CHECK DUPLICATE STUDENT ID
# ============================================================

def student_id_exists(student_id):
    """
    Check whether the student ID already exists
    in StudentDetails.csv.
    """

    if not os.path.isfile(STUDENT_DETAILS_FILE):
        return False

    try:

        with open(
            STUDENT_DETAILS_FILE,
            "r",
            newline="",
            encoding="utf-8-sig"
        ) as csv_file:

            reader = csv.DictReader(csv_file)

            for row in reader:

                existing_id = str(
                    row.get("Id", "")
                ).strip()

                if existing_id == student_id:
                    return True

    except Exception as e:

        messagebox.showerror(
            "File Error",
            f"Unable to read student details:\n\n{e}"
        )

        return True

    return False


# ============================================================
# SAVE STUDENT DETAILS
# ============================================================

def save_student_details(student_id, name, roll_no, email):
    """
    Save student information into StudentDetails.csv.
    """

    file_exists = os.path.isfile(
        STUDENT_DETAILS_FILE
    )

    try:

        with open(
            STUDENT_DETAILS_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = csv.writer(csv_file)

            # Create header if file doesn't exist
            # or is empty.
            if not file_exists or os.path.getsize(
                STUDENT_DETAILS_FILE
            ) == 0:

                writer.writerow(
                    [
                        "Id",
                        "Name",
                        "Roll no.",
                        "Email Id"
                    ]
                )

            writer.writerow(
                [
                    student_id,
                    name,
                    roll_no,
                    email
                ]
            )

        return True

    except Exception as e:

        messagebox.showerror(
            "File Error",
            f"Unable to save student details:\n\n{e}"
        )

        return False


# ============================================================
# DELETE CAPTURED IMAGES
# ============================================================

def delete_captured_images(student_id, name):
    """
    Delete images captured for the current student
    if the capture process fails or is cancelled.
    """

    try:

        prefix = f"{name}.{student_id}."

        for filename in os.listdir(
            TRAINING_IMAGE_DIR
        ):

            if filename.startswith(prefix):

                file_path = os.path.join(
                    TRAINING_IMAGE_DIR,
                    filename
                )

                try:
                    os.remove(file_path)

                except OSError:
                    pass

    except OSError:
        pass


# ============================================================
# TAKE IMAGES
# ============================================================

def take_image(self):

    # --------------------------------------------------------
    # Get information from GUI
    # --------------------------------------------------------

    student_id = self.id_entry.get().strip()
    name = self.name_entry.get().strip()
    roll_no = self.rollno_entry.get().strip()
    email = self.email_entry.get().strip()


    # --------------------------------------------------------
    # Validate Student ID
    # --------------------------------------------------------

    if not student_id:

        messagebox.showerror(
            "Invalid ID",
            "Please enter a Student ID."
        )

        return

    if not is_valid_id(student_id):

        messagebox.showerror(
            "Invalid ID",
            "Student ID must contain only numbers."
        )

        return


    # --------------------------------------------------------
    # Validate Name
    # --------------------------------------------------------

    if not name:

        messagebox.showerror(
            "Invalid Name",
            "Please enter the student's name."
        )

        return

    if not is_valid_name(name):

        messagebox.showerror(
            "Invalid Name",
            "Name must contain only alphabets and spaces."
        )

        return


    # --------------------------------------------------------
    # Validate Roll Number
    # --------------------------------------------------------

    if not roll_no:

        messagebox.showerror(
            "Invalid Roll Number",
            "Please enter the roll number."
        )

        return

    if not is_valid_roll_number(roll_no):

        messagebox.showerror(
            "Invalid Roll Number",
            "Roll number can contain only letters and numbers."
        )

        return


    # --------------------------------------------------------
    # Validate Email
    # --------------------------------------------------------

    if not email:

        messagebox.showerror(
            "Invalid Email",
            "Please enter the student's email address."
        )

        return

    if not is_valid_email(email):

        messagebox.showerror(
            "Invalid Email",
            "Please enter a valid email address."
        )

        return


    # --------------------------------------------------------
    # Check Duplicate ID
    # --------------------------------------------------------

    if student_id_exists(student_id):

        messagebox.showerror(
            "Duplicate ID",
            f"Student ID '{student_id}' already exists.\n\n"
            "Please use a different ID."
        )

        return


    # --------------------------------------------------------
    # Check Haar Cascade
    # --------------------------------------------------------

    if not os.path.isfile(CASCADE_PATH):

        messagebox.showerror(
            "Missing File",
            "Haar Cascade file was not found.\n\n"
            f"Expected location:\n{CASCADE_PATH}"
        )

        return


    # --------------------------------------------------------
    # Load Haar Cascade
    # --------------------------------------------------------

    detector = cv2.CascadeClassifier(
        CASCADE_PATH
    )

    if detector.empty():

        messagebox.showerror(
            "Cascade Error",
            "Unable to load the Haar Cascade classifier."
        )

        return


    # --------------------------------------------------------
    # Open Camera
    # --------------------------------------------------------

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # Fallback to default backend
    if not cam.isOpened():
        cam.release()
        cam = cv2.VideoCapture(0)

    if not cam.isOpened():

        messagebox.showerror(
            "Camera Error",
            "Unable to access the camera.\n\n"
            "Please make sure:\n"
            "• Your camera is connected.\n"
            "• No other application is using it.\n"
            "• Camera permission is enabled."
        )

        return


    # --------------------------------------------------------
    # Camera Configuration
    # --------------------------------------------------------

    cam.set(
        cv2.CAP_PROP_FRAME_WIDTH,
        640
    )

    cam.set(
        cv2.CAP_PROP_FRAME_HEIGHT,
        480
    )


    sample_num = 0

    capture_completed = False


    # --------------------------------------------------------
    # Capture Face Images
    # --------------------------------------------------------

    try:

        while True:

            ret, img = cam.read()

            # Camera failed to return frame
            if not ret or img is None:

                messagebox.showerror(
                    "Camera Error",
                    "Unable to read a frame from the camera."
                )

                break


            # Convert frame to grayscale
            gray = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )


            # Detect faces
            faces = detector.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )


            # Process detected faces
            for (x, y, w, h) in faces:

                # Draw rectangle around face
                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (10, 159, 255),
                    2
                )


                # Increase sample number
                sample_num += 1


                # Create image filename
                filename = (
                    f"{name}.{student_id}."
                    f"{sample_num}.jpg"
                )


                image_path = os.path.join(
                    TRAINING_IMAGE_DIR,
                    filename
                )


                # Save detected face
                success = cv2.imwrite(
                    image_path,
                    gray[
                        y:y + h,
                        x:x + w
                    ]
                )


                # If image wasn't saved,
                # don't count it.
                if not success:

                    sample_num -= 1

                    continue


                # Display counter
                cv2.putText(
                    img,
                    f"Images: {sample_num}/100",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )


                # Stop after exactly 100 images
                if sample_num >= 100:

                    capture_completed = True

                    break


            # Display camera window
            cv2.imshow(
                "Face Capture - Press Q to Stop",
                img
            )


            # Stop after 100 images
            if capture_completed:
                break


            # Allow user to manually stop
            key = cv2.waitKey(100) & 0xFF

            if key == ord("q"):

                break


    except Exception as e:

        messagebox.showerror(
            "Capture Error",
            f"An unexpected error occurred:\n\n{e}"
        )


    finally:

        # Release camera
        cam.release()

        # Close OpenCV windows
        cv2.destroyAllWindows()


    # ========================================================
    # CHECK CAPTURE RESULT
    # ========================================================

    if not capture_completed:

        # Delete partially captured images
        delete_captured_images(
            student_id,
            name
        )

        messagebox.showwarning(
            "Capture Cancelled",
            f"Face capture was not completed.\n\n"
            f"Images captured: {sample_num}/100\n\n"
            "Please try again and allow the camera "
            "to capture 100 images."
        )

        return


    # ========================================================
    # SAVE STUDENT INFORMATION
    # ========================================================

    saved = save_student_details(
        student_id,
        name,
        roll_no,
        email
    )


    if not saved:

        # Remove captured images if student
        # information could not be saved.
        delete_captured_images(
            student_id,
            name
        )

        return


    # ========================================================
    # CLEAR GUI FIELDS
    # ========================================================

    try:

        self.id_entry.delete(
            0,
            "end"
        )

        self.name_entry.delete(
            0,
            "end"
        )

        self.rollno_entry.delete(
            0,
            "end"
        )

        self.email_entry.delete(
            0,
            "end"
        )

    except Exception:
        pass


    # ========================================================
    # SUCCESS MESSAGE
    # ========================================================

    messagebox.showinfo(
        "Capture Complete",
        f"Face images captured successfully!\n\n"
        f"Student ID: {student_id}\n"
        f"Name: {name}\n"
        f"Roll No.: {roll_no}\n"
        f"Email: {email}\n\n"
        f"Images captured: {sample_num}\n\n"
        "The student details have been saved.\n"
        "You can now use 'Train Images' to train "
        "the face-recognition model."
    )




# import tkinter as tk
# import cv2
# import os.path
# import csv
# import tkinter.messagebox as messagebox
# import os


# # function to take images
# def take_image(self):
#     Id = self.id_entry.get()
#     name = self.name_entry.get()
#     rollno = self.rollno_entry.get()
#     email = self.email_entry.get()

#     # check if ID is a number
#     try:
#         float(Id)
#     except ValueError:
#         tk.messagebox.showerror("Error", "Id must be a number")
#         return

#     try:
#         import unicodedata
#         unicodedata.numeric(Id)
#     except (TypeError, ValueError):
#         pass
#     else:
#         tk.messagebox.showerror("Error", "Id must be a number")
#         return

#     # check if name contains only alphabets
#     try:
#         if not name.isalpha():
#             raise ValueError("Name must contain only alphabets")
#     except ValueError as e:
#         tk.messagebox.showerror("Error", str(e))
#         return

#     # check if roll no. contains only numbers and alphabets
#     try:
#         if not rollno.isalnum():
#             raise ValueError("Roll no. must contain only numbers and alphabets")
#     except ValueError as e:
#         tk.messagebox.showerror("Error", str(e))
#         return

#     # check if email address is valid
#     try:
#         if not "@" in email or not "." in email:
#             raise ValueError("Invalid email address")
#     except ValueError as e:
#         tk.messagebox.showerror("Error", str(e))
#         return

#     # Clear the contents of the text fields
#     self.id_entry.delete(0, 'end')
#     self.name_entry.delete(0, 'end')
#     self.rollno_entry.delete(0, 'end')
#     self.email_entry.delete(0, 'end')

#     # start capturing images
#     try:
#         cam = cv2.VideoCapture(0)
#     except Exception as e:
#         tk.messagebox.showerror("Error", str(e))
#         return

#     harcascadePath = "haarcascade_frontalface_default.xml"
#     detector = cv2.CascadeClassifier(harcascadePath)
#     sampleNum = 0

#     while (True):
#         ret, img = cam.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
#             # incrementing sample number
#             sampleNum = sampleNum + 1
#             # saving the captured face in the dataset folder TrainingImage
#             cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
#                         str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
#             # display the frame
#             cv2.imshow('frame', img)
#         # wait for 100 miliseconds
#         if cv2.waitKey(100) & 0xFF == ord('q'):
#             break
#         # break if the sample number is more than 100
#         elif sampleNum > 100:
#             break
#     cam.release()
#     cv2.destroyAllWindows()
#     res = "Images Saved for ID : " + Id + " Name : " + name + "Roll no.: " + rollno + "Email Id: " + email
#     header = ["Id", "Name", "Roll no.", "Email Id"]
#     row = [Id, name, rollno, email]
#     if (os.path.isfile("StudentDetails" + os.sep + "StudentDetails.csv")):
#         with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#             writer = csv.writer(csvFile)
#             writer.writerow(j for j in row)
#         csvFile.close()
#     else:
#         with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#             writer = csv.writer(csvFile)
#             writer.writerow(i for i in header)
#             writer.writerow(j for j in row)
#         csvFile.close()


















#
# import csv
# import cv2
# import os
# import os.path
#
#
# # counting the numbers
#
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False
#
#
# # Take image function
#
# def takeImages():
#     Id = input("Enter Your Id: ")
#     name = input("Enter Your Name: ")
#     rollno = input("Enter Your Roll No.: ")
#     email = input("Enter Your Valid Email Id: ")
#
#     if (is_number(Id) and name.isalpha() and rollno.isalnum()):
#         cam = cv2.VideoCapture(0)
#         harcascadePath = "haarcascade_frontalface_default.xml"
#         detector = cv2.CascadeClassifier(harcascadePath)
#         sampleNum = 0
#
#         while (True):
#             ret, img = cam.read()
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
#             for (x, y, w, h) in faces:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
#                 # incrementing sample number
#                 sampleNum = sampleNum + 1
#                 # saving the captured face in the dataset folder TrainingImage
#                 cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
#                             str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
#                 # display the frame
#                 cv2.imshow('frame', img)
#             # wait for 100 miliseconds
#             if cv2.waitKey(100) & 0xFF == ord('q'):
#                 break
#             # break if the sample number is more than 100
#             elif sampleNum > 100:
#                 break
#         cam.release()
#         cv2.destroyAllWindows()
#         res = "Images Saved for ID : " + Id + " Name : " + name + "Roll no.: " + rollno + "Email Id: " + email
#         header = ["Id", "Name", "Roll no.", "Email Id"]
#         row = [Id, name, rollno, email]
#         if (os.path.isfile("StudentDetails" + os.sep + "StudentDetails.csv")):
#             with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#                 writer = csv.writer(csvFile)
#                 writer.writerow(j for j in row)
#             csvFile.close()
#         else:
#             with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
#                 writer = csv.writer(csvFile)
#                 writer.writerow(i for i in header)
#                 writer.writerow(j for j in row)
#             csvFile.close()
#     else:
#         if (is_number(Id)):
#             print("Enter Alphabetical Name")
#         if (name.isalpha()):
#             print("Enter Numeric ID")
#         if (rollno.isalnum()):
#             print("Enter Only Number and Alphabet")
