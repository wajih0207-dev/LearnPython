
import customtkinter as ctk

app = ctk.CTk()
app.title("CustomTkinter Test")
app.geometry("400x250")

label = ctk.CTkLabel(
    app,
    text="CustomTkinter is working!"
)
label.pack(pady=30)

button = ctk.CTkButton(
    app,
    text="It works!",
    command=lambda: print("Button clicked!")
)
button.pack(pady=10)

app.mainloop()
