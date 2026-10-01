import os
import cv2
import tkinter.messagebox as messagebox


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CASCADE_PATH = os.path.join(
    BASE_DIR,
    "haarcascade_frontalface_default.xml"
)

CAMERA_WINDOW = "Webcam Check"


# ============================================================
# CAMERA CHECK
# ============================================================

def camer():

    print("\n" + "=" * 50)
    print("CAMERA CHECK")
    print("=" * 50)

    # --------------------------------------------------------
    # Check Haar Cascade
    # --------------------------------------------------------

    if not os.path.isfile(CASCADE_PATH):

        messagebox.showerror(
            "Missing File",
            f"Haar Cascade file was not found:\n\n"
            f"{CASCADE_PATH}"
        )

        return

    # --------------------------------------------------------
    # Load Haar Cascade
    # --------------------------------------------------------

    face_cascade = cv2.CascadeClassifier(
        CASCADE_PATH
    )

    if face_cascade.empty():

        messagebox.showerror(
            "Cascade Error",
            "Unable to load Haar Cascade classifier."
        )

        return

    # --------------------------------------------------------
    # Open Camera
    # --------------------------------------------------------

    print("Opening camera...")

    # Windows DirectShow
    cap = cv2.VideoCapture(
        0,
        cv2.CAP_DSHOW
    )

    # Fallback
    if not cap.isOpened():

        print("DirectShow failed.")
        print("Trying default camera backend...")

        cap.release()

        cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        messagebox.showerror(
            "Camera Error",
            "Unable to access the camera.\n\n"
            "Please make sure:\n"
            "• Camera is connected.\n"
            "• No other application is using it.\n"
            "• Camera permission is enabled."
        )

        return

    # --------------------------------------------------------
    # Camera Resolution
    # --------------------------------------------------------

    cap.set(
        cv2.CAP_PROP_FRAME_WIDTH,
        640
    )

    cap.set(
        cv2.CAP_PROP_FRAME_HEIGHT,
        480
    )

    print("Camera opened successfully.")
    print("Click X to close the camera.")

    try:

        while True:

            ret, img = cap.read()

            if not ret or img is None:

                print("Unable to read camera frame.")

                break

            # ------------------------------------------------
            # Convert to grayscale
            # ------------------------------------------------

            gray = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )

            # ------------------------------------------------
            # Detect faces
            # ------------------------------------------------

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(30, 30)
            )

            # ------------------------------------------------
            # Draw face rectangles
            # ------------------------------------------------

            for (x, y, w, h) in faces:

                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (10, 159, 255),
                    2
                )

            # ------------------------------------------------
            # Display
            # ------------------------------------------------

            cv2.imshow(
                CAMERA_WINDOW,
                img
            )

            # IMPORTANT:
            # Process Windows/OpenCV events first.
            cv2.waitKey(1)

            # ------------------------------------------------
            # Detect X button
            # ------------------------------------------------

            try:

                if cv2.getWindowProperty(
                    CAMERA_WINDOW,
                    cv2.WND_PROP_VISIBLE
                ) < 1:

                    break

            except cv2.error:

                break

    finally:

        # ----------------------------------------------------
        # Release camera
        # ----------------------------------------------------

        cap.release()

        cv2.destroyAllWindows()

        print("Camera released.")
        print("Camera check completed.")


# ============================================================
# DIRECT RUN
# ============================================================

if __name__ == "__main__":
    camer()



# import os
# import cv2
# import tkinter.messagebox as messagebox


# # ============================================================
# # PROJECT PATH
# # ============================================================

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CASCADE_PATH = os.path.join(
#     BASE_DIR,
#     "haarcascade_frontalface_default.xml"
# )


# # ============================================================
# # CAMERA CHECK
# # ============================================================

# def camer():

#     print("\n" + "=" * 50)
#     print("CAMERA CHECK")
#     print("=" * 50)

#     # --------------------------------------------------------
#     # Check Haar Cascade
#     # --------------------------------------------------------

#     if not os.path.isfile(CASCADE_PATH):
#         messagebox.showerror(
#             "Missing File",
#             f"Haar Cascade file was not found:\n\n{CASCADE_PATH}"
#         )
#         return

#     # --------------------------------------------------------
#     # Load Haar Cascade
#     # --------------------------------------------------------

#     face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

#     if face_cascade.empty():
#         messagebox.showerror(
#             "Cascade Error",
#             "Unable to load Haar Cascade classifier."
#         )
#         return

#     # --------------------------------------------------------
#     # Open Camera
#     # --------------------------------------------------------

#     print("Opening camera...")

#     # Use Windows DirectShow backend
#     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#     # Fallback if DirectShow fails
#     if not cap.isOpened():

#         print("DirectShow failed.")
#         print("Trying default camera backend...")

#         cap.release()
#         cap = cv2.VideoCapture(0)

#     if not cap.isOpened():

#         messagebox.showerror(
#             "Camera Error",
#             "Unable to access the camera.\n\n"
#             "Please make sure:\n"
#             "• Camera is connected.\n"
#             "• No other application is using it.\n"
#             "• Camera permission is enabled."
#         )

#         return

#     # --------------------------------------------------------
#     # Camera Resolution
#     # --------------------------------------------------------

#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#     print("Camera opened successfully.")

#     try:

#         while True:

#             ret, img = cap.read()

#             if not ret or img is None:
#                 print("Unable to read camera frame.")
#                 break

#             # ------------------------------------------------
#             # Convert to grayscale
#             # ------------------------------------------------

#             gray = cv2.cvtColor(
#                 img,
#                 cv2.COLOR_BGR2GRAY
#             )

#             # ------------------------------------------------
#             # Detect faces
#             # ------------------------------------------------

#             faces = face_cascade.detectMultiScale(
#                 gray,
#                 scaleFactor=1.3,
#                 minNeighbors=5,
#                 minSize=(30, 30)
#             )

#             # ------------------------------------------------
#             # Draw rectangles
#             # ------------------------------------------------

#             for (x, y, w, h) in faces:

#                 cv2.rectangle(
#                     img,
#                     (x, y),
#                     (x + w, y + h),
#                     (10, 159, 255),
#                     2
#                 )

#             # ------------------------------------------------
#             # Display
#             # ------------------------------------------------

#             cv2.imshow(
#                 "Webcam Check - Press Q to Close",
#                 img
#             )

#             # ------------------------------------------------
#             # Quit
#             # ------------------------------------------------

#             if cv2.waitKey(1) & 0xFF == ord("q"):
#                 break

#     finally:

#         cap.release()
#         cv2.destroyAllWindows()

#         print("Camera released.")
#         print("Camera check completed.")


# if __name__ == "__main__":
#     camer()





# def camer():
#     import cv2

#     # Load the cascade
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#     # To capture video from webcam.
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Read the frame
#         _, img = cap.read()

#         # Convert to grayscale
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # Detect the faces
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

#         # Draw the rectangle around each face
#         for (x, y, w, h) in faces:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (10,159,255), 2)


#         # Display
#         cv2.imshow('Webcam Check', img)

#         # Stop if escape key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the VideoCapture object
#     cap.release()
#     cv2.destroyAllWindows()
