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

def open_house_price():
    root.destroy()
    subprocess.Popen([sys.executable, "house_prices.py"])


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
    text="TRANSPORT",
    font=("Arial", 16, "bold"),
    bg="white"
).pack()


# ---------------- TABLE FRAME ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)



# ---------------- UPDATED COLUMNS ---------------- #
columns = (
    "Borough",
    "Tubes",
    "Train Stations",
    "Bus Stations",
    "Commute Distance/Time",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# ---------------- DATA ---------------- #
transport_data = [
    ("Camden", 5, 200, 3, 10),
    ("Barking and Dagenham", 2, 50, 1, 30),
    ("Barnet", 4, 150, 2, 15),
    ("Bexley", 1, 30, 1, 25),
    ("Brent", 3, 120, 2, 20),
    ("Bromley", 2, 80, 1, 22),
    ("Croydon", 3, 100, 2, 18),
    ("Ealing", 4, 130, 3, 12),
    ("Enfield", 2, 90, 1, 28),
    ("Greenwich", 3, 110, 2, 16),
    ("Hackney", 2, 70, 1, 24),
    ("Hammersmith and Fulham", 4, 140, 3, 14),
    ("Haringey", 1, 40, 1, 26),
    ("Harrow", 3, 100, 2, 17),
    ("Havering", 2, 80, 1, 23),
    ("Hillingdon", 3, 110, 2, 19),
    ("Hounslow", 2, 90, 1, 21),
    ("Islington", 4, 150, 3, 10),
    ("Kensington and Chelsea", 5, 200, 4, 8),
    ("Kingston upon Thames", 3, 120, 2, 16),
    ("Lambeth", 3, 120, 2, 18),
    ("Lewisham", 2, 80, 1, 22),
    ("Merton", 3, 100, 2, 20),
    ("Newham", 2, 70, 1, 24),
    ("Redbridge", 2, 80, 1, 23),
    ("Richmond upon Thames", 3, 110, 2, 19),
    ("Southwark", 3, 110, 2, 16),
    ("Sutton", 2, 90, 1, 28),
    ("Tower Hamlets", 1, 50, 1, 30),
    ("Waltham Forest", 2, 80, 1, 22),
    ("Wandsworth", 4, 130, 3, 14),
    ("Westminster", 5, 200, 4, 8),
    ("City of London", 5, 200, 4, 8)
]

# ---------------- PROCESS ---------------- #
processed = []

for b, tube, train, bus, commute in transport_data:
    processed.append({
        "borough": b,
        "tube": tube,
        "train": train,
        "bus": bus,
        "commute": commute
    })

# ---------------- RANKING FUNCTIONS ---------------- #
def rank_desc(key):  # higher = better
    sorted_list = sorted(processed, key=lambda x: x[key], reverse=True)
    rank = 1
    prev = None
    for i, item in enumerate(sorted_list):
        if prev != item[key]:
            rank = i + 1
        item[f"rank_{key}"] = rank
        prev = item[key]

def rank_asc(key):  # lower = better
    sorted_list = sorted(processed, key=lambda x: x[key])
    rank = 1
    prev = None
    for i, item in enumerate(sorted_list):
        if prev != item[key]:
            rank = i + 1
        item[f"rank_{key}"] = rank
        prev = item[key]

# Apply ranking
rank_desc("tube")
rank_desc("train")
rank_desc("bus")
rank_asc("commute")   # ✅ lower is better

# ---------------- AVERAGE ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_tube"] +
        item["rank_train"] +
        item["rank_bus"] +
        item["rank_commute"]
    ) / 4

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
for item in processed:
    tree.insert("", tk.END, values=(
        item["borough"],
        item["tube"],
        item["train"],
        item["bus"],
        item["commute"],
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