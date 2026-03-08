import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from PIL import Image, ImageTk



# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("London Borough Finder - Education")
root.geometry("1100x650")
root.configure(bg="white")

# ---------------- TOP HEADER ---------------- #
header_frame = tk.Frame(root, bg="#3db4f2", height=100)
header_frame.pack(fill="x")

tk.Label(
    header_frame,
    text="London Borough Finder",
    bg="#3db4f2",
    fg="black",
    font=("Arial", 22, "bold")
).pack(pady=15)



# ---------------- OPEN OTHER PAGES ---------------- #

def go_home():
    root.destroy()
    subprocess.Popen([sys.executable, "home_page.py"])


def open_house_price():
    root.destroy()
    subprocess.Popen([sys.executable, "house_prices.py"])

def open_safety():
    root.destroy()
    subprocess.Popen([sys.executable, "safety.py"])

def open_education():
    pass

def open_transport():
    root.destroy()
    subprocess.Popen([sys.executable, "transport.py"])

def open_leisure():
    root.destroy()
    subprocess.Popen([sys.executable, "leisure.py"])

def open_shopping():
    root.destroy()
    subprocess.Popen([sys.executable, "shopping.py"])

def open_health_fitness():
    root.destroy()
    subprocess.Popen([sys.executable, "health_fitness.py"])

def open_support_report():
    root.destroy()
    subprocess.Popen([sys.executable, "support_report.py"])


# ---------------- HOME ICON ---------------- #
home_img = Image.open("home.png")
home_img = home_img.resize((35, 35), Image.LANCZOS)
home_icon = ImageTk.PhotoImage(home_img)

home_button = tk.Button(
    header_frame,
    image=home_icon,
    bg="#3db4f2",
    bd=0,
    cursor="hand2",
    command=go_home
)
home_button.place(x=15, y=15)



# ---------------- NAVIGATION BAR ---------------- #
nav_frame = tk.Frame(root, bg="#2fa4de")
nav_frame.pack(fill="x")

tk.Button(nav_frame, text="House prices", width=12,relief="flat", bg="#2fa4de",command=open_house_price).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Education", width=12, bg="#2fa4de",relief="flat",command=open_education).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Safety", width=12, bg="#2fa4de",relief="flat",command=open_safety).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Shopping", width=12, bg="#2fa4de",relief="flat",command=open_shopping).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Health and Fitness", width=15, bg="#2fa4de",relief="flat",command=open_health_fitness).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Leisure", width=12, bg="#2fa4de",relief="flat",command=open_leisure).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Transport", width=12, bg="#2fa4de",relief="flat",command=open_transport).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Support and Report", width=15, bg="#2fa4de",relief="flat",command=open_support_report).pack(side="left", padx=10, pady=5)
# ---------------- DESCRIPTION ---------------- #
desc_frame = tk.Frame(root, bg="white")
desc_frame.pack(fill="x", pady=15)

tk.Label(
    desc_frame,
    text="Education Statistics by Borough",
    font=("Arial", 16, "bold"),
    bg="white"
).pack()

tk.Label(
    desc_frame,
    text="This table ranks London boroughs based on education performance. "
         "Rank 1 represents the best performing borough.",
    font=("Arial", 11),
    bg="white"
).pack(pady=5)

# ---------------- TABLE FRAME ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ---------------- EDUCATION TABLE ---------------- #
columns = ("Borough", "No. of Secondary & Primary Schools", "No. of Colleges & University", "Avg of Student Ranking","Notable University & Colleges","Borough Education Ranking")

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# ---------------- SAMPLE DATA ---------------- #
education_data = [
    (1, "Barnet", 78, "Outstanding", 4.1,2),
    (2, "Redbridge", 75, "Outstanding", 3.9,5),
    (3, "Harrow", 73, "Good", 3.8,6),
    (4, "Hillingdon", 70, "Good", 3.6,7),
    (5, "Greenwich", 68, "Good", 3.5,4),
    (6, "Lewisham", 65, "Good", 3.4,9),
    (7, "Bexley", 63, "Good", 3.3,6),
    (8, "Havering", 61, "Requires Improvement", 3.1,5),
    (9, "Newham", 59, "Requires Improvement", 3.0,9),
    (10, "Barking and Dagenham", 56, "Requires Improvement", 2.9,9)
]

for row in education_data:
    tree.insert("", tk.END, values=row)

tree.pack(fill="both", expand=True)

# ---------------- SCROLLBAR ---------------- #
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# ---------------- FOOTER ---------------- #
footer = tk.Label(
    root,
    text="London Borough Finder © 2026",
    bg="#f0f0f0",
    font=("Arial", 10)
)
footer.pack(fill="x", pady=5)

root.mainloop()
