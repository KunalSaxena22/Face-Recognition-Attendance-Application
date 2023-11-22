import automail
import json
import os
# from automail import EmailSenderApp
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

# # Define file path for user data
# file_path = "F:/FRAS/New Registration"
#
# try:
#     # Check if file exists, create it if necessary
#     if not os.path.isfile(file_path):
#         with open(file_path, 'w') as f:
#             json.dump({}, f)
#
#     # Load user data from file
#     with open(file_path, "r") as f:
#         users = json.load(f)
#
# except PermissionError:
#     print("Error: Permission denied. Check file permissions or run the program with administrator privileges.")
#
# except Exception as e:
#     print(f"Error: {e}")
#     users = {}
#
#
# class login:
#     def __init__(self, master):
#         self.master = master
#         self.login_frame = tk.Frame(master)
#         self.register_frame = tk.Frame(master)
#         self.create_widgets()
#         # master.title("Face Recognition Attendance System")
#         # master.geometry('1000x600')
#
#     def create_widgets(self):
#         # # Load the background image
#         # self.image = Image.open("IMG20201107134424.jpg")
#         # # Resize the image to 800x600
#         # self.image = self.image.resize((1000, 600), resample=Image.LANCZOS)
#         # self.background_image = ImageTk.PhotoImage(self.image)
#         # # Create a label for the background image
#         # self.background_label = tk.Label(master, image=self.background_image, bg="SystemButtonFace")
#         # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
#         # Set up styles
#         title_font = ("Arial", 36, "bold")
#         button_font = ("Arial", 14)
#         button_color = 'light blue'
#         #
#         # # Create header frame
#         # header_frame = tk.Frame(master, bg="#333333", height=80)
#         # header_frame.pack(fill="x")
#
#         # # Add header label
#         # header_label = tk.Label(header_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM", fg="#333333",
#         #                         font=("Arial", 24), padx=240)
#         # header_label.pack(side="left", pady=10)
#
#         # # Create login container frame
#         # self.login_frame = tk.Frame(self, bg="#FFFFFF", padx=50, pady=30)
#         # self.login_frame.pack(pady=40)
#
#         # Username label
#         self.username_label = tk.Label(self.login_frame, text="Username:", font=button_font, bg="#FFFFFF")
#         self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#
#         # Username entry
#         self.username_entry = tk.Entry(self.login_frame, font=button_font)
#         self.username_entry.grid(row=0, column=1, padx=10, pady=10)
#
#         # Password label
#         self.password_label = tk.Label(self.login_frame, text="Password:", font=button_font, bg="#FFFFFF")
#         self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
#
#         # Password entry
#         self.password_entry = tk.Entry(self.login_frame, font=button_font, show="*")
#         self.password_entry.grid(row=1, column=1, padx=10, pady=10)
#
#         # Register button
#         self.register_button = tk.Button(self.login_frame, text="Register", command=self.register, font=button_font,
#                                          bg=button_color, fg="#2F4F4F")
#         self.register_button.grid(row=2, columnspan=2, padx=10, pady=10)
#         # Bind the hover effect to the Register button
#         self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg="cyan"))
#         self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg=button_color))
#
#         # Login button
#         self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, font=button_font,
#                                       bg=button_color, fg="#2F4F4F")
#         self.login_button.grid(row=2, columnspan=1, padx=10, pady=10)
#         # Bind the hover effect to the Login button
#         self.login_button.bind("<Enter>", lambda e: self.login_button.config(bg="cyan"))
#         self.login_button.bind("<Leave>", lambda e: self.login_button.config(bg=button_color))
#
#         # # Quit button
#         # self.quit_button = tk.Button(self.login_frame, text="Quit", command=self.quit, font=button_font, bg=button_color,
#         #                              fg='#2F4F4F', padx=20, pady=10)
#         # self.quit_button.pack(pady=2)
#         # # Bind the hover effect to the Quit button
#         # self.quit_button.bind("<Enter>", lambda e: self.quit_button.config(bg="cyan"))
#         # self.quit_button.bind("<Leave>", lambda e: self.quit_button.config(bg=button_color))
#
#
#         #Frame 2 start
#         # Create the title label register_frame
#         self.register_title_label = tk.Label(self.register_frame, text="Registration", fg="#2F4F4F", font=title_font)
#         self.register_title_label.pack(pady=20)
#         # # Create login container frame
#         # self.register_frame = tk.Frame(self.register_frame, bg="#FFFFFF", padx=50, pady=30)
#         # self.register_frame.pack(pady=40)
#
#         # Name label
#         self.name_label = tk.Label(self.register_frame, text="Name:", font=button_font, bg="#FFFFFF")
#         self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#         # Name entry
#         self.name_entry = tk.Entry(self.register_frame, font=button_font)
#         self.name_entry.grid(row=0, column=1, padx=10, pady=10)
#
#         # Username label
#         self.username_label = tk.Label(self.register_frame, text="Username:", font=button_font, bg="#FFFFFF")
#         self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
#         # Username entry
#         self.username_entry = tk.Entry(self.register_frame, font=button_font)
#         self.username_entry.grid(row=1, column=1, padx=10, pady=10)
#
#         # Password label
#         self.password_label = tk.Label(self.register_frame, text="Password:", font=button_font, bg="#FFFFFF")
#         self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
#         # Password entry
#         self.password_entry = tk.Entry(self.register_frame, font=button_font, show="*")
#         self.password_entry.grid(row=2, column=1, padx=10, pady=10)
#
#         # New Register button
#         self.register_button = tk.Button(self.register_frame, text="Register", command=self.register_user,
#                                          font=button_font, bg=button_color, fg="#2F4F4F")
#         self.register_button.grid(row=3, columnspan=2, padx=10, pady=10)
#         # Bind the hover effect to the Register button
#         self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg="cyan"))
#         self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg=button_color))
#
#         self.login_frame.pack()
#
#         # self.eval('tk::PlaceWindow %s center' % self.winfo_toplevel())
#
#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#
#         # Add code to check if username and password are correct
#         if username == "admin" and password == "password":
#             self.master.destroy()  # Destroy login window
#             app1 = main.FaceRecognitionApp()
#             app1.mainloop()
#         else:
#             tk.messagebox.showerror("Error", "Invalid username or password")
#
#     def register(self):
#         self.login_frame.pack_forget()  # Hide login_frame
#         self.register_frame.pack()  # Show register_frame
#     #     self.title("Registration")
#     #     self.geometry('1000x600')
#     #     self.configure(bg='#C0C0C0')
#     #
#     #     # Set up styles
#     #     title_font = ("Arial", 24, "bold")
#     #     button_font = ("Arial", 14)
#     #     button_color = 'light blue'
#     #
#     #     # Create the title label register_frame
#     #     self.register_title_label = tk.Label(self.register_frame, text="Registration", fg="#2F4F4F", font=title_font)
#     #     self.register_title_label.pack(pady=20)
#     #     # # Create login container frame
#     #     # self.register_frame = tk.Frame(self.register_frame, bg="#FFFFFF", padx=50, pady=30)
#     #     # self.register_frame.pack(pady=40)
#     #
#     #     # Name label
#     #     self.name_label = tk.Label(self.register_frame, text="Name:", font=button_font, bg="#FFFFFF")
#     #     self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#     #     # Name entry
#     #     self.name_entry = tk.Entry(self.register_frame, font=button_font)
#     #     self.name_entry.grid(row=0, column=1, padx=10, pady=10)
#     #
#     #     # Username label
#     #     self.username_label = tk.Label(self.register_frame, text="Username:", font=button_font, bg="#FFFFFF")
#     #     self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
#     #     # Username entry
#     #     self.username_entry = tk.Entry(self.register_frame, font=button_font)
#     #     self.username_entry.grid(row=1, column=1, padx=10, pady=10)
#     #
#     #     # Password label
#     #     self.password_label = tk.Label(self.register_frame, text="Password:", font=button_font, bg="#FFFFFF")
#     #     self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
#     #     # Password entry
#     #     self.password_entry = tk.Entry(self.register_frame, font=button_font, show="*")
#     #     self.password_entry.grid(row=2, column=1, padx=10, pady=10)
#     #
#     #     # New Register button
#     #     self.register_button = tk.Button(self.register_frame, text="Register", command=self.register_user,
#     #                                      font=button_font, bg=button_color, fg="#2F4F4F")
#     #     self.register_button.grid(row=3, columnspan=2, padx=10, pady=10)
#     #     # Bind the hover effect to the Register button
#     #     self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg="cyan"))
#     #     self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg=button_color))
#
#         # Register new user
#
#     def register_user(self):
#         name = self.name_entry.get()
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#
#         # Check if all fields are filled
#         if name == '' or username == '' or password == '':
#             tk.messagebox.showerror("Error", "Please fill in all fields")
#             return
#
#         # Check if username is already taken
#         if username in users:
#             tk.messagebox.showerror("Error", "Username already taken")
#             return
#
#         # Add new user to dictionary of users
#         users[username] = {
#             'name': name,
#             'password': password
#         }
#
#         # Save updated user data to file
#         with open(file_path, "w") as f:
#             json.dump(users, f)
#
#         # Show success message
#         tk.messagebox.showinfo("Success", "User registered successfully")
#
#         # Clear the registration form
#         self.name_entry.delete(0, tk.END)
#         self.username_entry.delete(0, tk.END)
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = login(root)
#     root.mainloop()
#


file_path = "NewRegistration"

try:
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            json.dump({}, f)

    # Load user data from file
    with open(file_path, "r") as f:
        users = json.load(f)

except PermissionError:
    print("Error: Permission denied. Check file permissions or run the program with administrator privileges.")

except Exception as e:
    print(f"Error: {e}")
    users = {}


class Login:
    def __init__(self, master):
        self.master = master
        self.master.bind("<Configure>", self.on_resize)  # bind the resize event to the on_resize method
        self.login_frame = tk.Frame(self.master)
        self.register_frame = tk.Frame(self.master)
        self.main_frame = tk.Frame(self.master)
        self.capture_face_frame = tk.Frame(self.master)
        self.auto_mail_frame = tk.Frame(self.master)

        self.create_widgets()
        self.master.geometry("1000x600")

    def create_widgets(self):
        ################################# Login Frame ##############################################################
        # Create header frame
        header_frame = tk.Frame(self.login_frame, bg="#333333", height=80)
        header_frame.pack(fill="x")

        # Add header label
        header_label = tk.Label(header_frame, text="LOGIN", fg="#333333", font=("Arial", 24), padx=450)
        header_label.pack(side="left", pady=10)

        # Create sidebar frame
        sidebar_frame = tk.Frame(self.login_frame, bg="#444444", width=200)
        sidebar_frame.pack(side="left", fill="y")

        # Add sidebar buttons
        # Login Button
        self.login_button = tk.Button(sidebar_frame, text="Login", command=self.login,
                                      borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
        self.login_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.login_button.bind("<Enter>", lambda e: self.login_button.config(bg="#8D918D"))
        self.login_button.bind("<Leave>", lambda e: self.login_button.config(bg="#555555"))

        # Register Button
        self.register_button = tk.Button(sidebar_frame, text="Register", command=self.register,
                                         borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
        self.register_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg="#8D918D"))
        self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.login_frame, bg="#CECECE")
        main_frame.pack(side="right", fill="both", expand=True)

        # Add sidebar buttons

        self.username_label_login = tk.Label(main_frame, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
        self.username_label_login.pack(side="top", pady=10, padx=10, fill="y")
        self.username_entry_login = tk.Entry(main_frame, font=("Helvetica", 14))
        self.username_entry_login.pack(side="top", pady=10, padx=10, fill="y")

        self.password_label_login = tk.Label(main_frame, text="Enter Your Username", fg="black", font=("Helvetica", 14))
        self.password_label_login.pack(side="top", pady=10, padx=10, fill="y")
        self.password_entry_login = tk.Entry(main_frame, font=("Helvetica", 14), show="*")
        self.password_entry_login.pack(side="top", pady=10, padx=10, fill="y")

        ################################# Register Frame ##############################################################

        # Create header frame
        header_frame = tk.Frame(self.register_frame, bg="#333333", height=80)
        header_frame.pack(fill="x")

        # Add header label
        header_label = tk.Label(header_frame, text="REGISTRATION", fg="#333333", font=("Arial", 24), padx=400)
        header_label.pack(side="left", pady=10)

        # Create sidebar frame
        sidebar_frame = tk.Frame(self.register_frame, bg="#444444", width=200)
        sidebar_frame.pack(side="left", fill="y")

        # Add sidebar buttons
        # Take Image Button
        self.register_button = tk.Button(sidebar_frame, text="Register", command=self.register_user,
                                         borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                         pady=10)
        self.register_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg="#8D918D"))
        self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg="#555555"))

        # Back Button
        self.capture_faces_button = tk.Button(sidebar_frame, text="Back", command=self.close_register_window,
                                              borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                              pady=10)
        self.capture_faces_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.capture_faces_button.bind("<Enter>", lambda e: self.capture_faces_button.config(bg="#8D918D"))
        self.capture_faces_button.bind("<Leave>", lambda e: self.capture_faces_button.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.register_frame, bg="#CECECE")
        main_frame.pack(side="right", fill="both", expand=True)

        # Add sidebar buttons

        self.name_label = tk.Label(main_frame, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
        self.name_label.pack(side="top", pady=10, padx=10, fill="y")
        self.name_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.name_entry.pack(side="top", pady=10, padx=10, fill="y")

        self.username_label_reg = tk.Label(main_frame, text="Enter Your Username", fg="black", font=("Helvetica", 14))
        self.username_label_reg.pack(side="top", pady=10, padx=10, fill="y")
        self.username_entry_reg = tk.Entry(main_frame, font=("Helvetica", 14))
        self.username_entry_reg.pack(side="top", pady=10, padx=10, fill="y")

        self.password_label_reg = tk.Label(main_frame, text="Enter Your Password", fg="black", font=("Helvetica", 14))
        self.password_label_reg.pack(side="top", pady=10, padx=10, fill="y")
        self.password_entry_reg = tk.Entry(main_frame, font=("Helvetica", 14))
        self.password_entry_reg.pack(side="top", pady=10, padx=10, fill="y")

        ################################# Main Frame ##############################################################

        # Create header frame
        header_frame = tk.Frame(self.main_frame, bg="#333333", height=80)
        header_frame.pack(fill="x")

        # Add header label
        header_label = tk.Label(header_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM", fg="#333333",
                                font=("Arial", 24), padx=240)
        header_label.pack(side="left", pady=10)

        # Create sidebar frame
        sidebar_frame = tk.Frame(self.main_frame, bg="#444444", width=200)
        sidebar_frame.pack(side="left", fill="y")

        # Add sidebar buttons
        buttons = {
            "Check Camera": self.check_camera,
            "Capture Faces": self.capture_faces,
            "Train Images": self.train_images,
            "Recognize & Attendance": self.recognize_attendance,
            "Mail": self.auto_mail,
            "Exit": self.close_app
        }

        for button_text, command_func in buttons.items():
            button = tk.Button(sidebar_frame, text=button_text, command=command_func,
                               borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
            button.pack(side="top", pady=10, padx=10, fill="x")
            # Bind the hover effect to the button
            button.bind("<Enter>", lambda e, b=button: b.config(bg="#8D918D"))
            button.bind("<Leave>", lambda e, b=button: b.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
        main_frame.pack(side="right", fill="both", expand=True)

        # Load the background image
        self.image = Image.open("facial-recognition-face-recognition.jpg")
        # Resize the image to 800x600
        self.image = self.image.resize((800, 600), resample=Image.LANCZOS)
        self.background_image = ImageTk.PhotoImage(self.image)
        # Create a label for the background image
        self.background_label = tk.Label(main_frame, image=self.background_image, bg="SystemButtonFace")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        ######################################### Capture Face Frame ####################################################################

        # Create header frame
        header_frame = tk.Frame(self.capture_face_frame, bg="#333333", height=80)
        header_frame.pack(fill="x")

        # Add header label
        header_label = tk.Label(header_frame, text="CAPTURE IMAGES", fg="#333333", font=("Arial", 24), padx=360)
        header_label.pack(side="left", pady=10)

        # Create sidebar frame
        sidebar_frame = tk.Frame(self.capture_face_frame, bg="#444444", width=200)
        sidebar_frame.pack(side="left", fill="y")

        # Add sidebar buttons
        # Take Image Button
        self.check_camera_button = tk.Button(sidebar_frame, text="Take Images", command=self.take_images,
                                             borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                             pady=10)
        self.check_camera_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.check_camera_button.bind("<Enter>", lambda e: self.check_camera_button.config(bg="#8D918D"))
        self.check_camera_button.bind("<Leave>", lambda e: self.check_camera_button.config(bg="#555555"))

        # Back Button
        self.capture_faces_button = tk.Button(sidebar_frame, text="Back", command=self.close_capture_window,
                                              borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                              pady=10)
        self.capture_faces_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.capture_faces_button.bind("<Enter>", lambda e: self.capture_faces_button.config(bg="#8D918D"))
        self.capture_faces_button.bind("<Leave>", lambda e: self.capture_faces_button.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.capture_face_frame, bg="#CECECE")
        main_frame.pack(side="right", fill="both", expand=True)

        # Add sidebar buttons
        self.id_label = tk.Label(main_frame, text="Enter Your Id: ", fg="black", font=("Helvetica", 14))
        self.id_label.pack(side="top", pady=10, padx=10, fill="y")
        self.id_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.id_entry.pack(side="top", pady=10, padx=10, fill="y")

        self.name_label = tk.Label(main_frame, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
        self.name_label.pack(side="top", pady=10, padx=10, fill="y")
        self.name_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.name_entry.pack(side="top", pady=10, padx=10, fill="y")

        self.rollno_label = tk.Label(main_frame, text="Enter Your Roll No.: ", fg="black", font=("Helvetica", 14))
        self.rollno_label.pack(side="top", pady=10, padx=10, fill="y")
        self.rollno_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.rollno_entry.pack(side="top", pady=10, padx=10, fill="y")

        self.email_label = tk.Label(main_frame, text="Enter Your Valid Email Id: ", fg="black", font=("Helvetica", 14))
        self.email_label.pack(side="top", pady=10, padx=10, fill="y")
        self.email_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.email_entry.pack(side="top", pady=10, padx=10, fill="y")

        ################################################### Auto Mail Frame #####################################################

        # Create header frame
        header_frame = tk.Frame(self.auto_mail_frame, bg="#333333", height=80)
        header_frame.pack(fill="x")

        # Add header label
        header_label = tk.Label(header_frame, text="SENDING MAIL WITH ATTACHMENT", fg="#333333", font=("Arial", 24),
                                padx=360)
        header_label.pack(side="left", pady=10)

        # Create sidebar frame
        sidebar_frame = tk.Frame(self.auto_mail_frame, bg="#444444", width=200)
        sidebar_frame.pack(side="left", fill="y")

        # Add sidebar buttons
        # browse button
        self.browse_file_button = tk.Button(sidebar_frame, text="Browse", command=self.browse_file, borderwidth=5,
                                            font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
        self.browse_file_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.browse_file_button.bind("<Enter>", lambda e: self.browse_file_button.config(bg="#8D918D"))
        self.browse_file_button.bind("<Leave>", lambda e: self.browse_file_button.config(bg="#555555"))

        # email button
        self.send_email_button = tk.Button(sidebar_frame, text="Send Email", command=self.send_email, borderwidth=5,
                                           font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
        self.send_email_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.send_email_button.bind("<Enter>", lambda e: self.send_email_button.config(bg="#8D918D"))
        self.send_email_button.bind("<Leave>", lambda e: self.send_email_button.config(bg="#555555"))

        # Back Button
        self.capture_faces_button = tk.Button(sidebar_frame, text="Back", command=self.close_window_mail,
                                              borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                              pady=10)
        self.capture_faces_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.capture_faces_button.bind("<Enter>", lambda e: self.capture_faces_button.config(bg="#8D918D"))
        self.capture_faces_button.bind("<Leave>", lambda e: self.capture_faces_button.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.auto_mail_frame, bg="#CECECE")
        main_frame.pack(side="right", fill="both", expand=True)

        # Add sidebar buttons
        # Create the label and entry for sender email
        self.sender_email_label = tk.Label(main_frame, text="Enter Your Email ID: ", fg="black", font=("Helvetica", 14))
        self.sender_email_label.pack(side="top", pady=10, padx=10, fill="y")
        self.sender_email_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.sender_email_entry.pack(side="top", pady=10, padx=10, fill="y")

        # Create the label and entry for sender password
        self.sender_pass_label = tk.Label(main_frame, text="Enter Your Password", fg="black", font=("Helvetica", 14))
        self.sender_pass_label.pack(side="top", pady=10, padx=10, fill="y")
        self.sender_pass_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.sender_pass_entry.pack(side="top", pady=10, padx=10, fill="y")

        # Create the label and entry for attachment file
        self.attechment_label = tk.Label(main_frame, text="Enter the Attendance file Path", fg="black",
                                         font=("Helvetica", 14))
        self.attechment_label.pack(side="top", pady=10, padx=10, fill="y")
        self.attechment_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.attechment_entry.pack(side="top", pady=10, padx=10, fill="y")

        # By default
        self.login_frame.pack()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%% Function Start %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    def on_resize(self, event):
        """
        Adjusts the frame size according to the window size
        """
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        self.login_frame.config(width=width, height=height)
        self.register_frame.config(width=width, height=height)
        self.main_frame.config(width=width, height=height)
        self.capture_face_frame.config(width=width, height=height)
        self.auto_mail_frame.config(width=width, height=height)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Auto Mail Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    def browse_file(self):
        import automail
        automail.browse_file(self)

    def send_email(self):
        automail.send_email(self)

    def close_window_mail(self):
        self.auto_mail_frame.pack_forget()  # Hide login_frame
        self.main_frame.pack()  # Show register_frame

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Capture Images Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    def take_images(self):
        import Capture_Image
        Capture_Image.take_images(self)

    def close_capture_window(self):
        self.capture_face_frame.pack_forget()  # Hide login_frame
        self.main_frame.pack()  # Show register_frame

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Main Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    def check_camera(self):
        import check_camera
        check_camera.camer()

    def capture_faces(self):
        self.main_frame.pack_forget()  # Hide main frame
        self.capture_face_frame.pack()  # Show capture face

    def train_images(self):
        import Train_Image
        Train_Image.traingui()

    def recognize_attendance(self):
        import Recognize
        Recognize.recognize_attendence()

    def auto_mail(self):
        self.main_frame.pack_forget()  # Hide login_frame
        self.auto_mail_frame.pack()  # Show register_frame

    def close_app(self):
        # close the GUI
        self.master.destroy()

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Login Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    def main_page(self):
        self.login_frame.pack_forget()  # Hide login_frame
        self.main_frame.pack()  # Show register_frame

    def login(self):
        username = self.username_entry_login.get()
        password = self.password_entry_login.get()

        # Add code to check if username and password are correct
        if username == "admin" and password == "123456789":
            self.main_page()
            # self.master.destroy()  Destroy login window
            # app1 = main.FaceRecognitionApp()
            # app1.mainloop()
        else:
            tk.messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        self.login_frame.pack_forget()  # Hide login_frame
        self.register_frame.pack()  # Show register_frame

        # Register new user

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Register Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    def close_register_window(self):
        self.register_frame.pack_forget()  # Hide login_frame
        self.login_frame.pack()  # Show register_frame

    def register_user(self):
        name = self.name_entry.get()
        username = self.username_entry_reg.get()
        password = self.password_entry_reg.get()

        # Check if all fields are filled
        if name == '' or username == '' or password == '':
            tk.messagebox.showerror("Error", "Please fill in all fields")
            return

        # Check if username is already taken
        if username in users:
            tk.messagebox.showerror("Error", "Username already taken")
            return

        # Add new user to dictionary of users
        users[username] = {
            'name': name,
            'password': password
        }

        # Save updated user data to file
        with open(file_path, "w") as f:
            json.dump(users, f)

        # Show success message
        tk.messagebox.showinfo("Success", "User registered successfully")

        # Clear the registration form
        self.name_entry.delete(0, tk.END)
        self.username_entry_reg.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    gui = Login(root)
    root.mainloop()

# # Define file path for user data
# file_path = "New Registration"
#
# # Check if file exists, create it if necessary
# if not os.path.isfile(file_path):
#     with open(file_path, 'w') as f:
#         json.dump({}, f)
#
# # Load user data from file
# try:
#     with open(file_path, "r") as f:
#         users = json.load(f)
# except FileNotFoundError:
#     users = {}


# class RegistrationForm:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Registration")
#         self.master.geometry('1000x600')
#         self.master.configure(bg='#C0C0C0')
#         #
#         # # Load the background image
#         # self.image = Image.open("IMG20201107134424.jpg")
#         # # Resize the image to 800x600
#         # self.image = self.image.resize((1000, 600), resample=Image.LANCZOS)
#         # self.background_image = ImageTk.PhotoImage(self.image)
#         # # Create a label for the background image
#         # self.background_label = tk.Label(master, image=self.background_image, bg="SystemButtonFace")
#         # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
#         # Set up styles
#         title_font = ("Arial", 24, "bold")
#         button_font = ("Arial", 14)
#         button_color = 'light blue'
#
#         # Create the title label
#         self.register_title_label = tk.Label(master, text="Registration", fg="#2F4F4F",
#                                              font=title_font)
#         self.title_label.pack(pady=20)
#
#         # Create login container frame
#         self.register_frame = tk.Frame(master, bg="#FFFFFF", padx=50, pady=30)
#         self.login_frame.pack(pady=40)
#
#         # Name label
#         self.name_label = tk.Label(self.register_frame, text="Name:", font=button_font, bg="#FFFFFF")
#         self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
#
#         # Name entry
#         self.name_entry = tk.Entry(self.register_frame, font=button_font)
#         self.name_entry.grid(row=0, column=1, padx=10, pady=10)
#
#         # Username label
#         self.username_label = tk.Label(self.register_frame, text="Username:", font=button_font, bg="#FFFFFF")
#         self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
#
#         # Username entry
#         self.username_entry = tk.Entry(self.register_frame, font=button_font)
#         self.username_entry.grid(row=1, column=1, padx=10, pady=10)
#
#         # Password label
#         self.password_label = tk.Label(self.register_frame, text="Password:", font=button_font, bg="#FFFFFF")
#         self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
#
#         # Password entry
#         self.password_entry = tk.Entry(self.register_frame, font=button_font, show="*")
#         self.password_entry.grid(row=2, column=1, padx=10, pady=10)
#
#         # New Register button
#         self.register_button = tk.Button(self.register_frame, text="Register", command=self.register_user,
#                                          font=button_font,
#                                          bg=button_color, fg="#2F4F4F")
#         self.register_button.grid(row=3, columnspan=2, padx=10, pady=10)
#         # Bind the hover effect to the Register button
#         self.register_button.bind("<Enter>", lambda e: self.register_button.config(bg="cyan"))
#         self.register_button.bind("<Leave>", lambda e: self.register_button.config(bg=button_color))
#
#     # Register new user
#     def register_user(self):
#         name = self.name_entry.get()
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#
#         # Check if all fields are filled
#         if name == '' or username == '' or password == '':
#             tk.messagebox.showerror("Error", "Please fill in all fields")
#             return
#
#         # Check if username is already taken
#         if username in users:
#             tk.messagebox.showerror("Error", "Username already taken")
#             return
#
#         # Add new user to dictionary of users
#         users[username] = {
#             'name': name,
#             'password': password
#         }
#
#         # Save updated user data to file
#         with open(file_path, "w") as f:
#             json.dump(users, f)
#
#         # Show success message
#         tk.messagebox.showinfo("Success", "User registered successfully")
#
#         # Clear the registration form
#         self.name_entry.delete(0, tk.END)
#         self.username_entry.delete(0, tk.END)
