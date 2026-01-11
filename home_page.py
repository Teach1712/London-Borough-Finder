import tkinter as tk
from tkinter import ttk, messagebox
import sys
import subprocess
# ---------------- SAMPLE DATA (can be replaced with real stats) ---------------- #
borough_data = [
    {"name": "Greenwich", "Safety": 2, "Education": 3, "House Prices": 4, "Leisure": 2, "Health": 3},
    {"name": "Lewisham", "Safety": 4, "Education": 4, "House Prices": 3, "Leisure": 3, "Health": 4},
    {"name": "Redbridge", "Safety": 3, "Education": 2, "House Prices": 2, "Leisure": 3, "Health": 2},
    {"name": "Bexley", "Safety": 5, "Education": 5, "House Prices": 4, "Leisure": 4, "Health": 5},
]

# Calculate average ranking
for b in borough_data:
    b["Average"] = round(sum(b[k] for k in b if k not in ["name", "Average"]) / 5, 2)

borough_data.sort(key=lambda x: x["Average"])  # best to worst

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
tk.Button(nav_frame, text="Health and Fitness", width=15, bg="#2fa4de",relief="flat",command=open_health_fitness).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Leisure", width=12, bg="#2fa4de",relief="flat",command=open_leisure).pack(side="left", padx=10, pady=5)
tk.Button(nav_frame, text="Transport", width=12, bg="#2fa4de",relief="flat",command=open_transport).pack(side="left", padx=10, pady=5)
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
    "Borough", "Safety", "Education", "House Prices",
    "Leisure", "Health", "Average"
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
        b["name"],
        b["Safety"],
        b["Education"],
        b["House Prices"],
        b["Leisure"],
        b["Health"],
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

factors = ["Safety", "Education", "House Prices", "Leisure", "Health"]
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
    output_entry.insert(0, best["name"])

btn_frame = tk.Frame(bottom_frame)
btn_frame.pack()

tk.Button(btn_frame, text="Search", width=15, command=find_best_borough).pack(side="left", padx=10)
tk.Button(btn_frame, text="Reset", width=15, command=lambda: output_entry.delete(0, tk.END)).pack(side="left", padx=10)

root.mainloop()
