import datetime
import os

import cv2
import pandas as pd


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TRAINING_IMAGE_DIR = os.path.join(BASE_DIR, "TrainingImage")
MODEL_PATH = os.path.join(TRAINING_IMAGE_DIR, "Trainner.yml")

STUDENT_DETAILS_DIR = os.path.join(BASE_DIR, "StudentDetails")
STUDENT_DETAILS_FILE = os.path.join(
    STUDENT_DETAILS_DIR,
    "StudentDetails.csv"
)

ATTENDANCE_DIR = os.path.join(BASE_DIR, "Attendance")

CASCADE_PATH = os.path.join(
    BASE_DIR,
    "haarcascade_frontalface_default.xml"
)


# ============================================================
# RECOGNIZE ATTENDANCE
# ============================================================

def recognize_attendence():

    print("\n" + "=" * 60)
    print("FACE RECOGNITION ATTENDANCE")
    print("=" * 60)

    # --------------------------------------------------------
    # Check required files/directories
    # --------------------------------------------------------

    if not os.path.exists(MODEL_PATH):
        print("ERROR: Trained model not found.")
        print(f"Expected: {MODEL_PATH}")
        return

    if not os.path.exists(STUDENT_DETAILS_FILE):
        print("ERROR: Student details file not found.")
        print(f"Expected: {STUDENT_DETAILS_FILE}")
        return

    if not os.path.exists(CASCADE_PATH):
        print("ERROR: Haar Cascade file not found.")
        print(f"Expected: {CASCADE_PATH}")
        return

    os.makedirs(ATTENDANCE_DIR, exist_ok=True)

    # --------------------------------------------------------
    # Load trained LBPH model
    # --------------------------------------------------------

    print("\nLoading trained model...")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(MODEL_PATH)

    print("Model loaded successfully.")

    # --------------------------------------------------------
    # Load Haar Cascade
    # --------------------------------------------------------

    faceCascade = cv2.CascadeClassifier(CASCADE_PATH)

    if faceCascade.empty():
        print("ERROR: Could not load Haar Cascade.")
        return

    # --------------------------------------------------------
    # Load student details
    # --------------------------------------------------------

    try:
        df = pd.read_csv(STUDENT_DETAILS_FILE)
    except Exception as e:
        print(f"ERROR: Could not read student details: {e}")
        return

    # Make sure required columns exist
    required_columns = ["Id", "Name"]

    for column in required_columns:
        if column not in df.columns:
            print(f"ERROR: Missing column '{column}' in StudentDetails.csv")
            return

    # Convert IDs to numeric values where possible
    df["Id"] = pd.to_numeric(df["Id"], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=["Id"])

    # Convert IDs to integers
    df["Id"] = df["Id"].astype(int)

    # --------------------------------------------------------
    # Attendance DataFrame
    # --------------------------------------------------------

    col_names = ["Id", "Name", "Date", "Time"]

    attendance = pd.DataFrame(columns=col_names)

    # --------------------------------------------------------
    # Start camera
    # --------------------------------------------------------

    print("\nOpening camera...")

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cam.isOpened():

        # Fallback for systems where CAP_DSHOW doesn't work
        cam.release()
        cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("ERROR: Could not open camera.")
        return

    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("Camera opened successfully.")
    print("Press Q to stop attendance.\n")

    # --------------------------------------------------------
    # Face detection parameters
    # --------------------------------------------------------

    font = cv2.FONT_HERSHEY_SIMPLEX

    minW = 0.1 * cam.get(cv2.CAP_PROP_FRAME_WIDTH)
    minH = 0.1 * cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # --------------------------------------------------------
    # Recognition loop
    # --------------------------------------------------------

    try:

        while True:

            ret, im = cam.read()

            if not ret:
                print("ERROR: Could not read frame from camera.")
                break

            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:

                # Draw face rectangle
                cv2.rectangle(
                    im,
                    (x, y),
                    (x + w, y + h),
                    (10, 159, 255),
                    2
                )

                # ------------------------------------------------
                # Predict identity
                # ------------------------------------------------

                Id, conf = recognizer.predict(
                    gray[y:y + h, x:x + w]
                )

                # ------------------------------------------------
                # LBPH confidence handling
                #
                # IMPORTANT:
                # Lower 'conf' means a better LBPH match.
                # ------------------------------------------------

                confidence_percentage = max(
                    0,
                    min(
                        100,
                        round(100 - conf)
                    )
                )

                # ------------------------------------------------
                # Recognized student
                # ------------------------------------------------

                if conf < 100:

                    student_rows = df.loc[
                        df["Id"] == int(Id)
                    ]

                    if not student_rows.empty:

                        # IMPORTANT:
                        # Extract actual value instead of converting
                        # the entire Pandas Series/array to string.
                        student_name = str(
                            student_rows.iloc[0]["Name"]
                        ).strip()

                        display_text = (
                            f"{int(Id)} - {student_name}"
                        )

                    else:

                        # Model recognized an ID that does not
                        # exist in StudentDetails.csv
                        student_name = "Unknown"
                        display_text = "Unknown"

                else:

                    student_name = "Unknown"
                    display_text = "Unknown"

                # ------------------------------------------------
                # Attendance threshold
                #
                # Existing application behavior:
                # confidence > 67% => attendance
                # ------------------------------------------------

                is_valid_match = (
                    student_name != "Unknown"
                    and confidence_percentage > 67
                )

                if is_valid_match:

                    current_time = datetime.datetime.now()

                    date = current_time.strftime("%Y-%m-%d")
                    time_stamp = current_time.strftime("%H:%M:%S")

                    student_id = int(Id)

                    # ------------------------------------------------
                    # Add attendance only once per student
                    # ------------------------------------------------

                    already_marked = (
                        attendance["Id"].astype(str)
                        == str(student_id)
                    ).any()

                    if not already_marked:

                        attendance.loc[len(attendance)] = [
                            student_id,
                            student_name,
                            date,
                            time_stamp
                        ]

                        print(
                            f"Attendance marked: "
                            f"{student_id} - {student_name}"
                        )

                # ------------------------------------------------
                # Display text
                # ------------------------------------------------

                if is_valid_match:

                    display_text = (
                        f"{int(Id)} - {student_name} [Pass]"
                    )

                    text_color = (255, 255, 255)

                else:

                    display_text = "Unknown"

                    text_color = (255, 255, 255)

                # ------------------------------------------------
                # Display recognition result
                # ------------------------------------------------

                cv2.putText(
                    im,
                    display_text,
                    (x + 5, y - 5),
                    font,
                    0.8,
                    text_color,
                    2
                )

                # ------------------------------------------------
                # Display confidence
                # ------------------------------------------------

                confstr = f"{confidence_percentage}%"

                if confidence_percentage > 67:

                    confidence_color = (0, 255, 0)

                elif confidence_percentage > 50:

                    confidence_color = (0, 255, 255)

                else:

                    confidence_color = (0, 0, 255)

                cv2.putText(
                    im,
                    confstr,
                    (x + 5, y + h - 5),
                    font,
                    0.8,
                    confidence_color,
                    1
                )

            # ----------------------------------------------------
            # Show camera window
            # ----------------------------------------------------

            cv2.imshow("Attendance", im)

            # Press Q to quit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:

        cam.release()
        cv2.destroyAllWindows()

    # ============================================================
    # SAVE ATTENDANCE
    # ============================================================

    if attendance.empty:

        print("\nNo attendance was recorded.")

        return

    # Remove duplicate students
    attendance = attendance.drop_duplicates(
        subset=["Id"],
        keep="first"
    )

    # ------------------------------------------------------------
    # Generate filename
    # ------------------------------------------------------------

    current_time = datetime.datetime.now()

    date = current_time.strftime("%Y-%m-%d")
    time_stamp = current_time.strftime("%H-%M-%S")

    file_name = (
        f"Attendance_{date}_{time_stamp}.xlsx"
    )

    file_path = os.path.join(
        ATTENDANCE_DIR,
        file_name
    )

    # ------------------------------------------------------------
    # Save REAL Excel file
    # ------------------------------------------------------------

    try:

        attendance.to_excel(
            file_path,
            index=False,
            engine="openpyxl"
        )

        print("\n" + "=" * 60)
        print("ATTENDANCE SUCCESSFUL")
        print("=" * 60)

        print(f"\nStudents marked: {len(attendance)}")
        print(f"Attendance file:")
        print(file_path)

        print("\nAttendance Data:")
        print(attendance.to_string(index=False))

    except Exception as e:

        print("\nERROR: Could not save attendance file.")
        print(str(e))






# import datetime
# import os
# import time
# import cv2
# # import keyboard
# import pandas as pd


# # -------------------------
# def recognize_attendence():
#     recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
#     recognizer.read("./TrainingImage/Trainner.yml")
#     harcascadePath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(harcascadePath)
#     df = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     col_names = ['Id', 'Name', 'Date', 'Time']
#     attendance = pd.DataFrame(columns=col_names)

#     # Initialize and start realtime video capture
#     cam = cv2.VideoCapture(0)
#     cam.set(3, 640)  # set video width
#     cam.set(4, 480)  # set video height
#     # Define min window size to be recognized as a face
#     minW = 0.1 * cam.get(3)
#     minH = 0.1 * cam.get(4)

#     while True:
#         _, im = cam.read()
#         gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#         faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)),
#                                              flags=cv2.CASCADE_SCALE_IMAGE)
#         for (x, y, w, h) in faces:
#             cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)
#             Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

#             if conf < 100:

#                 aa = df.loc[df['Id'] == Id]['Name'].values
#                 confstr = "  {0}%".format(round(100 - conf))
#                 tt = str(Id) + "-" + aa


#             else:
#                 Id = '  Unknown  '
#                 tt = str(Id)
#                 confstr = "  {0}%".format(round(100 - conf))

#             if (100 - conf) > 67:
#                 ts = time.time()
#                 date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#                 timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#                 aa = str(aa)[2:-2]
#                 attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

#             tt = str(tt)[2:-2]
#             if (100 - conf) > 67:
#                 tt = tt + " [Pass]"
#                 cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
#             else:
#                 cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

#             if (100 - conf) > 67:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 0), 1)
#             elif (100 - conf) > 50:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
#             else:
#                 cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)

#         attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
#         cv2.imshow('Attendance', im)
#         if (cv2.waitKey(1) == ord('q')):
#             break
#     ts = time.time()
#     date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#     timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#     Hour, Minute, Second = timeStamp.split(":")
#     fileName = "Attendance" + os.sep + "Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".xlsx"
#     attendance.to_csv(fileName, index=False)
#     print("Attendance Successful")
#     cam.release()
#     cv2.destroyAllWindows()
