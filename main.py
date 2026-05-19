import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry("900x600")
app.title("Smart Expense Tracker")

title = ctk.CTkLabel(
    app,
    text="Smart Expense Tracker",
    font=("Arial", 28, "bold")
)

title.pack(pady=20)

app.mainloop()