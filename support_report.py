# --------- LIST OF IMPORTS --------- #
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
from PIL import Image, ImageTk
import smtplib
from email.message import EmailMessage
import webbrowser
import sqlite3   # ✅ NEW

# ---------------- DATABASE SETUP ---------------- #
conn = sqlite3.connect("ratings.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rating INTEGER
)
""")
conn.commit()

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("London Borough Finder")
root.geometry("1100x700")

# ---------------- TOP HEADER ---------------- #
header_frame = tk.Frame(root, bg="#3db4f2", height=100)
header_frame.pack(fill="x")

tk.Label(header_frame, text="London Borough Finder",
         bg="#3db4f2", fg="black",
         font=("Arial", 22, "bold")).pack(pady=15)

# ---------------- PAGE NAVIGATION FUNCTION ---------------- #
def open_page(filename):
    root.destroy()
    subprocess.Popen([sys.executable, filename])

# ---------------- HOME ICON ---------------- #
try:
    home_img = Image.open("home.png")
    home_img = home_img.resize((35, 35), Image.LANCZOS)
    home_icon = ImageTk.PhotoImage(home_img)

    tk.Button(header_frame, image=home_icon,
              bg="#3db4f2", bd=0,
              command=lambda: open_page("home_page.py")).place(x=15, y=15)
except:
    print("home.png not found")

# ---------------- NAVIGATION BAR ---------------- #
nav_frame = tk.Frame(root, bg="#2fa4de")
nav_frame.pack(fill="x")

buttons = [
    ("House prices", "house_price.py"),
    ("Education", "education.py"),
    ("Safety", "safety.py"),
    ("Shopping", "shopping.py"),
    ("Health and Fitness", "health_fitness.py"),
    ("Leisure", "leisure.py"),
    ("Transport", "transport.py"),
    ("Food", "food.py"),
    ("Support and Report", "support_report.py")
]

for text, file in buttons:
    tk.Button(nav_frame, text=text, width=15,
              relief="flat", bg="#2fa4de",
              command=lambda f=file: open_page(f)
              ).pack(side="left", padx=8, pady=5)

# ---------------- DESCRIPTION ---------------- #
desc_frame = tk.Frame(root, bg="white")
desc_frame.pack(fill="x", pady=15)

tk.Label(desc_frame, text="Support and Report",
         font=("Arial", 16, "bold"), bg="white").pack()

tk.Label(desc_frame,
         text="The links of the websites from which the data/statistics are collected.",
         font=("Arial", 11), bg="white").pack(pady=5)

# ---------------- TABLE ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("Safety", "Education", "House Prices", "Shopping",
           "Health and Fitness", "Leisure", "Food", "Transport")

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

report_data = [
    (
        "https://www.met.police.uk/crime-statistics/",
        "https://www.london.gov.uk/what-we-do/education-and-youth/schools-and-education/london-schools-performance-tables",
        "https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/housepriceindex/latest",
        "https://www.londontoolkit.com/boroughs/shopping.htm",
        "https://www.nhs.uk/service-search/find-a-gp",
        "https://www.londontoolkit.com/boroughs/leisure.htm",
        "https://www.londontoolkit.com/boroughs/food.htm",
        "https://www.londontoolkit.com/boroughs/transport.htm"
    ),
    (
        "https://www.london.gov.uk/what-we-do/communities-and-social-justice/safety-and-crime/safe-london-partnership",
        "https://www.london.gov.uk/what-we-do/education-and-youth/schools-and-education/london-schools-performance-tables",
        "https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/housepriceindex/latest",
        "https://www.londontoolkit.com/boroughs/shopping.htm",
        "https://www.nhs.uk/service-search/find-a-gp",
        "https://www.londontoolkit.com/boroughs/leisure.htm",
        "https://www.londontoolkit.com/boroughs/food.htm",
        "https://www.londontoolkit.com/boroughs/transport.htm"
    ),
    (
        "https://www.london.gov.uk/what-we-do/communities-and-social-justice/safety-and-crime/safe-london-partnership",
        "https://www.london.gov.uk/what-we-do/education-and-youth/schools-and-education/london-schools-performance-tables",                                 
        "https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/housepriceindex/latest",
        "https://www.londontoolkit.com/boroughs/shopping.htm",
        "https://www.nhs.uk/service-search/find-a-gp",
        "https://www.londontoolkit.com/boroughs/leisure.htm",
        "https://www.londontoolkit.com/boroughs/food.htm",
        "https://www.londontoolkit.com/boroughs/transport.htm"        
    ),
    (
        "https://www.london.gov.uk/what-we-do/communities-and-social-justice/safety-and-crime/safe-london-partnership",
        "https://www.london.gov.uk/what-we-do/education-and-youth/schools-and-education/london-schools-performance-tables",
        "https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/housepriceindex/latest",
        "https://www.londontoolkit.com/boroughs/shopping.htm",
        "https://www.nhs.uk/service-search/find-a-gp",
        "https://www.londontoolkit.com/boroughs/leisure.htm",
        "https://www.londontoolkit.com/boroughs/food.htm",
        "https://www.londontoolkit.com/boroughs/transport.htm"
    ),
    (
        "https://www.london.gov.uk/what-we-do/communities-and-social-justice/safety-and-crime/safe-london-partnership",
        "https://www.london.gov.uk/what-we-do/education-and-youth/schools-and-education/london-schools-performance-tables",
        "https://www.ons.gov.uk/economy/inflationandpriceindices/bulletins/housepriceindex/latest",
        "https://www.londontoolkit.com/boroughs/shopping.htm",
        "https://www.nhs.uk/service-search/find-a-gp",
        "https://www.londontoolkit.com/boroughs/leisure.htm",
        "https://www.londontoolkit.com/boroughs/food.htm",
        "https://www.londontoolkit.com/boroughs/transport.htm"
    )
]

for row in report_data:
    tree.insert("", tk.END, values=row)

def open_link(event):
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)

    if item:
        col_index = int(column.replace("#", "")) - 1
        values = tree.item(item, "values")

        if col_index < len(values):
            webbrowser.open(values[col_index])

tree.pack(side="left", fill="both", expand=True)
tree.bind("<Button-1>", open_link)

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# ---------------- EMAIL FUNCTION ---------------- #
def send_concern_email():
    concern_text = concern_entry.get()

    if concern_text.strip() == "":
        messagebox.showwarning("Empty", "Please enter your concern.")
        return

    try:
        sender_email = "singh.light@gmail.com"
        app_password = "your_app_password"

        msg = EmailMessage()
        msg['Subject'] = "Concern"
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg.set_content(concern_text)

        import smtplib
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        messagebox.showinfo("Success", "Sent!")
        concern_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- CONCERN BOX ---------------- #
concern_frame = tk.Frame(root, bg="white")
concern_frame.pack(pady=10)

tk.Label(concern_frame, text="Enter concern:", bg="white").grid(row=0, column=0)

concern_entry = tk.Entry(concern_frame, width=50)
concern_entry.grid(row=0, column=1)

tk.Button(concern_frame, text="Send",
          bg="#2fa4de", fg="white",
          command=send_concern_email).grid(row=0, column=2)

# ---------------- RATING SYSTEM ---------------- #
rating_frame = tk.Frame(root, bg="white")
rating_frame.pack(pady=20)

tk.Label(rating_frame, text="Rate our program!",
         bg="white", font=("Arial", 12, "bold")).grid(row=0, column=0)

stars = []
rating_value = tk.IntVar()

def update_average():
    cursor.execute("SELECT AVG(rating) FROM ratings")
    result = cursor.fetchone()[0]

    if result:
        avg_label.config(text=f"Average rating: {result:.2f}/5")
    else:
        avg_label.config(text="Average rating: 0/5")

def set_rating(value):
    rating_value.set(value)

    for i, star in enumerate(stars):
        star.config(text="★" if i < value else "☆")

    cursor.execute("INSERT INTO ratings (rating) VALUES (?)", (value,))
    conn.commit()

    update_average()

for i in range(5):
    star = tk.Label(rating_frame, text="☆", font=("Arial", 24))
    star.grid(row=0, column=i+1)
    star.bind("<Button-1>", lambda e, v=i+1: set_rating(v))
    stars.append(star)

avg_label = tk.Label(rating_frame,
                     text="Average rating: 0/5",
                     bg="white",
                     font=("Arial", 12))
avg_label.grid(row=0, column=7, padx=20)

update_average()  # ✅ load existing ratings

# ---------------- FOOTER ---------------- #
tk.Label(root, text="London Borough Finder © 2026",
         bg="#f0f0f0").pack(fill="x")

root.mainloop()