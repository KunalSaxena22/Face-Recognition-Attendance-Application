import os
import cv2
import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import messagebox


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TRAINING_IMAGE_DIR = os.path.join(
    BASE_DIR,
    "TrainingImage"
)

MODEL_PATH = os.path.join(
    TRAINING_IMAGE_DIR,
    "Trainner.yml"
)


# ============================================================
# CREATE REQUIRED DIRECTORY
# ============================================================

os.makedirs(
    TRAINING_IMAGE_DIR,
    exist_ok=True
)


# ============================================================
# GET IMAGES AND LABELS
# ============================================================

def getImagesAndLabels(path):
    """
    Load all captured face images and extract
    the student ID from each filename.

    Expected filename format:

        Name.ID.SampleNumber.jpg

    Example:

        Kunal.101.1.jpg
        Kunal.101.2.jpg
        Kunal.101.3.jpg

    The ID extracted from the above files is:

        101
    """

    # --------------------------------------------------------
    # Check directory
    # --------------------------------------------------------

    if not os.path.exists(path):

        raise FileNotFoundError(
            f"Training image directory was not found:\n\n{path}"
        )


    # --------------------------------------------------------
    # Get only image files
    # --------------------------------------------------------

    valid_extensions = (
        ".jpg",
        ".jpeg",
        ".png"
    )

    imagePaths = [
        os.path.join(path, filename)
        for filename in os.listdir(path)
        if filename.lower().endswith(valid_extensions)
    ]


    # --------------------------------------------------------
    # Check whether images exist
    # --------------------------------------------------------

    if not imagePaths:

        raise ValueError(
            "No training images were found.\n\n"
            "Please capture student face images first."
        )


    # --------------------------------------------------------
    # Create empty lists
    # --------------------------------------------------------

    faces = []
    Ids = []


    # --------------------------------------------------------
    # Process every image
    # --------------------------------------------------------

    for imagePath in imagePaths:

        filename = os.path.basename(
            imagePath
        )

        try:

            # ------------------------------------------------
            # Expected:
            #
            # Name.ID.SampleNumber.jpg
            #
            # Example:
            #
            # Kunal.101.25.jpg
            # ------------------------------------------------

            parts = filename.split(".")


            # A valid filename should contain at least:
            #
            # Name
            # ID
            # Sample
            # jpg

            if len(parts) < 4:

                print(
                    f"Skipping invalid filename: {filename}"
                )

                continue


            # ------------------------------------------------
            # Extract Student ID
            # ------------------------------------------------

            student_id = parts[1]


            if not student_id.isdigit():

                print(
                    f"Skipping image with invalid ID: "
                    f"{filename}"
                )

                continue


            Id = int(student_id)


            # ------------------------------------------------
            # Load image
            # ------------------------------------------------

            pilImage = Image.open(
                imagePath
            ).convert("L")


            # ------------------------------------------------
            # Convert image to NumPy array
            # ------------------------------------------------

            imageNp = np.array(
                pilImage,
                "uint8"
            )


            # ------------------------------------------------
            # Add image and ID
            # ------------------------------------------------

            faces.append(
                imageNp
            )

            Ids.append(
                Id
            )


        except Exception as e:

            print(
                f"Skipping image '{filename}': {e}"
            )


    # --------------------------------------------------------
    # Check whether valid images were loaded
    # --------------------------------------------------------

    if not faces:

        raise ValueError(
            "No valid training images could be loaded.\n\n"
            "Please check the images inside the "
            "TrainingImage folder."
        )


    return faces, Ids


# ============================================================
# TRAIN IMAGES
# ============================================================

def TrainImages():
    """
    Train the LBPH face recognition model
    using captured student images.
    """

    try:

        # ----------------------------------------------------
        # Display training information
        # ----------------------------------------------------

        print()
        print("=" * 60)
        print("FACE RECOGNITION TRAINING")
        print("=" * 60)
        print()


        # ----------------------------------------------------
        # Load images and IDs
        # ----------------------------------------------------

        print(
            "Loading training images..."
        )

        faces, Ids = getImagesAndLabels(
            TRAINING_IMAGE_DIR
        )


        # ----------------------------------------------------
        # Training statistics
        # ----------------------------------------------------

        total_images = len(faces)

        unique_ids = len(
            set(Ids)
        )


        print(
            f"Images found : {total_images}"
        )

        print(
            f"Students found : {unique_ids}"
        )

        print()


        # ----------------------------------------------------
        # Create LBPH recognizer
        # ----------------------------------------------------

        print(
            "Creating LBPH face recognizer..."
        )

        recognizer = (
            cv2.face.LBPHFaceRecognizer_create()
        )


        # ----------------------------------------------------
        # Train model
        # ----------------------------------------------------

        print(
            "Training model..."
        )

        recognizer.train(
            faces,
            np.array(Ids)
        )


        print(
            "Training completed successfully."
        )

        print()


        # ----------------------------------------------------
        # Save trained model
        # ----------------------------------------------------

        recognizer.save(
            MODEL_PATH
        )


        print(
            f"Model saved to:\n{MODEL_PATH}"
        )

        print()
        print("=" * 60)
        print("TRAINING COMPLETE")
        print("=" * 60)
        print()


        # ----------------------------------------------------
        # Success message
        # ----------------------------------------------------

        messagebox.showinfo(
            "Training Complete",
            f"Face recognition training completed "
            f"successfully!\n\n"
            f"Images trained: {total_images}\n"
            f"Students trained: {unique_ids}\n\n"
            f"Model saved as:\n"
            f"{MODEL_PATH}"
        )


    # --------------------------------------------------------
    # No training images
    # --------------------------------------------------------

    except FileNotFoundError as e:

        messagebox.showerror(
            "Training Error",
            str(e)
        )


    # --------------------------------------------------------
    # Invalid/empty images
    # --------------------------------------------------------

    except ValueError as e:

        messagebox.showerror(
            "Training Error",
            str(e)
        )


    # --------------------------------------------------------
    # OpenCV error
    # --------------------------------------------------------

    except cv2.error as e:

        messagebox.showerror(
            "OpenCV Training Error",
            f"OpenCV encountered an error:\n\n{e}"
        )


    # --------------------------------------------------------
    # Any other error
    # --------------------------------------------------------

    except Exception as e:

        messagebox.showerror(
            "Training Error",
            f"An unexpected error occurred:\n\n{e}"
        )


# ============================================================
# GUI
# ============================================================

root = tk.Tk()

root.withdraw()


# ============================================================
# TRAINING GUI
# ============================================================

def traingui():
    """
    Ask the user for confirmation before training.
    """

    answer = messagebox.askyesno(
        "Train Images",
        "Do you want to train the captured face images?"
    )


    if answer:

        TrainImages()

    else:

        messagebox.showinfo(
            "Training Cancelled",
            "No images were trained."
        )





# import os
# import time
# import cv2
# import numpy as np
# from PIL import Image
# from threading import Thread
# import tkinter as tk
# from tkinter import messagebox


# # -------------- image label ------------------------

# def getImagesAndLabels(path):
#     # get the path of all the files in the folder
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     # print(imagePaths)

#     # create empty face list
#     faces = []
#     # create empty ID list
#     Ids = []
#     # now looping through all the image paths and loading the Ids and the images
#     for imagePath in imagePaths:
#         # loading the image and converting it to gray scale
#         pilImage = Image.open(imagePath).convert('L')
#         # Now we are converting the PIL image into numpy array
#         imageNp = np.array(pilImage, 'uint8')
#         # getting the Id from the image
#         Id = int(os.path.split(imagePath)[-1].split(".")[1])
#         # extract the face from the training image sample
#         faces.append(imageNp)
#         Ids.append(Id)
#     return faces, Ids


# # ----------- train images function ---------------
# def TrainImages():
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     detector = cv2.CascadeClassifier(harcascadePath)
#     faces, Id = getImagesAndLabels("TrainingImage")
#     Thread(target=recognizer.train(faces, np.array(Id))).start()
#     # Below line is optional for a visual counter effect
#     Thread(target=counter_img("TrainingImage")).start()
#     recognizer.save("TrainingImage" + os.sep + "Trainner.yml")
#     messagebox.showinfo("Training Complete", "All images have been trained.")


# # Optional, adds a counter for images trained (You can remove it)
# def counter_img(path):
#     imgcounter = 1
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     for imagePath in imagePaths:
#         print(str(imgcounter) + "Images Trained", end="\r")
#         time.sleep(0.008)
#         imgcounter += 1


# # Create a GUI window
# root = tk.Tk()
# root.withdraw()  # Hide the window


# # Ask the user if they want to train the images
# def traingui():
#     if messagebox.askyesno("Train Images", "Do you want to train the images?"):
#         TrainImages()
#     else:
#         messagebox.showinfo("Training Cancelled", "No images were trained.")



# import os
# import time
# import cv2
# import numpy as np
# from PIL import Image
# from threading import Thread
#
#
# # -------------- image label ------------------------
#
# def getImagesAndLabels(path):
#     # get the path of all the files in the folder
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     # print(imagePaths)
#
#     # create empth face list
#     faces = []
#     # create empty ID list
#     Ids = []
#     # now looping through all the image paths and loading the Ids and the images
#     for imagePath in imagePaths:
#         # loading the image and converting it to gray scale
#         pilImage = Image.open(imagePath).convert('L')
#         # Now we are converting the PIL image into numpy array
#         imageNp = np.array(pilImage, 'uint8')
#         # getting the Id from the image
#         Id = int(os.path.split(imagePath)[-1].split(".")[1])
#         # extract the face from the training image sample
#         faces.append(imageNp)
#         Ids.append(Id)
#     return faces, Ids
#
#
# # ----------- train images function ---------------
# def TrainImages():
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     detector = cv2.CascadeClassifier(harcascadePath)
#     faces, Id = getImagesAndLabels("TrainingImage")
#     Thread(target=recognizer.train(faces, np.array(Id))).start()
#     # Below line is optional for a visual counter effect
#     Thread(target=counter_img("TrainingImage")).start()
#     recognizer.save("TrainingImage" + os.sep + "Trainner.yml")
#     print("All Images")
#
#
# # Optional, adds a counter for images trained (You can remove it)
# def counter_img(path):
#     imgcounter = 1
#     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
#     for imagePath in imagePaths:
#         print(str(imgcounter) + "Images Trained", end="\r")
#         time.sleep(0.008)
#         imgcounter += 1
