import tkinter as tk
import cv2
import os.path
import csv
import tkinter.messagebox as messagebox
import os


# function to take images
def take_image(self):
    Id = self.id_entry.get()
    name = self.name_entry.get()
    rollno = self.rollno_entry.get()
    email = self.email_entry.get()

    # check if ID is a number
    try:
        float(Id)
    except ValueError:
        tk.messagebox.showerror("Error", "Id must be a number")
        return

    try:
        import unicodedata
        unicodedata.numeric(Id)
    except (TypeError, ValueError):
        pass
    else:
        tk.messagebox.showerror("Error", "Id must be a number")
        return

    # check if name contains only alphabets
    try:
        if not name.isalpha():
            raise ValueError("Name must contain only alphabets")
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))
        return

    # check if roll no. contains only numbers and alphabets
    try:
        if not rollno.isalnum():
            raise ValueError("Roll no. must contain only numbers and alphabets")
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))
        return

    # check if email address is valid
    try:
        if not "@" in email or not "." in email:
            raise ValueError("Invalid email address")
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))
        return

    # Clear the contents of the text fields
    self.id_entry.delete(0, 'end')
    self.name_entry.delete(0, 'end')
    self.rollno_entry.delete(0, 'end')
    self.email_entry.delete(0, 'end')

    # start capturing images
    try:
        cam = cv2.VideoCapture(0)
    except Exception as e:
        tk.messagebox.showerror("Error", str(e))
        return

    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0

    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder TrainingImage
            cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' +
                        str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            # display the frame
            cv2.imshow('frame', img)
        # wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is more than 100
        elif sampleNum > 100:
            break
    cam.release()
    cv2.destroyAllWindows()
    res = "Images Saved for ID : " + Id + " Name : " + name + "Roll no.: " + rollno + "Email Id: " + email
    header = ["Id", "Name", "Roll no.", "Email Id"]
    row = [Id, name, rollno, email]
    if (os.path.isfile("StudentDetails" + os.sep + "StudentDetails.csv")):
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(j for j in row)
        csvFile.close()
    else:
        with open("StudentDetails" + os.sep + "StudentDetails.csv", 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(i for i in header)
            writer.writerow(j for j in row)
        csvFile.close()


















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
