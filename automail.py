import smtplib
from email.message import EmailMessage
import pandas
import tkinter as tk
from tkinter import filedialog, messagebox


def browse_file(self):
    file_path = filedialog.askopenfilename(title="Select Attendance File", filetypes=[("Excel Files", "*.xlsx *.xls")])
    if file_path:
        self.attechment_entry.delete(0, tk.END)
        self.attechment_entry.insert(0, file_path)


def send_email(self):
    sender_email = self.sender_email_entry.get()
    sender_pass = self.sender_pass_entry.get()
    attechment = self.attechment_entry.get()

    if not (sender_email and sender_pass and attechment):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        df = pandas.read_excel(attechment)
        receivers_email = df["EMAIL_ID"].values
        sub = ("Test Mail")
        attach_files = df["Files to be attached"]
        name = df["NAME"].values

        zipped = zip(receivers_email, attach_files, name)

        for (a, b, c) in zipped:
            msg = EmailMessage()
            files = [(attechment.format(b))]

            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name

                msg['From'] = sender_email
                msg['To'] = a
                msg['Subject'] = sub
                msg.set_content(f"hello {c}! I have something for you.")
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream',
                                   filename="{}.xls".format(b))

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(sender_email, sender_pass)

                    smtp.send_message(msg)

        messagebox.showinfo("Success", "All mails sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

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
