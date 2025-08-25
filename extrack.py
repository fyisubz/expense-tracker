import tkinter as tk
from tkinter import messagebox, ttk
from db import setup_database
from models import add_expense, fetch_expenses, summary_by_category
from analysis import visualise_by_category
from budget import setup_budget_table, set_budget, get_budget, check_monthly_budget
import sqlite3

setup_database()
setup_budget_table()


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("1020x600")

tk.Label(root, text="Category:").grid(row=0, column=0, padx=10, pady=5)
category_entry=tk.Entry(root)
category_entry.grid(row=0, column=1)

tk.Label(root, text="Amount").grid(row=1, column=0, padx=10, pady=5)
amount_entry=tk.Entry(root)
amount_entry.grid(row=1, column=1)

tk.Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=5)
desc_entry=tk.Entry(root)
desc_entry.grid(row=2, column=1)

def add_expense_action():
    category = category_entry.get()
    amount = amount_entry.get()
    desc = desc_entry.get()

    if not category or not amount:
        messagebox.showerror("Error", "Category and Amount are required")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return
    
    
    add_expense(category, amount, desc)
    messagebox.showinfo("Success", "Expense added")

    
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)

    load_expenses()

tk.Button(root, text="Add Expense", command=add_expense_action).grid(row=3, column=0, columnspan=2, pady=10)

columns = ("ID", "Date", "Category", "Amount", "Description")

tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


def load_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, category, amount, description FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("DEBUG rows:", rows)

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", tk.END, values=row)

load_expenses()


def view_expenses_action():
   load_expenses()

tk.Button(root, text="View Expenses", command=load_expenses).grid(row=5, column=0, pady=10)

def summary_action():
    summary = summary_by_category()
    if summary is None:
        messagebox.showinfo("Summary", "No data available")
    else:
        formatted_summary = "\n".join([f"{cat}: {amt:.2f}" for cat, amt in summary.items()])
        messagebox.showinfo("Summary by Category", formatted_summary)
        

tk.Button(root, text="Summary by Category", command=summary_action).grid(row=5, column=1, pady=5)
tk.Button(root, text="Visualise", command=visualise_by_category).grid(row=5, column=2, pady=5)

tk.Label(root, text="Budget:").grid(row=6, column=0, padx=10, pady=5)
budget_entry=tk.Entry(root)
budget_entry.grid(row=6, column=1)

saved_budget = get_budget()
if saved_budget:
    budget_entry.insert(0, str(saved_budget))


def set_budget_action():
    try:
        amount=float(budget_entry.get())
        set_budget(amount)
        messagebox.showinfo("Success", f"Budget set to {amount}")
        budget_entry.delete(0, tk.END)
        budget_entry.insert(0, str(amount))
    except ValueError:
        messagebox.showerror("Error", "Invalid budget amount")

tk.Button(root, text="Set Budget", command=set_budget_action).grid(row=6, column=2, pady=5)


def budget_alert_action():
    total_spent, remaining_budget, exceeded = check_monthly_budget()
    budget_limit = get_budget()

    msg = (
        f"Budget: {budget_limit:.2f}\n"
        f"Total Spent: {total_spent:.2f}\n"
        f"Remaining: {remaining_budget:.2f}"
    )

    if exceeded:
        messagebox.showwarning("Budget Alert", "Monthly budget exceeded!\n\n" + msg)
    else:
        messagebox.showinfo("Budget Status", msg)
            


tk.Button(root, text="Check Budget", command=budget_alert_action).grid(row=5, column=3, pady=5)
root.mainloop()



