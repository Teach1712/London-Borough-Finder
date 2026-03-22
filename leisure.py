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
    text="LEISURE",
    font=("Arial", 16, "bold"),
    bg="white"
).pack()


# ---------------- TABLE FRAME ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ---------------- UPDATED COLUMNS ---------------- #
columns = (
    "Borough",
    "Leisure Centers",
    "Restaurants",
    "Cinemas",
    "Museums",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# ---------------- DATA ---------------- #
leisure_data = [
    ("Camden", 5, 200, 3, 10),
    ("Barking and Dagenham", 2, 50, 1, 3),
    ("Barnet", 4, 150, 2, 8),
    ("Bexley", 3, 80, 1, 5),
    ("Brent", 6, 220, 4, 12),
    ("Bromley", 4, 120, 2, 7),
    ("Croydon", 5, 180, 3, 9),
    ("Ealing", 4, 160, 2, 8),
    ("Enfield", 3, 100, 1, 6),
    ("Greenwich", 7, 250, 5, 15),
    ("Hackney", 4, 130, 2, 7),
    ("Hammersmith and Fulham", 5, 190, 3, 10),
    ("Haringey", 3, 80, 1, 5),
    ("Harrow", 4, 140, 2, 7),
    ("Havering", 5, 170, 3, 9),
    ("Hillingdon", 6, 200, 4, 12),
    ("Hounslow", 4, 120, 2, 7),
    ("Islington", 5, 210, 4, 11),
    ("Kensington and Chelsea", 7, 300, 6, 20),
    ("Kingston upon Thames", 4, 150, 2, 8),
    ("Lambeth", 5, 180, 3, 9),
    ("Lewisham", 3, 90, 1, 5),
    ("Merton", 4, 140, 2, 7),
    ("Newham", 5, 190, 3, 10),
    ("Redbridge", 4, 130, 2, 7),
    ("Richmond upon Thames", 6, 220, 4, 12),
    ("Southwark", 5, 170, 3, 9),
    ("Sutton", 3, 80, 1, 5),
    ("Tower Hamlets", 4, 120, 2, 7),
    ("Waltham Forest", 5, 180, 3, 9),
    ("Wandsworth", 4, 140, 2, 7),
    ("Westminster", 6, 250, 5, 15),
    ("City of London", 6, 250, 5, 15),
]

# ---------------- PROCESS ---------------- #
processed = []

for b, lc, rest, cin, mus in leisure_data:
    processed.append({
        "borough": b,
        "lc": lc,
        "rest": rest,
        "cin": cin,
        "mus": mus
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

rank_desc("lc")
rank_desc("rest")
rank_desc("cin")
rank_desc("mus")

# ---------------- AVERAGE ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_lc"] +
        item["rank_rest"] +
        item["rank_cin"] +
        item["rank_mus"]
    ) / 4

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
for item in processed:
    tree.insert("", tk.END, values=(
        item["borough"],
        item["lc"],
        item["rest"],
        item["cin"],
        item["mus"],
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