import tkinter as tk 
from tkinter import messagebox, ttk 
import pandas as pd 
import matplotlib.pyplot as plt 
class AttendanceCounter: 
def __init__(self, master): 
self.master = master 
self.master.title("Attendance Counter") 
self.master.geometry("400x300") 
self.students = ["Aayush", "Rohit", "Anish", "Aniket", "Vaibhav"] 
self.attendance = {student: [] for student in self.students} 
self.student_label = tk.Label(master, text="Select Student:") 
self.student_label.pack(pady=10) 
self.student_combo = ttk.Combobox(master, values=self.students) 
self.student_combo.pack(pady=10) 
self.present_button = tk.Button(master, text="Mark Present", 
command=self.mark_present) 
self.present_button.pack(pady=5) 
self.absent_button = tk.Button(master, text="Mark Absent", 
command=self.mark_absent) 
self.absent_button.pack(pady=5) 
self.visualize_button = tk.Button(master, text="Visualize Attendance", 
command=self.visualize_attendance) 
self.visualize_button.pack(pady=10) 
def mark_present(self): 
selected_student = self.student_combo.get() 
if selected_student: 
self.attendance[selected_student].append("Present") 
messagebox.showinfo("Success", f"{selected_student} marked as 
Present!") 
else: 
messagebox.showwarning("Input Error", "Please select a student.") 
def mark_absent(self): 
selected_student = self.student_combo.get() 
if selected_student: 
self.attendance[selected_student].append("Absent") 
messagebox.showinfo("Success", f"{selected_student} marked as 
Absent!") 
else: 
messagebox.showwarning("Input Error", "Please select a student.") 
def visualize_attendance(self): 
attendance_summary = {student: sum(1 for record in records if record == 
"Present") 
for student, records in self.attendance.items()} 
df = pd.DataFrame(list(attendance_summary.items()), columns=['Student', 
'Present Count']) 
plt.figure(figsize=(8, 5)) 
plt.bar(df['Student'], df['Present Count'], color='green') 
plt.title('Attendance Summary') 
plt.xlabel('Students') 
plt.ylabel('Number of Days Present') 
plt.xticks(rotation=45) 
plt.tight_layout() 
plt.show() 
if __name__ == "__main__": 
root = tk.Tk() 
app = AttendanceCounter(root) 
root.mainloop()
