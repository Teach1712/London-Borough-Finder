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

# ---------------- FUNCTIONS ---------------- #
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

tk.Button(header_frame, image=home_icon, bg="#3db4f2",
          bd=0, command=go_home).place(x=15, y=15)

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
tk.Label(root, text="SAFETY PAGE", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# ---------------- TABLE FRAME ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

# ---------------- COLUMNS ---------------- #
columns = (
    "Borough",
    "Crime Rate",
    "Common Crimes",
    "Trend",
    "Response",
    "Feel Safe",
    "Stations",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor="center")

# ---------------- DATA ---------------- #
safety_data = [
    ("Barking and Dagenham", 45, "Theft, Vandalism","⬇ 1%","10 mins","74%",2),
    ("Barnet", 40, "Theft, Burglary","⬆ 2%","12 mins","80%",1),
    ("Bexley", 35, "Theft, Burglary","⬆ 3%","11 mins","77%",1),
    ("Brent", 55, "Assault, Theft","⬇ 4%","9 mins","73%",3),
    ("Bromley", 30, "Theft, Vandalism","⬆ 2%","12 mins","79%",1),
    ("Croydon", 60, "Assault, Theft","⬇ 2%","8 mins","70%",4),
    ("Ealing", 50, "Theft, Burglary","⬆ 1%","10 mins","76%",2),
    ("Enfield", 45, "Theft, Vandalism","⬇ 3%","9 mins","74%",3),
    ("Camden", 68, "Theft, Assault","⬇ 4%","8 mins","75%",3),
    ("Greenwich", 55, "Theft, Burglary","⬆ 2%","10 mins","70%",2),
    ("Hackney", 80, "Assault, Theft","⬇ 1%","7 mins","65%",4),
    ("Hammersmith and Fulham", 60, "Theft, Vandalism","⬆ 3%","9 mins","72%",3),
    ("Haringey", 70, "Assault, Theft","⬆ 4%","7 mins","68%",4),
    ("Harrow", 25, "Theft, Burglary","⬇ 1%","13 mins","82%",1),
    ("Havering", 20, "Theft, Vandalism","⬆ 2%","14 mins","85%",1),
    ("Hillingdon", 40, "Assault, Theft","⬇ 2%","9 mins","75%",3),
    ("Hounslow", 55, "Theft, Burglary","⬆ 3%","10 mins","73%",2),
    ("Islington", 75, "Assault, Theft","⬇ 5%","6 mins","68%",5),
    ("Kensington and Chelsea", 50, "Theft, Burglary","⬆ 1%","11 mins","78%",2),
    ("Lambeth", 85, "Assault, Theft","⬇ 2%","8 mins","66%",4),
    ("Lewisham", 65, "Theft, Vandalism","⬆ 4%","9 mins","71%",3),
    ("Southwark", 70, "Assault, Theft","⬇ 3%","7 mins","69%",4),
    ("Sutton", 30, "Theft, Burglary","⬆ 2%","12 mins","80%",1),
    ("Tower Hamlets", 45, "Theft, Vandalism","⬇ 1%","10 mins","74%",2),
    ("Kingston upon Thames", 35, "Theft, Burglary","⬆ 3%","11 mins","77%",1),
    ("Waltham Forest", 50, "Assault, Theft","⬇ 2%","9 mins","75%",3),
    ("Merton", 40, "Theft, Vandalism","⬆ 2%","10 mins","76%",2),
    ("Newham", 60, "Assault, Theft","⬇ 3%","8 mins","70%",4),
    ("Redbridge", 45, "Theft, Burglary","⬆ 1%","11 mins","74%",2),
    ("Richmond upon Thames", 25, "Theft, Vandalism","⬇ 1%","13 mins","82%",1),
    ("Wandsworth", 55, "Assault, Theft","⬆ 2%","9 mins","73%",3),
    ("Westminster", 70, "Theft, Burglary","⬇ 4%","7 mins","69%",4),
    ("City of London", 30, "Theft, Vandalism","⬆ 3%","12 mins","80%",1)
]

# ---------------- PROCESS ---------------- #
processed = []

for b, crime, crimes, trend, response, safe, stations in safety_data:
    processed.append({
        "borough": b,
        "crime": crime,
        "crimes": crimes,
        "trend": trend,
        "response": int(response.replace(" mins","")),
        "safe": int(safe.replace("%","")),
        "stations": stations
    })

# ---------------- RANKING ---------------- #
for key in ["crime", "response"]:
    sorted_list = sorted(processed, key=lambda x: x[key])
    for i, item in enumerate(sorted_list):
        item[f"rank_{key}"] = i + 1

for key in ["safe", "stations"]:
    sorted_list = sorted(processed, key=lambda x: x[key], reverse=True)
    for i, item in enumerate(sorted_list):
        item[f"rank_{key}"] = i + 1

# ---------------- AVERAGE ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_crime"] +
        item["rank_response"] +
        item["rank_safe"] +
        item["rank_stations"]
    ) / 4

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
for item in processed:
    tree.insert("", tk.END, values=(
        item["borough"],
        item["crime"],
        item["crimes"],
        item["trend"],
        f"{item['response']} mins",
        f"{item['safe']}%",
        item["stations"],
        f"{item['avg_rank']:.2f}"
    ))

tree.pack(fill="both", expand=True)

# ---------------- SCROLLBAR ---------------- #
scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# ---------------- FOOTER ---------------- #
tk.Label(root, text="London Borough Finder © 2026").pack()

root.mainloop()