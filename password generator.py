import tkinter as tk
import random
import string


# Generate Password
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(12))

    password_box.delete(0, tk.END)
    password_box.insert(0, password)


# Copy Password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_box.get())


# Main Window
root = tk.Tk()
root.title("3D Password Generator")
root.geometry("550x400")
root.configure(bg="#080014")  # Black-purple background

# Title
title = tk.Label(
    root,
    text="🔐 3D PASSWORD GENERATOR",
    font=("Arial", 22, "bold"),
    bg="#080014",
    fg="#FF4FD8"
)
title.pack(pady=20)

# Password Box
password_box = tk.Entry(
    root,
    font=("Arial", 18, "bold"),
    width=28,
    justify="center",
    bg="#1A002B",
    fg="#00F5FF",
    bd=4,
    relief="ridge"
)
password_box.pack(pady=30, ipady=12)


# 3D Button Function
def create_button(text, command, color):
    outer = tk.Frame(root, bg="#C026D3", padx=2, pady=2)  # Glow border

    btn = tk.Button(
        outer,
        text=text,
        command=command,
        font=("Arial", 14, "bold"),
        bg=color,
        fg="white",
        width=16,
        height=1,
        relief="raised",
        bd=5
    )
    btn.pack()
    return outer


# Buttons
generate_btn = create_button("Generate", generate_password, "#7E22CE")
generate_btn.pack(pady=15)

copy_btn = create_button("Copy", copy_password, "#DB2777")
copy_btn.pack(pady=15)

root.mainloop()