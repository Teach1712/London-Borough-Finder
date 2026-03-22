import tkinter as tk
from tkinter import messagebox
import sqlite3
import re
import subprocess
import sys
from PIL import Image, ImageTk

# ---------------- DATABASE SETUP ---------------- #
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT UNIQUE
)
""")
conn.commit()

# ---------------- EMAIL VALIDATION ---------------- #
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.com$'
    return re.match(pattern, email)

# ---------------- PASSWORD VALIDATION ---------------- #
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# ---------------- OPEN HOME PAGE ---------------- #
def open_homepage():
    root.destroy()
    subprocess.Popen([sys.executable, "home_page.py"])

# ---------------- REGISTER USER ---------------- #
def register():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    if not validate_email(email):
        messagebox.showerror(
            "Invalid Email",
            "Email must include @ and end with .com\nExample: user@gmail.com"
        )
        return

    if not validate_password(password):
        messagebox.showerror(
            "Invalid Password",
            "Password must be at least 8 characters long\n"
            "Include:\n- 1 Uppercase\n- 1 Lowercase\n- 1 Number\n- 1 Special character"
        )
        return

    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, password)
        )
        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")
        email_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email or Password already exists")

# ---------------- LOGIN USER ---------------- #
def login():
    email = email_entry.get()
    password = password_entry.get()

    if not validate_email(email):
        messagebox.showerror(
            "Invalid Email",
            "Email must include @ and end with .com"
        )
        return

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login Successful!\nAccess Granted")
        open_homepage()
    else:
        messagebox.showerror("Error", "Invalid Email or Password")

# ---------------- FORGOT PASSWORD ---------------- #
def open_forgot_password():
    win = tk.Toplevel(root)
    win.title("Reset Password")
    win.geometry("400x300")

    tk.Label(win, text="Reset Your Password", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(win, text="Email:").pack()
    email_entry_fp = tk.Entry(win, width=30)
    email_entry_fp.pack(pady=5)

    tk.Label(win, text="New Password:").pack()
    new_pass_entry = tk.Entry(win, show="*", width=30)
    new_pass_entry.pack(pady=5)

    tk.Label(win, text="Confirm Password:").pack()
    confirm_pass_entry = tk.Entry(win, show="*", width=30)
    confirm_pass_entry.pack(pady=5)

    def reset_password():
        email = email_entry_fp.get()
        new_pass = new_pass_entry.get()
        confirm_pass = confirm_pass_entry.get()

        if not validate_email(email):
            messagebox.showerror("Error", "Enter a valid email ending with .com")
            return

        if new_pass != confirm_pass:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if not validate_password(new_pass):
            messagebox.showerror(
                "Invalid Password",
                "Password must be at least 8 characters long\n"
                "Include uppercase, lowercase, number & special character"
            )
            return

        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()

        if not user:
            messagebox.showerror("Error", "Email not registered")
            return

        try:
            cursor.execute(
                "UPDATE users SET password=? WHERE email=?",
                (new_pass, email)
            )
            conn.commit()
            messagebox.showinfo("Success", "Password updated successfully")
            win.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Password already in use")

    tk.Button(win, text="Reset Password", command=reset_password).pack(pady=20)

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("London Borough Finder - Login")
root.geometry("800x400")
root.configure(bg="#9bd3ee")

main_frame = tk.Frame(root, bg="#9bd3ee")
main_frame.pack(fill="both", expand=True)

# ---------------- LEFT ICON BAR ---------------- #
icon_frame = tk.Frame(main_frame, bg="#9bd3ee", width=100)
icon_frame.pack(side="left", fill="y", padx=10, pady=20)

def load_icon(path, size=(40, 40)):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except:
        return None

home_icon = load_icon("home.png")
safety_icon = load_icon("safety.png")
education_icon = load_icon("education.png")
stats_icon = load_icon("stats.png")

tk.Label(icon_frame, image=home_icon, bg="#9bd3ee").pack(pady=15,padx=50)
tk.Label(icon_frame, image=safety_icon, bg="#9bd3ee").pack(pady=15)
tk.Label(icon_frame, image=education_icon, bg="#9bd3ee").pack(pady=15)
tk.Label(icon_frame, image=stats_icon, bg="#9bd3ee").pack(pady=15)

# ---------------- RIGHT LOGIN FORM ---------------- #
form_frame = tk.Frame(main_frame, bg="#9bd3ee")
form_frame.pack(side="left", fill="both", expand=True, padx=20)

tk.Label(
    form_frame,
    text="Welcome",
    bg="#9bd3ee",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(
    form_frame,
    text="Please click 'sign in' or 'login', then enter your email and password.",
    bg="#9bd3ee",
    font=("Arial", 10)
).pack(pady=5)

# ---------------- EMAIL & PASSWORD FIELDS ---------------- #


field_frame = tk.Frame(form_frame, bg="#9bd3ee")
field_frame.pack(pady=20)

# Email Row
tk.Label(field_frame, text="Email:       ", bg="#9bd3ee", width=10, anchor="e").grid(row=0, column=0, padx=5, pady=10)
email_entry = tk.Entry(field_frame, width=45)
email_entry.grid(row=0, column=1, padx=5, pady=10)

# Password Row
tk.Label(field_frame, text="Password:", bg="#9bd3ee", width=10, anchor="e").grid(row=1, column=0, padx=5, pady=10)
password_entry = tk.Entry(field_frame, show="*", width=45)
password_entry.grid(row=1, column=1, padx=5, pady=10)


btn_frame = tk.Frame(form_frame, bg="#9bd3ee")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Sign In", width=10, command=register).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Login", width=10, command=login).grid(row=0, column=1, padx=10)

tk.Button(
    form_frame,
    text="Forgot Password?",
    fg="blue",
    relief="flat",
    bg="#9bd3ee",
    cursor="hand2",
    command=open_forgot_password
).pack()

root.mainloop()
