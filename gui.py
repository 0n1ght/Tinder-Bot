# gui.py
import tkinter as tk
from tkinter import ttk

def create_gui():
    # Tworzenie głównego okna
    root = tk.Tk()
    root.title("Tinder Swapper")
    root.geometry("300x250")

    bot_label = tk.Label(root, text="Tinder Swapper", font=("Arial", 16))
    bot_label.pack(pady=10)

    sign_in_label = tk.Label(root, text="Sign-in method:")
    sign_in_label.pack()

    sign_in_var = tk.StringVar()
    sign_in_menu = ttk.Combobox(root, textvariable=sign_in_var, state="readonly")
    sign_in_menu['values'] = ("Facebook", "Google")
    sign_in_menu.current(0)
    sign_in_menu.pack(pady=5)

    email_label = tk.Label(root, text="Email or phone:")
    email_label.pack()

    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    password_label = tk.Label(root, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    platform = tk.StringVar()
    login = tk.StringVar()
    passwd = tk.StringVar()
    submitted = tk.BooleanVar(value=False)

    def on_submit():
        platform.set(sign_in_var.get())
        login.set(email_entry.get())
        passwd.set(password_entry.get())
        submitted.set(True)
        root.destroy()

    submit_button = tk.Button(root, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()

    return platform.get(), login.get(), passwd.get(), submitted.get()
