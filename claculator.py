import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("450x700")
app.title("Game Calculator")
app.configure(fg_color="#05010A")   # Deep black-purple

# Display
display = ctk.CTkEntry(
    app,
    width=380,
    height=80,
    font=("Arial", 32, "bold"),
    corner_radius=20,
    fg_color="#1A002B",
    text_color="#00F5FF"
)
display.pack(pady=30)

def click(value):
    display.insert("end", value)

def clear():
    display.delete(0, "end")

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, "end")
        display.insert(0, str(result))
    except:
        display.delete(0, "end")
        display.insert(0, "Error")

# Buttons
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack()

buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

for row in buttons:
    row_frame = ctk.CTkFrame(frame, fg_color="transparent")
    row_frame.pack(pady=8)

    for btn in row:
        if btn == "=":
            cmd = calculate
        elif btn == "C":
            cmd = clear
        else:
            cmd = lambda x=btn: click(x)

        button = ctk.CTkButton(
            row_frame,
            text=btn,
            width=75,
            height=75,
            corner_radius=25,
            font=("Arial", 24, "bold"),
            fg_color="#2A003F",
            hover_color="#C026D3",
            text_color="white",
            command=cmd
        )
        button.pack(side="left", padx=8)

app.mainloop()