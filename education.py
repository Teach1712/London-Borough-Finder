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
    text="EDUCATION",
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
columns = (
    "Borough",
    "No. of Primary Schools",
    "No. of Secondary Schools",
    "No. of Colleges",
    "No. of University",
    "Notable University",
    "Notable Colleges",
    "Average Ranking"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

# ---------------- SAMPLE DATA ---------------- #
education_data = [
    ("Camden", 38, 12,6,3,"University College London","SOAS University of London"),
    ("Westminster", 30, 10,5,2,"University of Westminster","Royal College of Art"),
    ("Barking and Dagenham", 25, 8,4,1,"None","None"),
    ("Barnet", 40, 15,7,4,"Barnet College","None"),
    ("Bexley", 28, 9,5,2,"None","None"),
    ("Brent", 35, 12,6,3,"None","None"),
    ("Bromley", 32, 10,5,2,"None","None"),
    ("Croydon", 30, 11,5,2,"None","None"),
    ("Ealing", 33, 13,6,3,"None","None"),
    ("Enfield", 29, 9,5,2,"None","None"),
    ("Greenwich", 31, 10,5,2,"None","None"),
    ("Hackney", 27, 8,4,1,"None","None"),
    ("Hammersmith and Fulham", 34, 12,6,3,"None","None"),
    ("Haringey", 28, 9,5,2,"None","None"),
    ("Harrow", 30, 10,5,2,"None","None"),
    ("Havering", 26, 7,4,1,"None","None"),
    ("Hillingdon", 29, 11,5,2,"None","None"),
    ("Hounslow", 31, 12,6,3,"None","None"),
    ("Islington", 36, 14,7,4,"City University of London","London Metropolitan University"),
    ("Kensington and Chelsea", 33, 13,6,3,"Imperial College London","Royal College of Art"),
    ("Kingston upon Thames", 27, 9,5,2,"None","None"),
    ("Lambeth", 30, 10,5,2,"None","None"),
    ("Lewisham", 28, 9,5,2,"None","None"),
    ("Merton", 29, 11,5,2,"None","None"),
    ("Newham", 26, 7,4,1,"None","None"),
    ("Redbridge", 30, 10,5,2,"None","None"),
    ("Richmond upon Thames", 32, 12,6,3,"None","None"),
    ("Southwark", 28, 9,5,2,"None","None"),
    ("Sutton", 27, 8,4,1,"None","None"),
    ("Tower Hamlets", 25, 7,4,1,"Queen Mary University of London","None"),
    ("Waltham Forest", 26, 7,4,1,"None","None"),
    ("Wandsworth", 28, 9,5,2,"None","None"),
    ("City of London", 40, 15,7,4,"None","None")
]


# ---------------- PROCESS DATA ---------------- #
processed = []

for b, p, s, c, u, uni_name, col_name in education_data:
    processed.append({
        "borough": b,
        "primary": p,
        "secondary": s,
        "college": c,
        "uni": u,
        "uni_name": uni_name,
        "col_name": col_name
    })

# ---------------- RANK EACH CATEGORY ---------------- #
for key in ["primary", "secondary", "college", "uni"]:
    sorted_list = sorted(processed, key=lambda x: x[key], reverse=True)  # highest = best

    for i, item in enumerate(sorted_list):
        item[f"rank_{key}"] = i + 1

# ---------------- AVERAGE RANK ---------------- #
for item in processed:
    item["avg_rank"] = (
        item["rank_primary"] +
        item["rank_secondary"] +
        item["rank_college"] +
        item["rank_uni"]
    ) / 4

# ---------------- SORT ---------------- #
processed.sort(key=lambda x: x["avg_rank"])

# ---------------- INSERT ---------------- #
for item in processed:
    avg_rank = f"{item['avg_rank']:.2f}"

    tree.insert("", tk.END, values=(
        item["borough"],
        item["primary"],
        item["secondary"],
        item["college"],
        item["uni"],
        item["uni_name"],
        item["col_name"],
        avg_rank
    ))



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
