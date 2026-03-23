import tkinter as tk
from tkinter import ttk
import subprocess
import sys
from PIL import Image, ImageTk

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("London Borough Finder")
root.geometry("1100x700")

# ---------------- HEADER ---------------- #
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
    text="SHOPPING ",
    font=("Arial", 16, "bold"),
    bg="white"
).pack()


# ---------------- TABLE ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ✅ Removed old ranking column, added new one at end
columns = (
    "Borough",
    "Retail Units",
    "No. of Shopping Centers",
    "No. of Malls",
    "High Street Score/10",
    "Number of Supermarkets",
    "Average Ranking"   # ✅ better name
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=160, anchor="center")

# ---------------- DATA ---------------- #
shopping_data = [
    ("Westminster", 5000, 10, 5, 9.5, 50),
    ("Barking and Dagenham", 800, 2, 0, 5.0, 10),
    ("Barnet", 2000, 5, 1, 7.0, 20),
    ("Bexley", 1500, 3, 0, 6.5, 15),
    ("Brent", 2500, 4, 1, 7.5, 25),
    ("Bromley", 1800, 3, 0, 6.8, 18),
    ("Camden", 3000, 6, 2, 8.0, 30),
    ("Croydon", 2200, 4, 1, 7.2, 22),
    ("Ealing", 1700, 3, 0, 6.9, 17),
    ("Enfield", 1600, 3, 0, 6.7, 16),
    ("Greenwich", 1900, 4, 1, 7.1, 19),
    ("Hackney", 2100, 5, 1, 7.3, 21),
    ("Hammersmith and Fulham", 2300, 5, 1, 7.4, 23),
    ("Haringey", 2000, 4, 1, 7.0, 20),
    ("Harrow", 1400, 2, 0, 6.5, 14),
    ("Havering", 1200, 2, 0, 6.3, 12),
    ("Hillingdon", 1600, 3, 0, 6.8, 16),
    ("Hounslow", 1800, 4, 1, 7.0, 18),
    ("Islington", 2500, 5, 1, 7.5, 25),
    ("Kensington and Chelsea", 2200, 4, 1, 7.2, 22),
    ("Kingston upon Thames", 1500, 3, 0, 6.8, 15),
    ("Lambeth", 2100, 5, 1, 7.3, 21),
    ("Lewisham", 1700, 3, 0, 6.9, 17),
    ("Merton", 1600, 3, 0, 6.7, 16),
    ("Newham", 1900, 4, 1, 7.1, 19),
    ("Redbridge", 1400, 2, 0, 6.5, 14),
    ("Richmond upon Thames", 1300, 2, 0, 6.4, 13),
    ("Southwark", 2000, 4, 1, 7.0, 20),
    ("Sutton", 1500, 3, 0, 6.8, 15),
    ("Tower Hamlets", 2200, 4, 1, 7.2, 22),
    ("Waltham Forest", 1600, 3, 0, 6.8, 16),
    ("Wandsworth", 1800, 4, 1, 7.0, 18),
    ("City of London", 3000, 6, 2, 8.0, 30)
]

# ---------------- PROCESS ---------------- #
processed = []

for b, r, sc, m, score, sup in shopping_data:
    processed.append({
        "borough": b,
        "retail": r,
        "centers": sc,
        "malls": m,
        "score": score,
        "supermarkets": sup
    })

# ---------------- RANKING (HIGHER = BETTER) ---------------- #
for key in ["retail", "centers", "malls", "score", "supermarkets"]:
    sorted_list = sorted(processed, key=lambda x: x[key], reverse=True)
    for i, item in enumerate(sorted_list):
        item[f"rank_{key}"] = i + 1

# ---------------- FINAL SCORE ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_retail"] +
        item["rank_centers"] +
        item["rank_malls"] +
        item["rank_score"] +
        item["rank_supermarkets"]
    ) / 5

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
# ---------------- INSERT ---------------- #
for item in processed:
    tree.insert("", tk.END, values=(
        item["borough"],
        item["retail"],
        item["centers"],
        item["malls"],
        item["score"],
        item["supermarkets"],
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