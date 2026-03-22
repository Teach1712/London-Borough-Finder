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
    text="FOOD",
    font=("Arial", 16, "bold"),
    bg="white"
).pack()



# ---------------- TABLE FRAME ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)


# ---------------- COLUMNS ---------------- #
columns = (
    "Borough",
    "No. of Restaurants",
    "No. of Cafes",
    "No. of Bars",
    "No. of Fast Food Chains",
    "No. of Bakeries",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# ---------------- DATA ---------------- #
food_data = [
    ("Camden", 150, 80, 50, 30, 20),
    ("Barking and Dagenham", 40, 20, 10, 5, 3),
    ("Barnet", 120, 60, 40, 20, 10),
    ("Bexley", 90, 40, 20, 15, 5),
    ("Brent", 180, 90, 60, 30, 15),
    ("Bromley", 110, 50, 30, 20, 10),
    ("Croydon", 130, 65, 45, 25, 15),
    ("Ealing", 100, 45, 30, 15, 10),
    ("Enfield", 80, 35, 25, 10, 5),
    ("Greenwich", 200, 100, 70, 40, 20),
    ("Hackney", 95, 45, 25, 15, 5),
    ("Hammersmith and Fulham", 160, 80, 50, 30, 15),
    ("Haringey", 70, 30, 15, 10, 5),
    ("Harrow", 110, 50, 30, 20, 10),
    ("Havering", 120, 60, 40, 20, 10),
    ("Hillingdon", 130, 65, 45, 25, 15),
    ("Hounslow", 110, 50, 30, 20, 10),
    ("Islington", 150, 80, 50, 30, 20),
    ("Kensington and Chelsea", 180, 90, 60, 30, 15),
    ("Kingston upon Thames", 120, 60, 40, 20, 10),
    ("Lambeth", 110, 50, 30, 20, 10),
    ("Lewisham", 100, 40, 25, 15, 8),
    ("Merton", 90, 45, 25, 15, 5),
    ("Newham", 170, 80, 50, 30, 20),
    ("Redbridge", 110, 50, 30, 20, 10),
    ("Richmond upon Thames", 130, 65, 45, 25, 15),
    ("Southwark", 125, 65, 42, 27, 17),
    ("Tower Hamlets", 170, 80, 50, 30, 20),
    ("Waltham Forest", 110, 50, 30, 20, 10),
    ("Wandsworth", 100, 40, 25, 15, 8),
    ("Westminster", 180, 90, 60, 30, 15),
    ("City of London", 150, 80, 50, 30, 20)
]

# ---------------- PROCESS ---------------- #
processed = []

for b, r, c, bars, fast, bake in food_data:
    processed.append({
        "borough": b,
        "restaurants": r,
        "cafes": c,
        "bars": bars,
        "fast": fast,
        "bakeries": bake
    })

# ---------------- RANK FUNCTION ---------------- #
def assign_rank(data, key, reverse=True):
    sorted_list = sorted(data, key=lambda x: x[key], reverse=reverse)
    rank = 1
    prev = None

    for i, item in enumerate(sorted_list):
        if prev != item[key]:
            rank = i + 1
        item[f"rank_{key}"] = rank
        prev = item[key]

# Apply ranking (higher = better)
assign_rank(processed, "restaurants")
assign_rank(processed, "cafes")
assign_rank(processed, "bars")
assign_rank(processed, "fast")
assign_rank(processed, "bakeries")

# ---------------- AVERAGE RANK ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_restaurants"] +
        item["rank_cafes"] +
        item["rank_bars"] +
        item["rank_fast"] +
        item["rank_bakeries"]
    ) / 5

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
for item in processed:
    tree.insert("", tk.END, values=(
        item["borough"],
        item["restaurants"],
        item["cafes"],
        item["bars"],
        item["fast"],
        item["bakeries"],
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