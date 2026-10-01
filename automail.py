import os
import smtplib
import pandas as pd

from email.message import EmailMessage
from tkinter import filedialog, messagebox


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STUDENT_DETAILS_FILE = os.path.join(
    BASE_DIR,
    "StudentDetails",
    "StudentDetails.csv"
)


# ============================================================
# BROWSE ATTENDANCE FILE
# ============================================================

def browse_file(self):

    file_path = filedialog.askopenfilename(
        title="Select Attendance File",
        filetypes=[
            ("Excel Files", "*.xlsx"),
            ("Excel Files", "*.xls")
        ]
    )

    if file_path:

        self.attechment_entry.delete(0, "end")
        self.attechment_entry.insert(0, file_path)


# ============================================================
# SEND EMAIL
# ============================================================

def send_email(self):

    sender_email = self.sender_email_entry.get().strip()
    sender_pass = self.sender_pass_entry.get().strip()
    attendance_file = self.attechment_entry.get().strip()

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    if not sender_email:
        messagebox.showerror(
            "Error",
            "Please enter sender email address."
        )
        return

    if not sender_pass:
        messagebox.showerror(
            "Error",
            "Please enter sender email password/app password."
        )
        return

    if not attendance_file:
        messagebox.showerror(
            "Error",
            "Please select an attendance Excel file."
        )
        return

    if not os.path.exists(attendance_file):
        messagebox.showerror(
            "Error",
            "Selected attendance file does not exist."
        )
        return

    if not os.path.exists(STUDENT_DETAILS_FILE):
        messagebox.showerror(
            "Error",
            "StudentDetails.csv was not found."
        )
        return

    try:

        # ====================================================
        # READ ATTENDANCE
        # ====================================================

        attendance_df = pd.read_excel(
            attendance_file
        )

        required_attendance_columns = [
            "Id",
            "Name",
            "Date",
            "Time"
        ]

        for column in required_attendance_columns:

            if column not in attendance_df.columns:

                raise ValueError(
                    f"Attendance file is missing column: {column}"
                )

        # ====================================================
        # READ STUDENT DETAILS
        # ====================================================

        students_df = pd.read_csv(
            STUDENT_DETAILS_FILE
        )

        required_student_columns = [
            "Id",
            "Name",
            "Email Id"
        ]

        for column in required_student_columns:

            if column not in students_df.columns:

                raise ValueError(
                    f"StudentDetails.csv is missing column: {column}"
                )

        # ====================================================
        # NORMALIZE IDs
        # ====================================================

        students_df["Id"] = pd.to_numeric(
            students_df["Id"],
            errors="coerce"
        )

        attendance_df["Id"] = pd.to_numeric(
            attendance_df["Id"],
            errors="coerce"
        )

        students_df = students_df.dropna(
            subset=["Id"]
        )

        attendance_df = attendance_df.dropna(
            subset=["Id"]
        )

        students_df["Id"] = students_df["Id"].astype(int)
        attendance_df["Id"] = attendance_df["Id"].astype(int)

        # ====================================================
        # GET ATTENDANCE DATE
        # ====================================================

        if attendance_df.empty:

            messagebox.showwarning(
                "No Attendance",
                "The selected attendance file is empty."
            )

            return

        attendance_date = str(
            attendance_df.iloc[0]["Date"]
        )

        # ====================================================
        # CREATE ATTENDANCE ID SET
        # ====================================================

        present_ids = set(
            attendance_df["Id"].tolist()
        )

        # ====================================================
        # EMAIL COUNTERS
        # ====================================================

        sent_count = 0
        skipped_count = 0
        failed_count = 0

        # ====================================================
        # CONNECT TO GMAIL
        # ====================================================

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            print("\nConnecting to Gmail...")

            smtp.login(
                sender_email,
                sender_pass
            )

            print("Gmail login successful.")

            # =================================================
            # PROCESS EACH STUDENT
            # =================================================

            for _, student in students_df.iterrows():

                student_id = int(student["Id"])

                student_name = str(
                    student["Name"]
                ).strip()

                receiver_email = str(
                    student["Email Id"]
                ).strip()

                # ------------------------------------------------
                # Validate email
                # ------------------------------------------------

                if (
                    not receiver_email
                    or receiver_email.lower() == "nan"
                    or "@" not in receiver_email
                ):

                    print(
                        f"Skipping {student_name}: "
                        f"invalid email."
                    )

                    skipped_count += 1
                    continue

                # ------------------------------------------------
                # Determine attendance status
                # ------------------------------------------------

                if student_id in present_ids:

                    status = "Present"

                    subject = (
                        f"Attendance Marked - "
                        f"{attendance_date}"
                    )

                    body = f"""
Hello {student_name},

Your attendance has been successfully marked.

Date: {attendance_date}
Status: Present

Student ID: {student_id}

Regards,
Face Recognition Attendance System
"""

                else:

                    status = "Absent"

                    subject = (
                        f"Attendance Alert - "
                        f"{attendance_date}"
                    )

                    body = f"""
Hello {student_name},

Our attendance system did not detect your presence
during today's attendance session.

Date: {attendance_date}
Status: Absent

Student ID: {student_id}

If you believe this is incorrect, please contact
the administrator.

Regards,
Face Recognition Attendance System
"""

                # =================================================
                # CREATE EMAIL
                # =================================================

                msg = EmailMessage()

                msg["From"] = sender_email
                msg["To"] = receiver_email
                msg["Subject"] = subject

                msg.set_content(
                    body.strip()
                )

                # =================================================
                # ATTACH ATTENDANCE FILE
                # =================================================

                try:

                    with open(
                        attendance_file,
                        "rb"
                    ) as file:

                        file_data = file.read()

                    file_name = os.path.basename(
                        attendance_file
                    )

                    msg.add_attachment(
                        file_data,
                        maintype="application",
                        subtype=(
                            "vnd.openxmlformats-officedocument"
                            ".spreadsheetml.sheet"
                        ),
                        filename=file_name
                    )

                except Exception as attachment_error:

                    print(
                        f"Could not attach file for "
                        f"{student_name}: "
                        f"{attachment_error}"
                    )

                # =================================================
                # SEND EMAIL
                # =================================================

                try:

                    smtp.send_message(msg)

                    print(
                        f"[SENT] "
                        f"{student_id} - "
                        f"{student_name} - "
                        f"{status} - "
                        f"{receiver_email}"
                    )

                    sent_count += 1

                except Exception as email_error:

                    print(
                        f"[FAILED] "
                        f"{student_name}: "
                        f"{email_error}"
                    )

                    failed_count += 1

        # ========================================================
        # RESULT
        # ========================================================

        messagebox.showinfo(
            "Email Completed",
            f"Emails sent: {sent_count}\n"
            f"Skipped: {skipped_count}\n"
            f"Failed: {failed_count}"
        )

        print("\n" + "=" * 60)
        print("EMAIL PROCESS COMPLETED")
        print("=" * 60)

        print(f"Emails sent    : {sent_count}")
        print(f"Emails skipped : {skipped_count}")
        print(f"Emails failed  : {failed_count}")

    except Exception as e:

        messagebox.showerror(
            "Email Error",
            str(e)
        )

        print(
            f"\nERROR: {e}"
        )




# import smtplib
# from email.message import EmailMessage
# import pandas
# import tkinter as tk
# from tkinter import filedialog, messagebox


# def browse_file(self):
#     file_path = filedialog.askopenfilename(title="Select Attendance File", filetypes=[("Excel Files", "*.xlsx *.xls")])
#     if file_path:
#         self.attechment_entry.delete(0, tk.END)
#         self.attechment_entry.insert(0, file_path)


# def send_email(self):
#     sender_email = self.sender_email_entry.get()
#     sender_pass = self.sender_pass_entry.get()
#     attechment = self.attechment_entry.get()

#     if not (sender_email and sender_pass and attechment):
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     try:
#         df = pandas.read_excel(attechment)
#         receivers_email = df["EMAIL_ID"].values
#         sub = ("Test Mail")
#         attach_files = df["Files to be attached"]
#         name = df["NAME"].values

#         zipped = zip(receivers_email, attach_files, name)

#         for (a, b, c) in zipped:
#             msg = EmailMessage()
#             files = [(attechment.format(b))]

#             for file in files:
#                 with open(file, 'rb') as f:
#                     file_data = f.read()
#                     file_name = f.name

#                 msg['From'] = sender_email
#                 msg['To'] = a
#                 msg['Subject'] = sub
#                 msg.set_content(f"hello {c}! I have something for you.")
#                 msg.add_attachment(file_data, maintype='application', subtype='octet-stream',
#                                    filename="{}.xls".format(b))

#                 with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                     smtp.login(sender_email, sender_pass)

#                     smtp.send_message(msg)

#         messagebox.showinfo("Success", "All mails sent successfully!")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# kvojqrgkjubveahb









# import os
# import smtplib
# from email.message import EmailMessage
# # from getpass import getpass
# import pandas
#
#
# def mail():
#     sender_email = input("Enter Your Email ID: ")
#     sender_pass = input("Enter Your Password: ")
#     attechment = input("Enter the Attendance file Path: ")
#
#     df = pandas.read_excel("E:\For email.xlsx")
#     receivers_email = df["EMAIL_ID"].values
#     sub = ("Test Mail ")
#     attach_files = df["Files to be attached"]
#     name = df["NAME"].values
#
#     zipped = zip(receivers_email, attach_files, name)
#
#     for (a, b, c) in zipped:
#
#         msg = EmailMessage()
#         files = [(attechment.format(b))]
#
#         for file in files:
#             with open(file, 'rb') as f:
#                 file_data = f.read()
#                 file_name = f.name
#
#             msg['From'] = sender_email
#             msg['To'] = a
#             msg['Subject'] = sub
#             msg.set_content(f"hello {c}! I have something for you.")
#             msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename="{}.xls".format(b))
#
#             with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                 smtp.login(sender_email, sender_pass)
#
#                 smtp.send_message(msg)
#
#     print("All mail sent!")
#
# E:\For email.xlsx
