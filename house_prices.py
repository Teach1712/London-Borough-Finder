import tkinter as tk
from tkinter import ttk, messagebox
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

# ---------------- FUNCTIONS ---------------- #
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

tk.Button(header_frame, image=home_icon, bg="#3db4f2", bd=0, command=go_home).place(x=15, y=15)

# ---------------- NAV BAR ---------------- #
nav_frame = tk.Frame(root, bg="#2fa4de")
nav_frame.pack(fill="x")

buttons = [
    ("House prices", open_house_price),
    ("Education", open_education),
    ("Safety", open_safety),
    ("Shopping", open_shopping),
    ("Health and Fitness", open_health_fitness),
    ("Leisure", open_leisure),
    ("Transport", open_transport),
    ("Food", open_food),
    ("Support and Report", open_support_report)
]

for text, cmd in buttons:
    tk.Button(nav_frame, text=text, width=15, bg="#2fa4de", relief="flat", command=cmd)\
        .pack(side="left", padx=5, pady=5)

# ---------------- TITLE ---------------- #
tk.Label(root, text="AVERAGE HOUSE PRICES", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# ---------------- TABLE ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = (
    "Borough",
    "Average 1 Bedroom Price",
    "Average 2 Bedroom Price",
    "Average 3 Bedroom Price",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180, anchor="center")

# ---------------- DATA ---------------- #
houseprice_data = [
    ("Barnet", "£1,200", "£1,500", "£1,800"),
    ("Barking and Dagenham", "£900", "£1,100", "£1,300"),
    ("Bexley", "£1,000", "£1,200", "£1,500"),
    ("Brent", "£1,100", "£1,400", "£1,700"),
    ("Bromley", "£900", "£1,100", "£1,400"),
    ("Camden", "£1,500", "£1,800", "£2,200"),
    ("Croydon", "£1,000", "£1,300", "£1,600"),
    ("Ealing", "£1,100", "£1,400", "£1,800"),
    ("Enfield", "£1,000", "£1,300", "£1,600"),
    ("Greenwich", "£900", "£1,100", "£1,400"),
    ("Hackney", "£1,200", "£1,500", "£1,800"),
    ("Hammersmith and Fulham", "£1,400", "£1,700", "£2,100"),
    ("Haringey", "£1,000", "£1,300", "£1,600"),
    ("Harrow", "£900", "£1,100", "£1,400"),
    ("Havering", "£800", "£1,000", "£1,300"),
    ("Hillingdon", "£1,000", "£1,300", "£1,600"),
    ("Hounslow", "£1,100", "£1,400", "£1,800"),
    ("Islington", "£1,300", "£1,600", "£2,000"),
    ("Kensington and Chelsea", "£1,500", "£1,800", "£2,200"),
    ("Kingston upon Thames", "£900", "£1,100", "£1,400"),
    ("Lambeth", "£1,200", "£1,500", "£1,800"),
    ("Lewisham", "£900", "£1,100", "£1,400"),
    ("Merton", "£900", "£1,100", "£1,400"),
    ("Newham", "£900", "£1,100", "£1,400"),
    ("Redbridge", "£900", "£1,100", "£1,400"),
    ("Richmond upon Thames", "£900", "£1,100", "£1,400"),
    ("Southwark", "£1,200", "£1,500", "£1,800"),
    ("Sutton", "£900", "£1,100", "£1,400"),
    ("Tower Hamlets", "£900", "£1,100", "£1,400"),
    ("Waltham Forest"," £900"," £1,100"," £1,400"),
    ("Wandsworth", "£900", "£1,100", "£1,400"),
    ("Westminster", "£1,400", "£1,700", "£2,100"),
    ("City of London", "£1,500", "£1,800", "£2,200")
]

# ---------------- PROCESS ---------------- #
processed = []

for b, p1, p2, p3 in houseprice_data:
    processed.append({
        "borough": b,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "v1": int(p1.replace("£","").replace(",","")),
        "v2": int(p2.replace("£","").replace(",","")),
        "v3": int(p3.replace("£","").replace(",",""))
    })

# Rank each category
for key in ["v1", "v2", "v3"]:
    sorted_list = sorted(processed, key=lambda x: x[key])
    for i, item in enumerate(sorted_list):
        item[f"rank_{key}"] = i + 1

# Final score
for item in processed:
    item["score"] = (item["rank_v1"] + item["rank_v2"] + item["rank_v3"]) / 3

# Sort by score
processed.sort(key=lambda x: x["score"])

# Insert with average ranking (2 decimal places)
for item in processed:
    avg_rank = f"{item['score']:.2f}"  # format to 2 decimal places

    tree.insert("", tk.END, values=(
        item["borough"],
        item["p1"],
        item["p2"],
        item["p3"],
        avg_rank
    ))

tree.pack(fill="both", expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Footer
tk.Label(root, text="London Borough Finder © 2026").pack()

root.mainloop()