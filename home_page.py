import tkinter as tk
from tkinter import ttk, messagebox
import sys
import subprocess
# ---------------- SAMPLE DATA (can be replaced with real stats) ---------------- #
borough_data = [
    {"Name": "Barking and Dagenham", "Safety": 15.50, "Food": 32.00, "Transport": 28.00, "Leisure": 31.75, "Health & Fitness": 31.00, "Shopping": 29.40, "Education": 28.25, "House Prices": 1.67},
    {"Name": "Barnet", "Safety": 16.25, "Food": 15.00, "Transport": 21.50, "Leisure": 17.25, "Health & Fitness": 22.50, "Shopping": 9.20, "Education": 1.00, "House Prices": 23.33},
    {"Name": "Bexley", "Safety": 16.25, "Food": 27.20, "Transport": 29.75, "Leisure": 28.75, "Health & Fitness": 28.00, "Shopping": 23.80, "Education": 16.25, "House Prices": 16.00},
    {"Name": "Brent", "Safety": 14.50, "Food": 3.20, "Transport": 12.75, "Leisure": 4.50, "Health & Fitness": 20.00, "Shopping": 5.20, "Education": 5.50, "House Prices": 21.00},
    {"Name": "Bromley", "Safety": 16.50, "Food": 16.80, "Transport": 21.50, "Leisure": 19.75, "Health & Fitness": 14.50, "Shopping": 19.20, "Education": 12.50, "House Prices": 3.00},
    {"Name": "Camden", "Safety": 14.50, "Food": 4.20, "Transport": 6.00, "Leisure": 8.50, "Health & Fitness": 9.50, "Shopping": 2.00, "Education": 4.25, "House Prices": 31.00},
    {"Name": "Croydon", "Safety": 14.00, "Food": 10.60, "Transport": 9.00, "Leisure": 10.25, "Health & Fitness": 1.75, "Shopping": 7.80, "Education": 13.25, "House Prices": 17.00},
    {"Name": "Ealing", "Safety": 15.75, "Food": 21.00, "Transport": 6.50, "Leisure": 17.00, "Health & Fitness": 5.75, "Shopping": 20.40, "Education": 5.75, "House Prices": 22.33},
    {"Name": "Enfield", "Safety": 12.75, "Food": 28.40, "Transport": 19.00, "Leisure": 28.00, "Health & Fitness": 9.25, "Shopping": 23.00, "Education": 17.25, "House Prices": 18.00},
    {"Name": "Greenwich", "Safety": 21.00, "Food": 1.00, "Transport": 19.00, "Leisure": 1.75, "Health & Fitness": 15.50, "Shopping": 12.00, "Education": 14.75, "House Prices": 4.00},
    {"Name": "Hackney", "Safety": 17.50, "Food": 25.40, "Transport": 8.75, "Leisure": 19.25, "Health & Fitness": 30.25, "Shopping": 8.00, "Education": 27.50, "House Prices": 24.67},
    {"Name": "Hammersmith and Fulham", "Safety": 17.75, "Food": 5.40, "Transport": 3.75, "Leisure": 9.00, "Health & Fitness": 24.75, "Shopping": 6.60, "Education": 7.00, "House Prices": 29.00},
    {"Name": "Haringey", "Safety": 16.25, "Food": 30.00, "Transport": 11.25, "Leisure": 28.75, "Health & Fitness": 28.25, "Shopping": 12.60, "Education": 19.50, "House Prices": 19.00},
    {"Name": "Harrow", "Safety": 15.75, "Food": 16.80, "Transport": 28.50, "Leisure": 18.50, "Health & Fitness": 23.00, "Shopping": 28.20, "Education": 17.00, "House Prices": 5.00},
    {"Name": "Havering", "Safety": 16.00, "Food": 15.00, "Transport": 33.00, "Leisure": 11.00, "Health & Fitness": 20.00, "Shopping": 30.40, "Education": 29.25, "House Prices": 1.33},
    {"Name": "Hillingdon", "Safety": 12.50, "Food": 10.60, "Transport": 21.00, "Leisure": 5.25, "Health & Fitness": 12.50, "Shopping": 23.40, "Education": 17.25, "House Prices": 20.00},
    {"Name": "Hounslow", "Safety": 20.50, "Food": 16.80, "Transport":13.50, "Leisure": 19.75, "Health & Fitness": 9.25, "Shopping": 15.20, "Education": 9.25, "House Prices": 23.67},
    {"Name": "Islington", "Safety": 16.00, "Food": 4.20, "Transport": 6.75, "Leisure": 7.00, "Health & Fitness": 4.25, "Shopping": 6.80, "Education": 2.75, "House Prices": 28.00},
    {"Name": "Kensington and Chelsea", "Safety": 17.50, "Food": 3.20, "Transport": 2.50, "Leisure": 1.00, "Health & Fitness": 2.25, "Shopping": 10.60, "Education": 7.75, "House Prices": 32.00},
    {"Name": "Kingston upon Thames", "Safety": 18.50, "Food": 15.00, "Transport": 29.50, "Leisure": 17.25, "Health & Fitness": 21.75, "Shopping": 25.60, "Education": 22.50, "House Prices": 6.00},
    {"Name": "Lambeth", "Safety": 19.50, "Food": 16.80, "Transport": 8.75, "Leisure": 10.25, "Health & Fitness": 29.50, "Shopping": 10.40, "Education": 19.00, "House Prices": 26.00},
    {"Name": "Lewisham", "Safety": 19.50, "Food": 25.00, "Transport": 19.25, "Leisure": 28.50, "Health & Fitness": 14.50, "Shopping": 23.00, "Education": 22.75, "House Prices": 7.00},
    {"Name": "Merton", "Safety": 17.00, "Food": 25.60, "Transport": 21.25, "Leisure": 18.50, "Health & Fitness": 12.50, "Shopping": 26.00, "Education": 19.75, "House Prices": 8.00},
    {"Name": "Newham", "Safety": 17.00, "Food": 3.60, "Transport": 11.75, "Leisure": 9.00, "Health & Fitness": 22.25, "Shopping": 15.00, "Education": 30.25, "House Prices": 9.00},
    {"Name": "Redbridge", "Safety": 21.00, "Food": 16.80, "Transport": 21.25, "Leisure": 19.25, "Health & Fitness": 9.00, "Shopping": 30.40, "Education": 21.00, "House Prices": 10.00},
    {"Name": "Richmond upon Thames", "Safety": 17.50, "Food": 10.60, "Transport": 13.75, "Leisure": 4.50, "Health & Fitness": 5.00, "Shopping": 31.40, "Education": 10.00, "House Prices": 11.00},
    {"Name": "Southwark", "Safety": 16.75, "Food": 11.40, "Transport": 6.25, "Leisure": 11.00, "Health & Fitness": 8.75, "Shopping": 15.40, "Education": 24.75, "House Prices": 27.00},
    {"Name": "Sutton", "Safety": 17.25, "Food": 25.60, "Transport": 28.00, "Leisure": 28.75, "Health & Fitness": 13.50, "Shopping": 27.80, "Education": 29.75, "House Prices": 12.00},
    {"Name": "Tower Hamlets", "Safety": 18.75, "Food": 3.60, "Transport": 12.25, "Leisure": 19.75, "Health & Fitness": 20.00, "Shopping": 12.60, "Education": 32.25, "House Prices": 13.00},
    {"Name": "Waltham Forest", "Safety": 15.75, "Food": 16.80, "Transport": 21.50, "Leisure": 10.25, "Health & Fitness": 9.25, "Shopping": 27.20, "Education": 32.50, "House Prices": 14.00},
    {"Name": "Wandsworth", "Safety": 19.00, "Food": 25.20, "Transport": 7.50, "Leisure": 18.50, "Health & Fitness": 2.75, "Shopping": 18.40, "Education": 25.75, "House Prices": 15.00},
    {"Name": "Westminster", "Safety": 18.00, "Food": 3.20, "Transport": 1.00, "Leisure": 2.25, "Health & Fitness": 4.25, "Shopping": 1.00, "Education": 12.25, "House Prices": 30.00},
    {"Name": "City of London", "Safety": 18.75, "Food": 4.20, "Transport": 2.75, "Leisure": 2.25, "Health & Fitness": 1.00, "Shopping": 3.00, "Education": 2.50, "House Prices": 33.00}
    
]

# Calculate average ranking
for b in borough_data:
    values = [
        b["Safety"], b["Food"], b["Transport"], b["Leisure"],
        b["Health & Fitness"], b["Shopping"], b["Education"], b["House Prices"]
    ]
    b["Average"] = round(sum(values) / len(values), 2) # best to worst

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("London Borough Finder")
root.geometry("1100x700")

# ---------------- TOP TITLE ---------------- #
top_frame = tk.Frame(root, bg="#3db4f2", height=80)
top_frame.pack(fill="x")

tk.Label(
    top_frame,
    text="London borough finder",
    font=("Arial", 24, "bold"),
    bg="#3db4f2"
).pack(pady=20)

# ---------------- OPEN OTHER PAGES ---------------- #
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


# ---------------- NAVIGATION BAR ---------------- #
nav_frame = tk.Frame(root, bg="#2fa4de")
nav_frame.pack(fill="x")

tk.Button(nav_frame, text="House prices", width=12,relief="flat", bg="#2fa4de",command=open_house_price).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Education", width=12, bg="#2fa4de",relief="flat",command=open_education).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Safety", width=12, bg="#2fa4de",relief="flat",command=open_safety).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Shopping", width=12, bg="#2fa4de",relief="flat",command=open_shopping).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Health & Fitness", width=15, bg="#2fa4de",relief="flat",command=open_health_fitness).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Leisure", width=12, bg="#2fa4de",relief="flat",command=open_leisure).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Transport", width=12, bg="#2fa4de",relief="flat",command=open_transport).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Food", width=12, bg="#2fa4de",relief="flat",command=open_food).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Support and Report", width=15, bg="#2fa4de",relief="flat",command=open_support_report).pack(side="left", padx=10, pady=5)


# ---------------- DESCRIPTION ---------------- #
desc_frame = tk.Frame(root)
desc_frame.pack(pady=15)

tk.Label(
    desc_frame,
    text="Find your ideal borough to stay in London using the London borough finder!",
    font=("Arial", 12)
).pack()

tk.Label(
    desc_frame,
    text="Description of the program",
    font=("Arial", 10, "italic")
).pack()

# ---------------- TABLE ---------------- #
table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=10, fill="both", expand=True)

columns = (
    "Name", "Safety", "Food", "Transport",
    "Leisure", "Health & Fitness", "Shopping",
    "Education", "House Prices", "Average"
)

tree = ttk.Treeview(table_frame, columns=columns, show="headings")
tree.pack(side="left", fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

for b in borough_data:
    tree.insert("", "end", values=(
        b["Name"],
        b["Safety"],
        b["Food"],
        b["Transport"],
        b["Leisure"],
        b["Health & Fitness"],
        b["Shopping"],
        b["Education"],
        b["House Prices"],
        b["Average"]
    ))

# ---------------- PREFERENCE SELECTOR ---------------- #
bottom_frame = tk.Frame(root, bd=2, relief="groove")
bottom_frame.pack(pady=20, padx=20, fill="x")

tk.Label(
    bottom_frame,
    text="Your most preferred borough:",
    font=("Arial", 14, "bold")
).pack(anchor="w", pady=5)

tk.Label(
    bottom_frame,
    text="Select up to 3 most important factors:",
    font=("Arial", 10)
).pack(anchor="w")

factors = ["Safety", "Education", "House Prices", "Leisure", "Health & Fitness", "Shopping", "Transport", "Food"]
selected = {}

check_frame = tk.Frame(bottom_frame)
check_frame.pack(anchor="w")

def toggle_limit():
    if sum(v.get() for v in selected.values()) > 3:
        messagebox.showwarning("Limit", "You can select only 3 factors")
        for v in selected.values():
            v.set(0)

for f in factors:
    selected[f] = tk.IntVar()
    tk.Checkbutton(
        check_frame,
        text=f,
        variable=selected[f],
        command=toggle_limit
    ).pack(side="left", padx=10)

output_entry = tk.Entry(bottom_frame, width=40)
output_entry.pack(pady=10)

def find_best_borough():
    chosen = [k for k, v in selected.items() if v.get() == 1]
    if len(chosen) == 0:
        messagebox.showerror("Error", "Select at least one factor")
        return

    best = min(
        borough_data,
        key=lambda b: sum(b[f] for f in chosen) / len(chosen)
    )

    output_entry.delete(0, tk.END)
    output_entry.insert(0, best["Name"])

btn_frame = tk.Frame(bottom_frame)
btn_frame.pack()

tk.Button(btn_frame, text="Search", width=15, command=find_best_borough).pack(side="left", padx=10)
tk.Button(btn_frame, text="Reset", width=15, command=lambda: output_entry.delete(0, tk.END)).pack(side="left", padx=10)

root.mainloop()
