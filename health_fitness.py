import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from PIL import Image, ImageTk

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("London Borough Finder")
root.geometry("1100x700")

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
    pass

def open_safety():
    root.destroy()
    subprocess.Popen([sys.executable, "safety.py"])

def open_education():
    root.destroy()
    subprocess.Popen([sys.executable, "education.py"])

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

def open_food():
    root.destroy()
    subprocess.Popen([sys.executable, "food.py"])

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
tk.Button(nav_frame, text="Food", width=12, bg="#2fa4de",relief="flat",command=open_food).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Support and Report", width=15, bg="#2fa4de",relief="flat",command=open_support_report).pack(side="left", padx=10, pady=5)

# ---------------- DESCRIPTION ---------------- #
desc_frame = tk.Frame(root, bg="white")
desc_frame.pack(fill="x", pady=15)

tk.Label(
    desc_frame,
    text="HEALTH AND FITNESS",
    font=("Arial", 16, "bold"),
    bg="white"
).pack()

# ---------------- TABLE FRAME ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ---------------- UPDATED COLUMNS ---------------- #
columns = (
    "Borough",
    "GP Clinics",
    "Hospitals",
    "Pharmacies",
    "Gyms",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# ---------------- DATA ---------------- #
health_data = [
    ("Camden", 25, 3, 15, 20),
    ("Barking and Dagenham", 10, 1, 5, 8),
    ("Barnet", 20, 2, 10, 15),
    ("Bexley", 15, 1, 8, 12),
    ("Brent", 18, 2, 12, 18),
    ("Bromley", 22, 3, 14, 17),
    ("Croydon", 30, 4, 20, 25),
    ("Ealing", 28, 3, 18, 22),
    ("Enfield", 26, 3, 16, 19),
    ("Greenwich", 24, 2, 14, 18),
    ("Hackney", 12, 1, 6, 10),
    ("Hammersmith and Fulham", 16, 2, 10, 14),
    ("Haringey", 14, 1, 8, 12),
    ("Harrow", 17, 2, 11, 16),
    ("Havering", 19, 2, 13, 17),
    ("Hillingdon", 21, 3, 15, 19),
    ("Hounslow", 23, 3, 17, 20),
    ("Islington", 27, 4, 19, 23),
    ("Kensington and Chelsea", 29, 4, 21, 24),
    ("Kingston upon Thames", 18, 2, 12, 16),
    ("Lambeth", 13, 1, 7, 11),
    ("Lewisham", 20, 3, 14, 18),
    ("Merton", 21, 3, 15, 19),
    ("Newham", 17, 2, 12, 16),
    ("Redbridge", 23, 3, 17, 21),
    ("Richmond upon Thames", 26, 4, 18, 22),
    ("Southwark", 25, 3, 16, 20),
    ("Sutton", 22, 3, 14, 18),
    ("Tower Hamlets", 19, 2, 13, 17),
    ("Waltham Forest", 24, 3, 16, 20),
    ("Wandsworth", 28, 4, 20, 24),
    ("City of London", 30, 4, 22, 26)
]

# ---------------- PROCESS ---------------- #
processed = []

for b, gp, hosp, pharm, gym in health_data:
    processed.append({
        "borough": b,
        "gp": gp,
        "hosp": hosp,
        "pharm": pharm,
        "gym": gym
    })

# ---------------- RANKING (HIGHER = BETTER) ---------------- #
def rank_desc(key):
    sorted_list = sorted(processed, key=lambda x: x[key], reverse=True)
    rank = 1
    prev = None
    for i, item in enumerate(sorted_list):
        if prev != item[key]:
            rank = i + 1
        item[f"rank_{key}"] = rank
        prev = item[key]

rank_desc("gp")
rank_desc("hosp")
rank_desc("pharm")
rank_desc("gym")

# ---------------- AVERAGE RANK ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_gp"] +
        item["rank_hosp"] +
        item["rank_pharm"] +
        item["rank_gym"]
    ) / 4

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
for item in processed:
    tree.insert("", tk.END, values=(
        item["borough"],
        item["gp"],
        item["hosp"],
        item["pharm"],
        item["gym"],
        f"{item['avg_rank']:.2f}"   # ✅ 2 decimal places
    ))

tree.pack(fill="both", expand=True)

# ---------------- SCROLLBAR ---------------- #
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# ---------------- FOOTER ---------------- #
tk.Label(root, text="London Borough Finder © 2026").pack()

root.mainloop()