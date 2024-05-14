import tkinter as tk
from tkinter import messagebox

class GUIUniApp:
    def __init__(self, master):
        self.master = master
        self.master.title("GUIUniApp - Student Login")
        self.master.geometry("300x200")

        # Initialize student database
        self.student_database = self.load_student_data()

        # Create login widgets
        self.label_email = tk.Label(master, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()

        self.label_password = tk.Label(master, text="Password:")
        self.label_password.pack()
        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.pack()

    def load_student_data(self):
        # Load student data from file 'students.data' (simulated data for demonstration)
        student_data = {}
        try:
            with open("students.data", "r") as file:
                for line in file:
                    email, password = line.strip().split(",")
                    student_data[email] = {"password": password, "subjects": []}
        except FileNotFoundError:
            messagebox.showerror("Error", "Students data file not found.")
        return student_data

    def save_student_data(self):
        # Save student data to file 'students.data'
        with open("students.data", "w") as file:
            for email, data in self.student_database.items():
                file.write(f"{email},{data['password']}\n")

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Check if email and password match records in the database
        if email in self.student_database and self.student_database[email]["password"] == password:
            messagebox.showinfo("Login Successful", "Welcome, " + email)
            self.open_enrolment_window(email)
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    def open_enrolment_window(self, email):
        enrolment_window = tk.Toplevel(self.master)
        enrolment_window.title("Enrolment")

        # Enrolment heading
        label_heading = tk.Label(enrolment_window, text="Enrolment", font=("Arial", 14, "bold"))
        label_heading.pack(pady=10)

        # Enrolment form
        self.label_subjects = tk.Label(enrolment_window, text="Select Subjects:")
        self.label_subjects.pack()

        self.subject_var1 = tk.BooleanVar()
        self.subject_var2 = tk.BooleanVar()
        self.subject_var3 = tk.BooleanVar()
        self.subject_var4 = tk.BooleanVar()
        self.subject_var5 = tk.BooleanVar()
        self.subject_var6 = tk.BooleanVar()



        self.checkbutton1 = tk.Checkbutton(enrolment_window, text="Subject 1", variable=self.subject_var1)
        self.checkbutton1.pack()
        self.checkbutton2 = tk.Checkbutton(enrolment_window, text="Subject 2", variable=self.subject_var2)
        self.checkbutton2.pack()
        self.checkbutton3 = tk.Checkbutton(enrolment_window, text="Subject 3", variable=self.subject_var3)
        self.checkbutton3.pack()
        self.checkbutton4 = tk.Checkbutton(enrolment_window, text="Subject 4", variable=self.subject_var4)
        self.checkbutton4.pack()
        self.checkbutton5 = tk.Checkbutton(enrolment_window, text="Subject 5", variable=self.subject_var5)
        self.checkbutton5.pack()
        self.checkbutton6 = tk.Checkbutton(enrolment_window, text="Subject 6", variable=self.subject_var6)
        self.checkbutton6.pack()

        self.button_enrol = tk.Button(enrolment_window, text="Enrol", command=lambda: self.enrol(email))
        self.button_enrol.pack(pady=10)

    def enrol(self, email):
        selected_subjects = []
        if self.subject_var1.get():
            selected_subjects.append("Subject 1")
        if self.subject_var2.get():
            selected_subjects.append("Subject 2")
        if self.subject_var3.get():
            selected_subjects.append("Subject 3")
        if self.subject_var4.get():
            selected_subjects.append("Subject 4")
        if self.subject_var5.get():
            selected_subjects.append("Subject 5")
        if self.subject_var6.get():
            selected_subjects.append("Subject 6")

        if len(selected_subjects) > 4:
            messagebox.showerror("Enrolment Failed", "You can enrol in a maximum of 4 subjects.")
        elif len(selected_subjects) == 0:
            messagebox.showerror("Enrolment Failed", "Please select at least one subject.")
        else:
            # Update student's enrolled subjects
            self.student_database[email]["subjects"] = selected_subjects
            messagebox.showinfo("Enrolment Successful", "You have successfully enrolled.")
            self.save_student_data()
            # Open enrollment list window
            self.open_enrollment_list_window(email)

    def open_enrollment_list_window(self, email):
        enrollment_list_window = tk.Toplevel(self.master)
        enrollment_list_window.title("Enrollment List")

        # Enrollment list heading
        label_heading = tk.Label(enrollment_list_window, text="Enrollment List", font=("Arial", 14, "bold"))
        label_heading.pack(pady=10)

        # Create enrollment listbox
        enrollment_listbox = tk.Listbox(enrollment_list_window)
        enrollment_listbox.pack()

        # Display enrolled subjects in listbox
        for subject in self.student_database[email]["subjects"]:
            enrollment_listbox.insert(tk.END, subject)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIUniApp(root)
    root.mainloop()
