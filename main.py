import json
import os
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# ============================================================
# Next-Gen Attendance System
# Main GUI
#
# Authentication:
# Login/Register -> Dashboard
#
# Existing modules used:
#   Capture_Image.py
#   Train_Image.py
#   Recognize.py
#   check_camera.py
#   automail.py
#
# Storage:
#   JSON  -> administrator login/register
#   CSV   -> student details
#   XLSX  -> attendance
# ============================================================


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STUDENT_DETAILS_DIR = os.path.join(BASE_DIR, "StudentDetails")
TRAINING_IMAGE_DIR = os.path.join(BASE_DIR, "TrainingImage")
ATTENDANCE_DIR = os.path.join(BASE_DIR, "Attendance")

os.makedirs(STUDENT_DETAILS_DIR, exist_ok=True)
os.makedirs(TRAINING_IMAGE_DIR, exist_ok=True)
os.makedirs(ATTENDANCE_DIR, exist_ok=True)

AUTH_FILE = os.path.join(
    STUDENT_DETAILS_DIR,
    "NewRegisterInfo.json"
)

STUDENT_CSV = os.path.join(
    STUDENT_DETAILS_DIR,
    "StudentDetails.csv"
)

TRAINER_FILE = os.path.join(
    TRAINING_IMAGE_DIR,
    "Trainner.yml"
)


# Create authentication file if it does not exist.
if not os.path.isfile(AUTH_FILE):
    try:
        with open(AUTH_FILE, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)
    except Exception as error:
        print(f"Could not create authentication file: {error}")


# ============================================================
# MAIN APPLICATION CLASS
# ============================================================

class Login:

    def __init__(self, master):

        self.master = master

        # ----------------------------------------------------
        # Window
        # ----------------------------------------------------
        self.master.title(
            "AttendX - Next-Gen Attendance System"
        )

        self.master.geometry("1200x720")
        self.master.minsize(1000, 650)
        self.master.configure(bg="#F4F6F8")

        self.master.protocol(
            "WM_DELETE_WINDOW",
            self.close_app
        )

        # Currently logged-in administrator
        self.current_user = None

        # ----------------------------------------------------
        # Main screens
        # ----------------------------------------------------
        self.login_frame = tk.Frame(
            self.master,
            bg="#F4F6F8"
        )

        self.register_frame = tk.Frame(
            self.master,
            bg="#F4F6F8"
        )

        self.main_frame = tk.Frame(
            self.master,
            bg="#F4F6F8"
        )

        self.capture_face_frame = tk.Frame(
            self.master,
            bg="#F4F6F8"
        )

        self.auto_mail_frame = tk.Frame(
            self.master,
            bg="#F4F6F8"
        )

        # ----------------------------------------------------
        # Create all screens
        # ----------------------------------------------------
        self.create_login_screen()
        self.create_register_screen()
        self.create_dashboard()
        self.create_capture_screen()
        self.create_mail_screen()

        # ----------------------------------------------------
        # Start with LOGIN screen
        # ----------------------------------------------------
        self.show_login()

    # ========================================================
    # COMMON FUNCTIONS
    # ========================================================

    def hide_all_frames(self):
        """
        Hide every application screen.
        """

        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.main_frame.pack_forget()
        self.capture_face_frame.pack_forget()
        self.auto_mail_frame.pack_forget()

    def show_login(self):
        """
        Show the authentication/login screen.
        """

        self.hide_all_frames()

        self.login_frame.pack(
            fill="both",
            expand=True
        )

        self.username_entry_login.focus_set()

    def make_sidebar_button(
        self,
        parent,
        text,
        command
    ):
        """
        Create a consistent sidebar button.
        """

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg="#263238",
            fg="white",
            activebackground="#37474F",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=9
        )

        button.pack(
            fill="x",
            padx=16,
            pady=3
        )

        button.bind(
            "<Enter>",
            lambda event: button.config(
                bg="#37474F"
            )
        )

        button.bind(
            "<Leave>",
            lambda event: button.config(
                bg="#263238"
            )
        )

        return button

    # ========================================================
    # LOGIN SCREEN
    # ========================================================

    def create_login_screen(self):

        # Main centered card
        container = tk.Frame(
            self.login_frame,
            bg="white"
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=760,
            height=480
        )

        # ----------------------------------------------------
        # Left branding section
        # ----------------------------------------------------

        left = tk.Frame(
            container,
            bg="#263238",
            width=300
        )

        left.pack(
            side="left",
            fill="y"
        )

        left.pack_propagate(False)

        tk.Label(
            left,
            text="AttendX",
            font=("Segoe UI", 34, "bold"),
            bg="#263238",
            fg="white"
        ).pack(
            pady=(80, 5)
        )

        tk.Label(
            left,
            text="Next-Gen Attendance System",
            font=("Segoe UI", 15),
            bg="#263238",
            fg="#CFD8DC",
            justify="center"
        ).pack(pady=10)

        tk.Label(
            left,
            text="Secure attendance management\nfor your classroom.",
            font=("Segoe UI", 10),
            bg="#263238",
            fg="#B0BEC5",
            justify="center"
        ).pack(pady=25)

        # ----------------------------------------------------
        # Right login section
        # ----------------------------------------------------

        right = tk.Frame(
            container,
            bg="white"
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=45,
            pady=40
        )

        tk.Label(
            right,
            text="Welcome Back",
            font=("Segoe UI", 24, "bold"),
            bg="white",
            fg="#263238"
        ).pack(anchor="w")

        tk.Label(
            right,
            text="Login with your registered administrator account.",
            font=("Segoe UI", 10),
            bg="white",
            fg="#78909C"
        ).pack(
            anchor="w",
            pady=(5, 25)
        )

        tk.Label(
            right,
            text="Username",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).pack(anchor="w")

        self.username_entry_login = tk.Entry(
            right,
            font=("Segoe UI", 12),
            relief="solid",
            bd=1
        )

        self.username_entry_login.pack(
            fill="x",
            ipady=8,
            pady=(5, 15)
        )

        tk.Label(
            right,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).pack(anchor="w")

        self.password_entry_login = tk.Entry(
            right,
            font=("Segoe UI", 12),
            show="*",
            relief="solid",
            bd=1
        )

        self.password_entry_login.pack(
            fill="x",
            ipady=8,
            pady=(5, 22)
        )

        login_button = tk.Button(
            right,
            text="LOGIN",
            command=self.login,
            font=("Segoe UI", 11, "bold"),
            bg="#1565C0",
            fg="white",
            activebackground="#0D47A1",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=11
        )

        login_button.pack(
            fill="x"
        )

        register_button = tk.Button(
            right,
            text="Create New Account",
            command=self.register,
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#1565C0",
            activebackground="white",
            activeforeground="#0D47A1",
            relief="flat",
            cursor="hand2"
        )

        register_button.pack(
            pady=(18, 0)
        )

        self.password_entry_login.bind(
            "<Return>",
            lambda event: self.login()
        )

    # ========================================================
    # REGISTER SCREEN
    # ========================================================

    def create_register_screen(self):

        container = tk.Frame(
            self.register_frame,
            bg="white"
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=760,
            height=520
        )

        # Header
        header = tk.Frame(
            container,
            bg="#263238",
            height=100
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Create Administrator Account",
            font=("Segoe UI", 23, "bold"),
            bg="#263238",
            fg="white"
        ).pack(
            pady=(24, 2)
        )

        tk.Label(
            header,
            text="Register first, then login with your credentials",
            font=("Segoe UI", 10),
            bg="#263238",
            fg="#CFD8DC"
        ).pack()

        # Form
        form = tk.Frame(
            container,
            bg="white"
        )

        form.pack(
            fill="both",
            expand=True,
            padx=90,
            pady=25
        )

        def create_field(label_text, password=False):

            tk.Label(
                form,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg="white",
                fg="#455A64"
            ).pack(
                anchor="w",
                pady=(5, 3)
            )

            entry = tk.Entry(
                form,
                font=("Segoe UI", 11),
                relief="solid",
                bd=1
            )

            if password:
                entry.config(show="*")

            entry.pack(
                fill="x",
                ipady=7
            )

            return entry

        self.register_name_entry = create_field(
            "Full Name"
        )

        self.username_entry_reg = create_field(
            "Username"
        )

        self.password_entry_reg = create_field(
            "Password",
            password=True
        )

        buttons = tk.Frame(
            form,
            bg="white"
        )

        buttons.pack(
            fill="x",
            pady=20
        )

        register_button = tk.Button(
            buttons,
            text="REGISTER",
            command=self.register_user,
            font=("Segoe UI", 10, "bold"),
            bg="#1565C0",
            fg="white",
            activebackground="#0D47A1",
            relief="flat",
            cursor="hand2",
            pady=10
        )

        register_button.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 6)
        )

        back_button = tk.Button(
            buttons,
            text="BACK TO LOGIN",
            command=self.close_register_window,
            font=("Segoe UI", 10, "bold"),
            bg="#ECEFF1",
            fg="#263238",
            activebackground="#CFD8DC",
            relief="flat",
            cursor="hand2",
            pady=10
        )

        back_button.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(6, 0)
        )

    # ========================================================
    # DASHBOARD
    # ========================================================

    def create_dashboard(self):

        # Sidebar
        sidebar = tk.Frame(
            self.main_frame,
            bg="#263238",
            width=235
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="AttendX",
            font=("Segoe UI", 27, "bold"),
            bg="#263238",
            fg="white"
        ).pack(
            pady=(25, 0)
        )

        tk.Label(
            sidebar,
            text="Next-Gen Attendance System",
            font=("Segoe UI", 9),
            bg="#263238",
            fg="#B0BEC5",
            justify="center"
        ).pack(
            pady=(0, 20)
        )

        # Dashboard menu
        self.make_sidebar_button(
            sidebar,
            "Dashboard",
            self.refresh_dashboard
        )

        self.make_sidebar_button(
            sidebar,
            "Students",
            self.show_students
        )

        self.make_sidebar_button(
            sidebar,
            "Capture Faces",
            self.capture_faces
        )

        self.make_sidebar_button(
            sidebar,
            "Train Model",
            self.train_images
        )

        self.make_sidebar_button(
            sidebar,
            "Recognize Attendance",
            self.recognize_attendance
        )

        self.make_sidebar_button(
            sidebar,
            "Attendance",
            self.show_attendance
        )

        self.make_sidebar_button(
            sidebar,
            "Reports",
            self.show_attendance
        )

        self.make_sidebar_button(
            sidebar,
            "Mail",
            self.auto_mail
        )

        self.make_sidebar_button(
            sidebar,
            "Check Camera",
            self.check_camera
        )

        # Spacer
        tk.Frame(
            sidebar,
            bg="#263238"
        ).pack(
            fill="both",
            expand=True
        )

        # Logout
        self.make_sidebar_button(
            sidebar,
            "Logout",
            self.logout
        )

        # Exit
        exit_button = tk.Button(
            sidebar,
            text="Exit",
            command=self.close_app,
            font=("Segoe UI", 10, "bold"),
            bg="#B71C1C",
            fg="white",
            activebackground="#C62828",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            pady=9
        )

        exit_button.pack(
            fill="x",
            padx=16,
            pady=(3, 18)
        )

        # Dashboard content
        self.dashboard_content = tk.Frame(
            self.main_frame,
            bg="#F4F6F8"
        )

        self.dashboard_content.pack(
            side="right",
            fill="both",
            expand=True
        )

    # ========================================================
    # DASHBOARD DATA
    # ========================================================

    def read_students(self):

        try:

            import pandas as pd

            if not os.path.isfile(STUDENT_CSV):
                return pd.DataFrame()

            dataframe = pd.read_csv(
                STUDENT_CSV
            )

            return dataframe

        except Exception as error:

            print(
                f"Student data error: {error}"
            )

            return None

    def get_today_attendance(self):

        try:

            import pandas as pd

            today = datetime.now().strftime(
                "%Y-%m-%d"
            )

            files = []

            for filename in os.listdir(
                ATTENDANCE_DIR
            ):

                if (
                    filename.lower().endswith(".xlsx")
                    and today in filename
                ):

                    files.append(
                        os.path.join(
                            ATTENDANCE_DIR,
                            filename
                        )
                    )

            if not files:
                return pd.DataFrame()

            dataframes = []

            for file_path in sorted(
                files,
                reverse=True
            ):

                try:

                    dataframe = pd.read_excel(
                        file_path
                    )

                    dataframes.append(
                        dataframe
                    )

                except Exception as error:

                    print(
                        f"Could not read {file_path}: {error}"
                    )

            if not dataframes:
                return pd.DataFrame()

            return pd.concat(
                dataframes,
                ignore_index=True
            )

        except Exception as error:

            print(
                f"Attendance data error: {error}"
            )

            return None

    # ========================================================
    # STAT CARD
    # ========================================================

    def create_stat_card(
        self,
        parent,
        title,
        value,
        column
    ):

        card = tk.Frame(
            parent,
            bg="white",
            highlightthickness=1,
            highlightbackground="#E0E0E0"
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=7
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#78909C"
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 4)
        )

        tk.Label(
            card,
            text=str(value),
            font=("Segoe UI", 26, "bold"),
            bg="white",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 18)
        )

    # ========================================================
    # DASHBOARD
    # ========================================================

    def refresh_dashboard(self):

        self.hide_all_frames()

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        for widget in self.dashboard_content.winfo_children():
            widget.destroy()

        students = self.read_students()
        attendance = self.get_today_attendance()

        if students is None:
            total_students = 0
        else:
            total_students = len(students)

        if attendance is None:
            present = 0
        else:
            if attendance.empty:
                present = 0
            elif "Id" in attendance.columns:
                present = attendance["Id"].astype(
                    str
                ).nunique()
            elif "Name" in attendance.columns:
                present = attendance["Name"].astype(
                    str
                ).nunique()
            else:
                present = len(attendance)

        if total_students > 0:
            present = min(
                present,
                total_students
            )

        absent = max(
            total_students - present,
            0
        )

        if total_students > 0:
            percentage = (
                present /
                total_students
            ) * 100
        else:
            percentage = 0

        # ----------------------------------------------------
        # Header
        # ----------------------------------------------------

        top = tk.Frame(
            self.dashboard_content,
            bg="#F4F6F8"
        )

        top.pack(
            fill="x",
            padx=28,
            pady=(25, 10)
        )

        tk.Label(
            top,
            text="Dashboard",
            font=("Segoe UI", 27, "bold"),
            bg="#F4F6F8",
            fg="#263238"
        ).pack(
            side="left"
        )

        user_text = (
            f"Welcome, {self.current_user}"
            if self.current_user
            else "Welcome"
        )

        tk.Label(
            top,
            text=user_text,
            font=("Segoe UI", 10),
            bg="#F4F6F8",
            fg="#78909C"
        ).pack(
            side="right",
            pady=10
        )

        # ----------------------------------------------------
        # Statistics
        # ----------------------------------------------------

        stats = tk.Frame(
            self.dashboard_content,
            bg="#F4F6F8"
        )

        stats.pack(
            fill="x",
            padx=28,
            pady=12
        )

        for column in range(4):
            stats.columnconfigure(
                column,
                weight=1
            )

        self.create_stat_card(
            stats,
            "TOTAL STUDENTS",
            total_students,
            0
        )

        self.create_stat_card(
            stats,
            "PRESENT TODAY",
            present,
            1
        )

        self.create_stat_card(
            stats,
            "ABSENT TODAY",
            absent,
            2
        )

        self.create_stat_card(
            stats,
            "ATTENDANCE",
            f"{percentage:.1f}%",
            3
        )

        # ----------------------------------------------------
        # Quick actions
        # ----------------------------------------------------

        quick = tk.Frame(
            self.dashboard_content,
            bg="white"
        )

        quick.pack(
            fill="x",
            padx=35,
            pady=20
        )

        tk.Label(
            quick,
            text="Quick Actions",
            font=("Segoe UI", 15, "bold"),
            bg="white",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 10)
        )

        action_row = tk.Frame(
            quick,
            bg="white"
        )

        action_row.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        actions = [
            (
                "Capture New Student",
                self.capture_faces
            ),
            (
                "Train Recognition Model",
                self.train_images
            ),
            (
                "Mark Attendance",
                self.recognize_attendance
            ),
            (
                "Check Camera",
                self.check_camera
            )
        ]

        for text, command in actions:

            button = tk.Button(
                action_row,
                text=text,
                command=command,
                font=("Segoe UI", 10, "bold"),
                bg="#ECEFF1",
                fg="#263238",
                activebackground="#CFD8DC",
                relief="flat",
                cursor="hand2",
                padx=14,
                pady=10
            )

            button.pack(
                side="left",
                padx=5
            )

        # ----------------------------------------------------
        # Recent attendance
        # ----------------------------------------------------

        recent = tk.Frame(
            self.dashboard_content,
            bg="white"
        )

        recent.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 25)
        )

        tk.Label(
            recent,
            text="Recent Attendance",
            font=("Segoe UI", 15, "bold"),
            bg="white",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 8)
        )

        tree_frame = tk.Frame(
            recent,
            bg="white"
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "Name",
            "ID",
            "Time"
        )

        tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            height=7
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=180
            )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            tree_frame,
            orient="vertical",
            command=tree.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        if (
            attendance is not None
            and not attendance.empty
        ):

            for _, row in attendance.tail(10).iloc[::-1].iterrows():

                name = str(
                    row.get(
                        "Name",
                        "Unknown"
                    )
                )

                student_id = str(
                    row.get(
                        "Id",
                        ""
                    )
                )

                time_value = str(
                    row.get(
                        "Time",
                        row.get(
                            "Date",
                            ""
                        )
                    )
                )

                tree.insert(
                    "",
                    "end",
                    values=(
                        name,
                        student_id,
                        time_value
                    )
                )

    # ========================================================
    # STUDENTS
    # ========================================================

    def show_students(self):

        self.hide_all_frames()

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        for widget in self.dashboard_content.winfo_children():
            widget.destroy()

        tk.Label(
            self.dashboard_content,
            text="Students",
            font=("Segoe UI", 27, "bold"),
            bg="#F4F6F8",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=28,
            pady=(25, 15)
        )

        container = tk.Frame(
            self.dashboard_content,
            bg="white"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 30)
        )

        tree_frame = tk.Frame(
            container,
            bg="white"
        )

        tree_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        students = self.read_students()

        if (
            students is None
            or students.empty
        ):

            tk.Label(
                tree_frame,
                text="No student records found.",
                font=("Segoe UI", 12),
                bg="white",
                fg="#78909C"
            ).pack(
                pady=40
            )

            return

        columns = list(
            students.columns
        )

        tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=150
            )

        for _, row in students.iterrows():

            values = []

            for column in columns:

                values.append(
                    str(
                        row.get(
                            column,
                            ""
                        )
                    )
                )

            tree.insert(
                "",
                "end",
                values=values
            )

        tree.pack(
            fill="both",
            expand=True
        )

    # ========================================================
    # ATTENDANCE
    # ========================================================

    def show_attendance(self):

        self.hide_all_frames()

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        for widget in self.dashboard_content.winfo_children():
            widget.destroy()

        tk.Label(
            self.dashboard_content,
            text="Attendance Records",
            font=("Segoe UI", 27, "bold"),
            bg="#F4F6F8",
            fg="#263238"
        ).pack(
            anchor="w",
            padx=28,
            pady=(25, 15)
        )

        container = tk.Frame(
            self.dashboard_content,
            bg="white"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 30)
        )

        files = []

        for filename in os.listdir(
            ATTENDANCE_DIR
        ):

            if filename.lower().endswith(
                ".xlsx"
            ):

                files.append(
                    os.path.join(
                        ATTENDANCE_DIR,
                        filename
                    )
                )

        files.sort(
            reverse=True
        )

        if not files:

            tk.Label(
                container,
                text="No attendance files found.",
                font=("Segoe UI", 12),
                bg="white",
                fg="#78909C"
            ).pack(
                pady=40
            )

            return

        selected_file = files[0]

        try:

            import pandas as pd

            dataframe = pd.read_excel(
                selected_file
            )

            columns = list(
                dataframe.columns
            )

            tree = ttk.Treeview(
                container,
                columns=columns,
                show="headings"
            )

            for column in columns:

                tree.heading(
                    column,
                    text=column
                )

                tree.column(
                    column,
                    width=160
                )

            for _, row in dataframe.iterrows():

                values = []

                for column in columns:

                    values.append(
                        str(
                            row.get(
                                column,
                                ""
                            )
                        )
                    )

                tree.insert(
                    "",
                    "end",
                    values=values
                )

            tree.pack(
                fill="both",
                expand=True,
                padx=20,
                pady=20
            )

            tk.Label(
                container,
                text=(
                    "Showing: "
                    + os.path.basename(
                        selected_file
                    )
                ),
                font=("Segoe UI", 9),
                bg="white",
                fg="#78909C"
            ).pack(
                pady=(0, 12)
            )

        except Exception as error:

            messagebox.showerror(
                "Attendance Error",
                str(error)
            )

    # ========================================================
    # CAPTURE SCREEN
    # ========================================================

    def create_capture_screen(self):

        frame = self.capture_face_frame

        header = tk.Frame(
            frame,
            bg="#263238",
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="CAPTURE STUDENT FACES",
            font=("Segoe UI", 22, "bold"),
            bg="#263238",
            fg="white"
        ).pack(
            pady=24
        )

        content = tk.Frame(
            frame,
            bg="#F4F6F8"
        )

        content.pack(
            fill="both",
            expand=True
        )

        form = tk.Frame(
            content,
            bg="white"
        )

        form.place(
            relx=0.5,
            rely=0.48,
            anchor="center",
            width=520,
            height=430
        )

        tk.Label(
            form,
            text="Student Information",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#263238"
        ).pack(
            pady=(25, 20)
        )

        def create_field(label_text):

            tk.Label(
                form,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg="white",
                fg="#455A64"
            ).pack(
                anchor="w",
                padx=55,
                pady=(5, 3)
            )

            entry = tk.Entry(
                form,
                font=("Segoe UI", 11),
                relief="solid",
                bd=1
            )

            entry.pack(
                fill="x",
                padx=55,
                ipady=6
            )

            return entry

        self.id_entry = create_field(
            "Student ID"
        )

        self.name_entry = create_field(
            "Name"
        )

        self.rollno_entry = create_field(
            "Roll Number"
        )

        self.email_entry = create_field(
            "Email"
        )

        buttons = tk.Frame(
            form,
            bg="white"
        )

        buttons.pack(
            fill="x",
            padx=55,
            pady=20
        )

        tk.Button(
            buttons,
            text="TAKE 100 IMAGES",
            command=self.take_images,
            font=("Segoe UI", 10, "bold"),
            bg="#1565C0",
            fg="white",
            activebackground="#0D47A1",
            relief="flat",
            cursor="hand2",
            pady=10
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 6)
        )

        tk.Button(
            buttons,
            text="BACK",
            command=self.close_capture_window,
            font=("Segoe UI", 10, "bold"),
            bg="#ECEFF1",
            fg="#263238",
            activebackground="#CFD8DC",
            relief="flat",
            cursor="hand2",
            pady=10
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(6, 0)
        )

    # ========================================================
    # MAIL SCREEN
    # ========================================================

    def create_mail_screen(self):

        frame = self.auto_mail_frame

        header = tk.Frame(
            frame,
            bg="#263238",
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="SEND ATTENDANCE REPORT",
            font=("Segoe UI", 22, "bold"),
            bg="#263238",
            fg="white"
        ).pack(
            pady=24
        )

        content = tk.Frame(
            frame,
            bg="#F4F6F8"
        )

        content.pack(
            fill="both",
            expand=True
        )

        form = tk.Frame(
            content,
            bg="white"
        )

        form.place(
            relx=0.5,
            rely=0.48,
            anchor="center",
            width=650,
            height=430
        )

        tk.Label(
            form,
            text="Email Settings",
            font=("Segoe UI", 18, "bold"),
            bg="white",
            fg="#263238"
        ).pack(
            pady=(25, 20)
        )

        def create_field(
            label_text,
            show=None
        ):

            tk.Label(
                form,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg="white",
                fg="#455A64"
            ).pack(
                anchor="w",
                padx=55,
                pady=(5, 3)
            )

            entry = tk.Entry(
                form,
                font=("Segoe UI", 11),
                relief="solid",
                bd=1,
                show=show
            )

            entry.pack(
                fill="x",
                padx=55,
                ipady=6
            )

            return entry

        self.sender_email_entry = create_field(
            "Sender Email"
        )

        self.sender_pass_entry = create_field(
            "Sender Password",
            show="*"
        )

        self.attechment_entry = create_field(
            "Attendance File Path"
        )

        buttons = tk.Frame(
            form,
            bg="white"
        )

        buttons.pack(
            fill="x",
            padx=55,
            pady=20
        )

        tk.Button(
            buttons,
            text="BROWSE",
            command=self.browse_file,
            font=("Segoe UI", 10, "bold"),
            bg="#ECEFF1",
            fg="#263238",
            relief="flat",
            cursor="hand2",
            pady=9
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5)
        )

        tk.Button(
            buttons,
            text="SEND EMAIL",
            command=self.send_email,
            font=("Segoe UI", 10, "bold"),
            bg="#1565C0",
            fg="white",
            relief="flat",
            cursor="hand2",
            pady=9
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        tk.Button(
            buttons,
            text="BACK",
            command=self.close_window_mail,
            font=("Segoe UI", 10, "bold"),
            bg="#ECEFF1",
            fg="#263238",
            relief="flat",
            cursor="hand2",
            pady=9
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(5, 0)
        )

    # ========================================================
    # EXISTING PROJECT MODULES
    # ========================================================

    def check_camera(self):

        try:

            import check_camera

            check_camera.camer()

        except Exception as error:

            messagebox.showerror(
                "Camera Error",
                str(error)
            )

    def capture_faces(self):

        self.hide_all_frames()

        self.capture_face_frame.pack(
            fill="both",
            expand=True
        )

    def take_images(self):

        try:

            import Capture_Image

            Capture_Image.take_image(
                self
            )

        except Exception as error:

            messagebox.showerror(
                "Capture Error",
                str(error)
            )

    def close_capture_window(self):

        self.hide_all_frames()

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.refresh_dashboard()

    def train_images(self):

        try:

            import Train_Image

            Train_Image.traingui()

            self.refresh_dashboard()

        except Exception as error:

            messagebox.showerror(
                "Training Error",
                str(error)
            )

    def recognize_attendance(self):

        try:

            import Recognize

            Recognize.recognize_attendence()

            self.refresh_dashboard()

        except Exception as error:

            messagebox.showerror(
                "Recognition Error",
                str(error)
            )

    # ========================================================
    # MAIL
    # ========================================================

    def auto_mail(self):

        self.hide_all_frames()

        self.auto_mail_frame.pack(
            fill="both",
            expand=True
        )

    def browse_file(self):

        try:

            import automail

            automail.browse_file(
                self
            )

        except Exception as error:

            messagebox.showerror(
                "Mail Error",
                str(error)
            )

    def send_email(self):

        try:

            import automail

            automail.send_email(
                self
            )

        except Exception as error:

            messagebox.showerror(
                "Mail Error",
                str(error)
            )

    def close_window_mail(self):

        self.hide_all_frames()

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.refresh_dashboard()

    # ========================================================
    # AUTHENTICATION - LOAD USERS
    # ========================================================

    def load_users(self):

        try:

            with open(
                AUTH_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                users = json.load(
                    file
                )

                if isinstance(
                    users,
                    dict
                ):

                    return users

                return {}

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return {}

        except Exception as error:

            messagebox.showerror(
                "Authentication Error",
                f"Could not read user data:\n{error}"
            )

            return {}

    # ========================================================
    # AUTHENTICATION - SAVE USERS
    # ========================================================

    def save_users(
        self,
        users
    ):

        with open(
            AUTH_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                users,
                file,
                indent=4
            )

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        username = (
            self.username_entry_login
            .get()
            .strip()
        )

        password = (
            self.password_entry_login
            .get()
        )

        if not username or not password:

            messagebox.showerror(
                "Login Error",
                "Please enter username and password."
            )

            return

        users = self.load_users()

        if (
            username in users
            and users[username].get(
                "password"
            ) == password
        ):

            self.current_user = (
                users[username].get(
                    "name",
                    username
                )
            )

            self.username_entry_login.delete(
                0,
                tk.END
            )

            self.password_entry_login.delete(
                0,
                tk.END
            )

            self.main_page()

        else:

            messagebox.showerror(
                "Login Error",
                "Invalid username or password."
            )

    # ========================================================
    # OPEN REGISTER SCREEN
    # ========================================================

    def register(self):

        self.hide_all_frames()

        self.register_frame.pack(
            fill="both",
            expand=True
        )

        self.register_name_entry.focus_set()

    # ========================================================
    # BACK TO LOGIN
    # ========================================================

    def close_register_window(self):

        self.hide_all_frames()

        self.show_login()

    # ========================================================
    # REGISTER USER
    # ========================================================

    def register_user(self):

        name = (
            self.register_name_entry
            .get()
            .strip()
        )

        username = (
            self.username_entry_reg
            .get()
            .strip()
        )

        password = (
            self.password_entry_reg
            .get()
        )

        # ----------------------------------------------------
        # Validate fields
        # ----------------------------------------------------

        if (
            not name
            or not username
            or not password
        ):

            messagebox.showerror(
                "Registration Error",
                "Please fill in all fields."
            )

            return

        # ----------------------------------------------------
        # Load current users
        # ----------------------------------------------------

        users = self.load_users()

        # ----------------------------------------------------
        # Check duplicate username
        # ----------------------------------------------------

        if username in users:

            messagebox.showerror(
                "Registration Error",
                "Username already taken."
            )

            return

        # ----------------------------------------------------
        # Add new user
        # ----------------------------------------------------

        users[username] = {
            "name": name,
            "password": password
        }

        # ----------------------------------------------------
        # Save
        # ----------------------------------------------------

        try:

            self.save_users(
                users
            )

        except Exception as error:

            messagebox.showerror(
                "Registration Error",
                f"Could not save account:\n{error}"
            )

            return

        # ----------------------------------------------------
        # Clear form
        # ----------------------------------------------------

        self.register_name_entry.delete(
            0,
            tk.END
        )

        self.username_entry_reg.delete(
            0,
            tk.END
        )

        self.password_entry_reg.delete(
            0,
            tk.END
        )

        # ----------------------------------------------------
        # IMPORTANT:
        # Do NOT automatically login.
        # Return to LOGIN screen.
        # ----------------------------------------------------

        messagebox.showinfo(
            "Registration Successful",
            "User registered successfully.\n\n"
            "Please login with your new credentials."
        )

        self.show_login()

    # ========================================================
    # DASHBOARD AFTER LOGIN
    # ========================================================

    def main_page(self):

        self.hide_all_frames()

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        self.refresh_dashboard()

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):

        self.current_user = None

        self.hide_all_frames()

        self.show_login()

    # ========================================================
    # EXIT APPLICATION
    # ========================================================

    def close_app(self):

        self.master.destroy()


# ============================================================
# APPLICATION START
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = Login(
        root
    )

    root.mainloop()












# import automail
# import json
# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import os

# # file_path = "D:/Face-Recognition-Attendance-Application/StudentDetails/NewRegisterInfo.json"
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# student_details_dir = os.path.join(BASE_DIR, "StudentDetails")
# os.makedirs(student_details_dir, exist_ok=True)

# file_path = os.path.join(
#     student_details_dir,
#     "NewRegisterInfo.json"
# )

# try:
#     if not os.path.isfile(file_path):
#         with open(file_path, 'w') as f:
#             json.dump({}, f)

#     # Load user data from file
#     with open(file_path, "r") as f:
#         users = json.load(f)

# except PermissionError:
#     print("Error: Permission denied. Check file permissions or run the program with administrator privileges.")

# except Exception as e:
#     print(f"Error: {e}")
#     users = {}


# class Login:
#     def __init__(self, master):
#         self.master = master
#         self.master.bind("<Configure>", self.on_resize)  # bind the resize event to the on_resize method
#         self.login_frame = tk.Frame(self.master)
#         self.register_frame = tk.Frame(self.master)
#         self.main_frame = tk.Frame(self.master)
#         self.capture_face_frame = tk.Frame(self.master)
#         self.auto_mail_frame = tk.Frame(self.master)

#         self.create_widgets()
#         self.master.geometry("1000x600")

#     def create_widgets(self):
#         ################################# Login Frame ##############################################################
#         # Create header frame
#         header_frame = tk.Frame(self.login_frame, bg="#333333", height=80)
#         header_frame.pack(fill="x")

#         # Add header label
#         header_label = tk.Label(header_frame, text="LOGIN", fg="#333333", font=("Arial", 24), padx=450)
#         header_label.pack(side="left", pady=10)

#         # Create sidebar frame
#         sidebar_frame = tk.Frame(self.login_frame, bg="#444444", width=200)
#         sidebar_frame.pack(side="left", fill="y")

#         # Add sidebar buttons
#         # Login Button
#         self.login_button = tk.Button(sidebar_frame, text="Login", command=self.login,
#                                       borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
#         self.login_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Check Camera button
#         self.login_button.bind("<Enter>", lambda k: self.login_button.config(bg="#8D918D"))
#         self.login_button.bind("<Leave>", lambda k: self.login_button.config(bg="#555555"))

#         # Register Button
#         self.register_login_button = tk.Button(sidebar_frame, text="Register", command=self.register,
#                                                borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
#                                                pady=10)
#         self.register_login_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Capture Faces button
#         self.register_login_button.bind("<Enter>", lambda k: self.register_login_button.config(bg="#8D918D"))
#         self.register_login_button.bind("<Leave>", lambda k: self.register_login_button.config(bg="#555555"))

#         # Create main frame
#         main_frame = tk.Frame(self.login_frame, bg="#CECECE")
#         main_frame.pack(side="right", fill="both", expand=True)

#         # Add sidebar buttons

#         self.username_label_login = tk.Label(main_frame, text="Enter Username: ", fg="black", font=("Helvetica", 14))
#         self.username_label_login.pack(side="top", pady=10, padx=10, fill="y")
#         self.username_entry_login = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.username_entry_login.pack(side="top", pady=10, padx=10, fill="y")

#         self.password_label_login = tk.Label(main_frame, text="Enter Password", fg="black", font=("Helvetica", 14))
#         self.password_label_login.pack(side="top", pady=10, padx=10, fill="y")
#         self.password_entry_login = tk.Entry(main_frame, font=("Helvetica", 14), show="*")
#         self.password_entry_login.pack(side="top", pady=10, padx=10, fill="y")

#         ################################# Register Frame ##############################################################

#         # Create header frame
#         header_frame = tk.Frame(self.register_frame, bg="#333333", height=80)
#         header_frame.pack(fill="x")

#         # Add header label
#         header_label = tk.Label(header_frame, text="REGISTRATION", fg="#333333", font=("Arial", 24), padx=400)
#         header_label.pack(side="left", pady=10)

#         # Create sidebar frame
#         sidebar_frame = tk.Frame(self.register_frame, bg="#444444", width=200)
#         sidebar_frame.pack(side="left", fill="y")

#         # Add sidebar buttons
#         # New Register Button
#         self.new_register_button = tk.Button(sidebar_frame, text="Register", command=self.register_user,
#                                              borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
#                                              pady=10)
#         self.new_register_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Check Camera button
#         self.new_register_button.bind("<Enter>", lambda e: self.new_register_button.config(bg="#8D918D"))
#         self.new_register_button.bind("<Leave>", lambda e: self.new_register_button.config(bg="#555555"))

#         # Back Button
#         self.register_back_button = tk.Button(sidebar_frame, text="Back", command=self.close_register_window,
#                                               borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
#                                               pady=10)
#         self.register_back_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Capture Faces button
#         self.register_back_button.bind("<Enter>", lambda e: self.register_back_button.config(bg="#8D918D"))
#         self.register_back_button.bind("<Leave>", lambda e: self.register_back_button.config(bg="#555555"))

#         # Create main frame
#         main_frame = tk.Frame(self.register_frame, bg="#CECECE")
#         main_frame.pack(side="right", fill="both", expand=True)

#         # Add sidebar buttons

#         self.register_name_label = tk.Label(main_frame, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
#         self.register_name_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.register_name_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.register_name_entry.pack(side="top", pady=10, padx=10, fill="y")

#         self.username_label_reg = tk.Label(main_frame, text="Enter Your Username", fg="black", font=("Helvetica", 14))
#         self.username_label_reg.pack(side="top", pady=10, padx=10, fill="y")
#         self.username_entry_reg = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.username_entry_reg.pack(side="top", pady=10, padx=10, fill="y")

#         self.password_label_reg = tk.Label(main_frame, text="Enter Your Password", fg="black", font=("Helvetica", 14))
#         self.password_label_reg.pack(side="top", pady=10, padx=10, fill="y")
#         self.password_entry_reg = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.password_entry_reg.pack(side="top", pady=10, padx=10, fill="y")

#         ################################# Main Frame ##############################################################

#         # Create header frame
#         header_frame = tk.Frame(self.main_frame, bg="#333333", height=80)
#         header_frame.pack(fill="x")

#         # Add header label
#         header_label = tk.Label(header_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM", fg="#333333",
#                                 font=("Arial", 24), padx=240)
#         header_label.pack(side="left", pady=10)

#         # Create sidebar frame
#         sidebar_frame = tk.Frame(self.main_frame, bg="#444444", width=200)
#         sidebar_frame.pack(side="left", fill="y")

#         # Add sidebar buttons
#         buttons = {
#             "Check Camera": self.check_camera,
#             "Capture Faces": self.capture_faces,
#             "Train Images": self.train_images,
#             "Recognize & Attendance": self.recognize_attendance,
#             "Mail": self.auto_mail,
#             "Exit": self.close_app
#         }

#         for button_text, command_func in buttons.items():
#             button = tk.Button(sidebar_frame, text=button_text, command=command_func,
#                                borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
#             button.pack(side="top", pady=10, padx=10, fill="x")
#             # Bind the hover effect to the button
#             button.bind("<Enter>", lambda e, b=button: b.config(bg="#8D918D"))
#             button.bind("<Leave>", lambda e, b=button: b.config(bg="#555555"))

#         # Create main frame
#         main_frame = tk.Frame(self.main_frame, bg="#FFFFFF")
#         main_frame.pack(side="right", fill="both", expand=True)

#         # Load the background image
#         self.image = Image.open("facial-recognition-face-recognition.jpg")
#         # Resize the image to 800x600
#         # self.image = self.image.resize((800, 600), resample=Image.LANCZOS)
#         self.background_image = ImageTk.PhotoImage(self.image)
#         # Create a label for the background image
#         self.background_label = tk.Label(main_frame, image=self.background_image, bg="SystemButtonFace")
#         self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

#         ######################################### Capture Face Frame ####################################################################

#         # Create header frame
#         header_frame = tk.Frame(self.capture_face_frame, bg="#333333", height=80)
#         header_frame.pack(fill="x")

#         # Add header label
#         header_label = tk.Label(header_frame, text="CAPTURE IMAGES", fg="#333333", font=("Arial", 24), padx=360)
#         header_label.pack(side="left", pady=10)

#         # Create sidebar frame
#         sidebar_frame = tk.Frame(self.capture_face_frame, bg="#444444", width=200)
#         sidebar_frame.pack(side="left", fill="y")

#         # Add sidebar buttons
#         # Take Image Button
#         self.take_image_button = tk.Button(sidebar_frame, text="Take Images", command=self.take_images,
#                                            borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
#                                            pady=10)
#         self.take_image_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Check Camera button
#         self.take_image_button.bind("<Enter>", lambda e: self.take_image_button.config(bg="#8D918D"))
#         self.take_image_button.bind("<Leave>", lambda e: self.take_image_button.config(bg="#555555"))

#         # Back Button
#         self.capture_faces_back_button = tk.Button(sidebar_frame, text="Back", command=self.close_capture_window,
#                                                    borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
#                                                    pady=10)
#         self.capture_faces_back_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Capture Faces button
#         self.capture_faces_back_button.bind("<Enter>", lambda e: self.capture_faces_back_button.config(bg="#8D918D"))
#         self.capture_faces_back_button.bind("<Leave>", lambda e: self.capture_faces_back_button.config(bg="#555555"))

#         # Create main frame
#         main_frame = tk.Frame(self.capture_face_frame, bg="#CECECE")
#         main_frame.pack(side="right", fill="both", expand=True)

#         # Add sidebar buttons
#         self.id_label = tk.Label(main_frame, text="Enter Your Id: ", fg="black", font=("Helvetica", 14))
#         self.id_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.id_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.id_entry.pack(side="top", pady=10, padx=10, fill="y")

#         self.name_label = tk.Label(main_frame, text="Enter Your Name: ", fg="black", font=("Helvetica", 14))
#         self.name_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.name_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.name_entry.pack(side="top", pady=10, padx=10, fill="y")

#         self.rollno_label = tk.Label(main_frame, text="Enter Your Roll No.: ", fg="black", font=("Helvetica", 14))
#         self.rollno_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.rollno_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.rollno_entry.pack(side="top", pady=10, padx=10, fill="y")

#         self.email_label = tk.Label(main_frame, text="Enter Your Valid Email Id: ", fg="black", font=("Helvetica", 14))
#         self.email_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.email_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.email_entry.pack(side="top", pady=10, padx=10, fill="y")

#         ################################################### Auto Mail Frame #####################################################

#         # Create header frame
#         header_frame = tk.Frame(self.auto_mail_frame, bg="#333333", height=80)
#         header_frame.pack(fill="x")

#         # Add header label
#         header_label = tk.Label(header_frame, text="SENDING MAIL WITH ATTACHMENT", fg="#333333", font=("Arial", 24),
#                                 padx=360)
#         header_label.pack(side="left", pady=10)

#         # Create sidebar frame
#         sidebar_frame = tk.Frame(self.auto_mail_frame, bg="#444444", width=200)
#         sidebar_frame.pack(side="left", fill="y")

#         # Add sidebar buttons
#         # browse button
#         self.browse_file_button = tk.Button(sidebar_frame, text="Browse", command=self.browse_file, borderwidth=5,
#                                             font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
#         self.browse_file_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Check Camera button
#         self.browse_file_button.bind("<Enter>", lambda e: self.browse_file_button.config(bg="#8D918D"))
#         self.browse_file_button.bind("<Leave>", lambda e: self.browse_file_button.config(bg="#555555"))

#         # email button
#         self.send_email_button = tk.Button(sidebar_frame, text="Send Email", command=self.send_email, borderwidth=5,
#                                            font=("Arial", 16), bg="#555555", fg="white", padx=20, pady=10)
#         self.send_email_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Check Camera button
#         self.send_email_button.bind("<Enter>", lambda e: self.send_email_button.config(bg="#8D918D"))
#         self.send_email_button.bind("<Leave>", lambda e: self.send_email_button.config(bg="#555555"))

#         # Back Button
#         self.capture_faces_button = tk.Button(sidebar_frame, text="Back", command=self.close_window_mail,
#                                               borderwidth=5, font=("Arial", 16), bg="#555555", fg="white", padx=20,
#                                               pady=10)
#         self.capture_faces_button.pack(side="top", pady=10, padx=10, fill="x")
#         # Bind the hover effect to the Capture Faces button
#         self.capture_faces_button.bind("<Enter>", lambda e: self.capture_faces_button.config(bg="#8D918D"))
#         self.capture_faces_button.bind("<Leave>", lambda e: self.capture_faces_button.config(bg="#555555"))

#         # Create main frame
#         main_frame = tk.Frame(self.auto_mail_frame, bg="#CECECE")
#         main_frame.pack(side="right", fill="both", expand=True)

#         # Add sidebar buttons
#         # Create the label and entry for sender email
#         self.sender_email_label = tk.Label(main_frame, text="Enter Your Email ID: ", fg="black", font=("Helvetica", 14))
#         self.sender_email_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.sender_email_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.sender_email_entry.pack(side="top", pady=10, padx=10, fill="y")

#         # Create the label and entry for sender password
#         self.sender_pass_label = tk.Label(main_frame, text="Enter Your Password", fg="black", font=("Helvetica", 14))
#         self.sender_pass_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.sender_pass_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.sender_pass_entry.pack(side="top", pady=10, padx=10, fill="y")

#         # Create the label and entry for attachment file
#         self.attechment_label = tk.Label(main_frame, text="Enter the Attendance file Path", fg="black",
#                                          font=("Helvetica", 14))
#         self.attechment_label.pack(side="top", pady=10, padx=10, fill="y")
#         self.attechment_entry = tk.Entry(main_frame, font=("Helvetica", 14))
#         self.attechment_entry.pack(side="top", pady=10, padx=10, fill="y")

#         # By default
#         self.login_frame.pack()

#     # %%%%%%%%%%%%%%%%%%%%%%%%%%%% Function Start %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#     def on_resize(self, event):
#         """
#         Adjusts the frame size according to the window size
#         """
#         width = self.master.winfo_width()
#         height = self.master.winfo_height()
#         self.login_frame.config(width=width, height=height)
#         self.register_frame.config(width=width, height=height)
#         self.main_frame.config(width=width, height=height)
#         self.capture_face_frame.config(width=width, height=height)
#         self.auto_mail_frame.config(width=width, height=height)

#     # $$$$$$$$$$$$$$$$$$$$$$$$$$ Auto Mail Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     def browse_file(self):
#         automail.browse_file(self)

#     def send_email(self):
#         automail.send_email(self)

#     def close_window_mail(self):
#         self.auto_mail_frame.pack_forget()  # Hide login_frame
#         self.main_frame.pack()  # Show register_frame

#     # $$$$$$$$$$$$$$$$$$$$$$$$$$ Capture Images Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     def take_images(self):
#         import Capture_Image
#         Capture_Image.take_image(self)

#     def close_capture_window(self):
#         self.capture_face_frame.pack_forget()  # Hide login_frame
#         self.main_frame.pack()  # Show register_frame

#     # $$$$$$$$$$$$$$$$$$$$$$$$$$ Main Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     def check_camera(self):
#         import check_camera
#         check_camera.camer()

#     def capture_faces(self):
#         self.main_frame.pack_forget()  # Hide main frame
#         self.capture_face_frame.pack()  # Show capture face

#     def train_images(self):
#         import Train_Image
#         Train_Image.traingui()

#     def recognize_attendance(self):
#         import Recognize
#         Recognize.recognize_attendence()

#     def auto_mail(self):
#         self.main_frame.pack_forget()  # Hide login_frame
#         self.auto_mail_frame.pack()  # Show register_frame

#     def close_app(self):
#         # close the GUI
#         self.master.destroy()

#     # $$$$$$$$$$$$$$$$$$$$$$$$$$ Login Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     def main_page(self):
#         self.login_frame.pack_forget()  # Hide login_frame
#         self.main_frame.pack()  # Show register_frame

#     def login(self):
#         username = self.username_entry_login.get()
#         password = self.password_entry_login.get()

#         try:
#             with open(file_path, "r") as f:
#                 users = json.load(f)
#         except FileNotFoundError:
#             users = {}

#         # Check if username and password are correct
#         if username in users and users[username]['password'] == password:
#             self.main_page()
#         else:
#             tk.messagebox.showerror("Error", "Invalid username or password")

#     def register(self):
#         self.login_frame.pack_forget()  # Hide login_frame
#         self.register_frame.pack()  # Show register_frame

#         # Register new user

#     # $$$$$$$$$$$$$$$$$$$$$$$$$$ Register Functions $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#     def close_register_window(self):
#         self.register_frame.pack_forget()  # Hide login_frame
#         self.login_frame.pack()  # Show register_frame

#     def register_user(self):
#         name = self.register_name_entry.get()
#         username = self.username_entry_reg.get()
#         password = self.password_entry_reg.get()

#         # Check if all fields are filled
#         if name == '' or username == '' or password == '':
#             tk.messagebox.showerror("Error", "Please fill in all fields")
#             return

#         # Check if username is already taken
#         if username in users:
#             tk.messagebox.showerror("Error", "Username already taken")
#             return

#         # Add new user to dictionary of users
#         users[username] = {
#             'name': name,
#             'password': password
#         }

#         # Save updated user data to file
#         with open(file_path, "w") as f:
#             json.dump(users, f)

#         # Show success message
#         tk.messagebox.showinfo("Success", "User registered successfully")

#         # Clear the registration form
#         self.register_name_entry.delete(0, tk.END)
#         self.username_entry_reg.delete(0, tk.END)
#         self.password_entry_reg.delete(0, tk.END)


# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = Login(root)
#     root.mainloop()










