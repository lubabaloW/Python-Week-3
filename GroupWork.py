
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *
from customtkinter import CTk
import csv
import tkinter as tk
import re
import threading
from PIL import ImageTk, Image


class Main:
    def __init__(self):

        self.root = CTk()
        self.root.title("Welcome to Marking program")
        self.root.geometry('900x600')
        self.email_signup = CTkEntry(self.root, bg_color="gray")
        self.style = ttk.Style(self.root)
        self.image = Image.open("MARKOHOLIC.jpg")
        self.image = self.image.resize((300, 250))
        self.photo = ImageTk.PhotoImage(self.image)
        # Convert the Image object into a Tkinter PhotoImage object

        self.canvas = CTkCanvas(self.root, width=self.image.width, height=self.image.height, bg="gray")
        self.canvas.grid()

        # Add the image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

        self.password_signup1 = CTkEntry(self.root, show="*", bg_color="gray")
        self.password_signup2 = CTkEntry(self.root, show="*", bg_color="gray")
        self.email_signup.grid(row=1, column=1, padx=10, pady=10)
        self.password_signup1.grid(row=2, column=1, padx=10, pady=10)
        self.password_signup2.grid(row=3, column=1, padx=10, pady=10)
        self.root.config(bg="gray")
        self.lblemail = CTkLabel(self.root, text="Enter your email:", bg_color="gray")
        self.lblemail.grid(row=1, column=0, padx=10, pady=10)

        self.lblupassword = CTkLabel(self.root, text="Enter your password:", bg_color="gray")
        self.lblupassword.grid(row=2, column=0, padx=10, pady=10)
        self.lblupassword2 = CTkLabel(self.root, text="Confirm your password:", bg_color="gray")
        self.lblupassword2.grid(row=3, column=0, padx=10, pady=10)

        def loggedin():
            self.top = CTkToplevel()
            self.top.title("Log in")
            self.top.geometry('900x600')
            self.top.config(bg="gray")
            self.lblemaillog = CTkLabel(self.top, text="Enter your email:", bg_color="gray")
            self.lblemaillog.grid(row=1, column=0, padx=10, pady=10)
            self.lblupasswordlog = CTkLabel(self.top, text="Enter your password:", bg_color="gray")
            self.lblupasswordlog.grid(row=2, column=0, padx=10, pady=10)
            global email_login
            global password_login
            self.email_login = CTkEntry(self.top, bg_color="gray")
            self.password_login = CTkEntry(self.top, show="*", bg_color="gray")
            self.email_login.grid(row=1, column=1, padx=10, pady=10)
            self.password_login.grid(row=2, column=1, padx=10, pady=10)

            def login():
                global email
                self.email = self.email_login.get()
                self.password = self.password_login.get()
                with open("users.csv", mode="r") as f:
                    reader = csv.reader(f, delimiter=",")
                    for row in reader:
                        if row == [self.email, self.password]:
                            print("You logged in!")
                            self.top.withdraw()
                            mainmenu()
                            return True
                print("Please try again")
                return False

            self.btnlog = CTkButton(self.top, text="Login", fg_color="red", command=login)
            # set Button grid
            self.btnlog.grid(column=1, row=3)
            self.root.withdraw()

        def register():
            with open("users.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                self.email = self.email_signup.get()
                self.password = self.password_signup1.get()
                self.password2 = self.password_signup2.get()

                if not re.match(r"[^@]+@gmail\.com", self.email):
                    messagebox.showerror("Error", "Please enter a valid Gmail address.")
                    return

                if self.password == self.password2:
                    writer.writerow([self.email, self.password])
                    print("Registration is successful!")
                    loggedin()
                else:
                    messagebox.showerror("Error", "Passwords do not match")

        self.btn = CTkButton(self.root, text="Register", fg_color="red", command=register, bg_color="gray")
        # set Button grid
        self.btn.grid(column=1, row=5)
        self.btn_account = CTkButton(self.root, text="Already have an account?", command=loggedin, bg_color="gray")
        self.btn_account.grid(column=3, row=5)

        def mainmenu():
            self.menu = CTkToplevel()
            self.menu.title("Main menu")
            self.menu.geometry('900x600')
            self.menu.config(bg="gray")
            self.lbl_learners = CTkLabel(self.menu, text="WELCOME TO THE MARKOHOLIC GRADING SYSTEM", bg_color="gray")
            self.lbl_learners.grid(row=0, column=0, padx=10, pady=10)

            # GUI CODE

            def load_groups():
                # Read groups from groups.csv
                with open('groups.csv', 'r') as file:
                    reader = csv.reader(file)
                    groups = [row[1] for row in reader if row[0] == self.email]  # Filter out empty rows
                return groups

            def view_group_marks(group):
                self.view_marks_window = CTkToplevel()
                self.view_marks_window.title(f"Marks for {group}")
                self.view_marks_window.geometry('900x600')
                self.view_marks_window.config(bg="gray")
                # Load and display learner marks for the selected group
                with open("marks.csv", mode="r") as f:
                    reader = csv.reader(f, delimiter=",")
                    learner_marks = [row for row in reader if row[1] == group]

                for i, row in enumerate(learner_marks):
                    self.lbl_learners = CTkLabel(self.view_marks_window, text=f"{row[2]}: {row[3]}")
                    self.lbl_learners.grid(row=i, column=0, padx=10, pady=5)

                total_marks = 0
                num_learners = len(learner_marks)

                for row in learner_marks:
                    total_marks += int(row[3])

                if num_learners > 0:
                    average_mark = total_marks / num_learners
                    self.lbl_average = CTkLabel(self.view_marks_window, text=f"Average Mark: {average_mark:.2f}")
                    self.lbl_average.grid(pady=5)
                else:
                    self.lbl_no_data = CTkLabel(self.view_marks_window, text="No data available")
                    self.lbl_no_data.grid(pady=5)

            def view_groups():
                self.groups_window = CTkToplevel()
                self.groups_window.title("View Groups")
                self.groups_window.geometry('900x600')
                self.groups_window.config(bg="gray")
                self.menu.withdraw()
                # Load groups
                groups = load_groups()

                # Create buttons for each group
                for group in groups:
                    CTkButton(self.groups_window, text=group, command=lambda g=group: view_group_marks(g)).pack()

            def addgroupmenu():
                self.addgroups = CTkToplevel()
                self.addgroups.title("Add Group")
                self.addgroups.geometry('900x600')
                self.addgroups.config(bg="gray")
                self.lblgroupname = CTkLabel(self.addgroups, text="Enter your groups name:")
                self.lblgroupname.grid(row=1, column=0, padx=10, pady=10)
                self.group_name = CTkEntry(self.addgroups)
                self.group_name.grid(row=1, column=1, padx=10, pady=10)
                self.menu.withdraw()
                def addgroup():
                    with open("groups.csv", mode="a", newline="") as f:
                        writer = csv.writer(f, delimiter=",")
                        global group
                        self.group = self.group_name.get()
                        writer.writerow([self.email, self.group])
                        print("Group added successfully!")

                        def addlearners():

                            self.lbllearnername = CTkLabel(self.addgroups, text="Enter your learner name:")
                            self.lbllearnername.grid(row=1, column=0, padx=10, pady=10)
                            self.learner_name = CTkEntry(self.addgroups)
                            self.learner_name.grid(row=1, column=1, padx=10, pady=10)

                            def addlearner():
                                with open("learner.csv", mode="a", newline="") as f:
                                    writer = csv.writer(f, delimiter=",")
                                    global learner
                                    self.learner = self.learner_name.get()
                                    writer.writerow([self.email, self.group, self.learner])
                                    self.learner_name.delete(0, END)
                                    print("learner added successfully!")

                            def addmarks():
                                def submit_marks():
                                    # Get marks input and learner names
                                    marks = [entry.get() for entry in marks_entries]

                                    # Write marks to marks.csv
                                    with open('marks.csv', 'a', newline='') as file:
                                        writer = csv.writer(file)
                                        for name, mark in zip(learner_names, marks):
                                            writer.writerow([self.email, self.group, name, mark])
                                    messagebox.showinfo("Marks info:", "MARKS SUBMITTED")
                                    view_groups()

                                def create_text_boxes():
                                    global marks_entries
                                    marks_entries = []
                                    for i, name in enumerate(learner_names):
                                        tk.Label(self.addmarks, text=name).grid(row=i + 1, column=0)
                                        self.entry = CTkEntry(self.addmarks)
                                        self.entry.grid(row=i + 1, column=1)
                                        marks_entries.append(self.entry)

                                def filter_learner_data(email, group):
                                    with open('learner.csv', 'r') as file:
                                        reader = csv.reader(file)
                                        learner_data = [row for row in reader if row[0] == email and row[1] == group]
                                    return learner_data

                                # Get email and group of the current user (example values)
                                current_user_email = self.email
                                current_user_group = self.group

                                # Filter learner data based on user email and group
                                learner_data = filter_learner_data(current_user_email, current_user_group)

                                # Tkinter setup
                                self.addmarks = CTkToplevel()
                                self.addmarks.title("Add Marks")
                                self.addmarks.geometry('900x600')
                                self.addmarks.config(bg="gray")
                                # Create text boxes for marks

                                learner_names = [row[2] for row in learner_data]
                                create_text_boxes()

                                # Submit button
                                self.submit_button = CTkButton(self.addmarks, text="Submit Marks", command=submit_marks)
                                self.submit_button.grid(row=len(learner_names) + 1, column=0, columnspan=2)
                                self.btn_group_choose = CTkButton(self.addmarks, text="View groups", fg_color="red", command=view_groups)
                                self.btn_group_choose.grid(row=len(learner_names) + 1, column=4, columnspan=2)

                            self.btn_submit_learner = CTkButton(self.addgroups, text="Add learner", fg_color="red",
                                                                command=addlearner)
                            self.btn_submit_learner.grid(column=1, row=0)

                            self.btn_view_learners = CTkButton(self.addgroups, text="View learners", fg_color="red",
                                                               command=addmarks)
                            self.btn_view_learners.grid(column=2, row=0)

                        addlearners()

                self.btn_submit_group = CTkButton(self.addgroups, text="Add group", fg_color="red", command=addgroup)
                self.btn_submit_group.grid(column=1, row=0)

            self.btn_group_choose = CTkButton(self.menu, text="Add group", fg_color="red", command=addgroupmenu)
            self.btn_group_choose.grid(column=0, row=1)
            self.btn_group_choose = CTkButton(self.menu, text="View groups", fg_color="red", command=view_groups)
            self.btn_group_choose.grid(column=0, row=2)

        self.root.mainloop()


Main()
