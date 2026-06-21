import tkinter as tk
from tkinter import messagebox


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        return f"Student Name: {self.name}, ID: {self.student_id}"


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_teacher_info(self):
        return f"Teacher: {self.name}\nSubject: {self.subject}"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Class Object Relationship")
        self.root.geometry("500x400")
        self.root.configure(bg="white")

        self.teacher = Teacher("Mr. Rahman", "Python Programming")

        tk.Label(root, text="Student Name", bg="white", fg="black").pack()
        self.name_entry = tk.Entry(root, bg="white", fg="black", insertbackground="black")
        self.name_entry.pack()

        tk.Label(root, text="Student ID", bg="white", fg="black").pack()
        self.id_entry = tk.Entry(root, bg="white", fg="black", insertbackground="black")
        self.id_entry.pack()

        tk.Button(root, text="Add Student", command=self.add_student).pack(pady=10)
        tk.Button(root, text="Show Relationship", command=self.show_relationship).pack()

        self.output = tk.Text(
            root,
            height=12,
            width=55,
            bg="white",
            fg="black",
            insertbackground="black"
        )
        self.output.pack(pady=10)

    def add_student(self):
        name = self.name_entry.get()
        student_id = self.id_entry.get()

        if name == "" or student_id == "":
            messagebox.showwarning("Warning", "Please enter all fields")
            return

        student = Student(name, student_id)
        self.teacher.add_student(student)

        messagebox.showinfo("Success", "Student object added to Teacher object")

        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)

    def show_relationship(self):
        self.output.delete("1.0", tk.END)

        self.output.insert(tk.END, self.teacher.show_teacher_info())
        self.output.insert(tk.END, "\n\nObject Relationship:\n")
        self.output.insert(tk.END, "Teacher object contains these Student objects:\n\n")

        for student in self.teacher.students:
            self.output.insert(tk.END, student.show_info() + "\n")


root = tk.Tk()
app = App(root)
root.mainloop()