import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x550")
root.config(bg="white")

# Time Update Function
def update_time():
    current = datetime.now().strftime("%d-%m-%Y | %I:%M:%S %p")
    time_label.config(text=current)
    root.after(1000, update_time)

# Task Functions
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select task first!")

# Background Design
canvas = tk.Canvas(root, width=700, height=550, bg="white", highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_polygon(0, 0, 150, 0, 0, 150, fill="#0f6b46")
canvas.create_polygon(700, 550, 550, 550, 700, 400, fill="#0f6b46")

# Title
title = tk.Label(root, text="TO-DO LIST",
                 font=("Arial", 28, "bold"),
                 bg="white")
title.pack(pady=10)

# Date and Time
time_label = tk.Label(root, font=("Arial", 14, "bold"),
                      bg="white", fg="green")
time_label.pack()
update_time()

# Entry Box
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=20)

# Buttons
frame = tk.Frame(root, bg="white")
frame.pack()

tk.Button(frame, text="Add Task", command=add_task,
          bg="green", fg="white",
          font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)

tk.Button(frame, text="Delete Task", command=delete_task,
          bg="red", fg="white",
          font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10)

# Listbox
listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 13))
listbox.pack(pady=20)

root.mainloop()