import automail
import json
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os

file_path = "F:/FRAS/StudentDetails/NewRegisterInfo.json"
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
        self.login_button.bind("<Enter>", lambda k: self.login_button.config(bg="#8D918D"))
        self.login_button.bind("<Leave>", lambda k: self.login_button.config(bg="#555555"))

        # Register Button
        self.register_login_button = tk.Button(sidebar_frame, text="Register", command=self.register,
                                               borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                               pady=10)
        self.register_login_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.register_login_button.bind("<Enter>", lambda k: self.register_login_button.config(bg="#8D918D"))
        self.register_login_button.bind("<Leave>", lambda k: self.register_login_button.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.login_frame, bg="#CECECE")
        main_frame.pack(side="right", fill="both", expand=True)

        # Add sidebar buttons

        self.username_label_login = tk.Label(main_frame, text="Enter Username: ", fg="black", font=("Helvetica", 14))
        self.username_label_login.pack(side="top", pady=10, padx=10, fill="y")
        self.username_entry_login = tk.Entry(main_frame, font=("Helvetica", 14))
        self.username_entry_login.pack(side="top", pady=10, padx=10, fill="y")

        self.password_label_login = tk.Label(main_frame, text="Enter Password", fg="black", font=("Helvetica", 14))
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
        # New Register Button
        self.new_register_button = tk.Button(sidebar_frame, text="Register", command=self.register_user,
                                             borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                             pady=10)
        self.new_register_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.new_register_button.bind("<Enter>", lambda e: self.new_register_button.config(bg="#8D918D"))
        self.new_register_button.bind("<Leave>", lambda e: self.new_register_button.config(bg="#555555"))

        # Back Button
        self.register_back_button = tk.Button(sidebar_frame, text="Back", command=self.close_register_window,
                                              borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                              pady=10)
        self.register_back_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.register_back_button.bind("<Enter>", lambda e: self.register_back_button.config(bg="#8D918D"))
        self.register_back_button.bind("<Leave>", lambda e: self.register_back_button.config(bg="#555555"))

        # Create main frame
        main_frame = tk.Frame(self.register_frame, bg="#CECECE")
        main_frame.pack(side="right", fill="both", expand=True)

        # Add sidebar buttons

        self.register_name_label = tk.Label(main_frame, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
        self.register_name_label.pack(side="top", pady=10, padx=10, fill="y")
        self.register_name_entry = tk.Entry(main_frame, font=("Helvetica", 14))
        self.register_name_entry.pack(side="top", pady=10, padx=10, fill="y")

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
        # self.image = self.image.resize((800, 600), resample=Image.LANCZOS)
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
        self.take_image_button = tk.Button(sidebar_frame, text="Take Images", command=self.take_images,
                                           borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                           pady=10)
        self.take_image_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Check Camera button
        self.take_image_button.bind("<Enter>", lambda e: self.take_image_button.config(bg="#8D918D"))
        self.take_image_button.bind("<Leave>", lambda e: self.take_image_button.config(bg="#555555"))

        # Back Button
        self.capture_faces_back_button = tk.Button(sidebar_frame, text="Back", command=self.close_capture_window,
                                                   borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
                                                   pady=10)
        self.capture_faces_back_button.pack(side="top", pady=10, padx=10, fill="x")
        # Bind the hover effect to the Capture Faces button
        self.capture_faces_back_button.bind("<Enter>", lambda e: self.capture_faces_back_button.config(bg="#8D918D"))
        self.capture_faces_back_button.bind("<Leave>", lambda e: self.capture_faces_back_button.config(bg="#555555"))

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
        automail.browse_file(self)

    def send_email(self):
        automail.send_email(self)

    def close_window_mail(self):
        self.auto_mail_frame.pack_forget()  # Hide login_frame
        self.main_frame.pack()  # Show register_frame

    # $$$$$$$$$$$$$$$$$$$$$$$$$$ Capture Images Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
    def take_images(self):
        import Capture_Image
        Capture_Image.take_image(self)

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

        try:
            with open(file_path, "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        # Check if username and password are correct
        if username in users and users[username]['password'] == password:
            self.main_page()
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
        name = self.register_name_entry.get()
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
        self.register_name_entry.delete(0, tk.END)
        self.username_entry_reg.delete(0, tk.END)
        self.password_entry_reg.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    gui = Login(root)
    root.mainloop()

# import os  # accessing the os functions
# import check_camera
# import Capture_Image
# import Train_Image
# import Recognize
# import automail
# import pyfiglet
# from tkinter import *
#
# # creating the title bar function
#
# def title_bar():
#     os.system('cls')  # for windows
#
#     # title of the program
#
#     ascii_banner = pyfiglet.figlet_format("Face   Recognition   Attendance   System", font="digital", width=100)
#     print(ascii_banner)
#
# # creating the user main menu function
#
# def mainMenu():
#     title_bar()
#     print()
#     print(10 * "*", "WELCOME MENU", 10 * "*")
#     print(" [1] Check Camera")
#     print(" [2] Capture Faces")
#     print(" [3] Train Images")
#     print(" [4] Recognize & Attendance")
#     print(" [5] Auto Mail")
#     print(" [6] Quit")
#
#     while True:
#         try:
#             choice = int(input("Enter Choice: "))
#
#             if choice == 1:
#                 checkCamera()
#                 break
#             elif choice == 2:
#                 CaptureFaces()
#                 break
#             elif choice == 3:
#                 Trainimages()
#                 break
#             elif choice == 4:
#                 RecognizeFaces()
#                 break
#             elif choice == 5:
#                 automail.mail()
#                 # os.system("py automail.py")
#                 break
#                 mainMenu()
#             elif choice == 6:
#                 print("Thank You")
#                 break
#             else:
#                 print("Invalid Choice. Enter 1-4")
#                 mainMenu()
#         except ValueError:
#             print("Invalid Choice. Enter 1-4\n Try Again")
#     exit
#
#
# # ---------------------------------------------------------
# # calling the camera test function from check camera.py file
#
# def checkCamera():
#     check_camera.camer()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # --------------------------------------------------------------
# # calling the take image function form capture image.py file
#
# def CaptureFaces():
#     Capture_Image.takeImages()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # -----------------------------------------------------------------
# # calling the train images from train_images.py file
#
# def Trainimages():
#     Train_Image.TrainImages()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # --------------------------------------------------------------------
# # calling the recognize_attendance from recognize.py file
#
# def RecognizeFaces():
#     Recognize.recognize_attendence()
#     key = input("Enter any key to return main menu")
#     mainMenu()
#
#
# # ---------------main driver ------------------
# mainMenu()
