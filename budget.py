import sqlite3
import pandas as pd
from datetime import datetime

def setup_budget_table():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute(''' 
     CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL
        )''')
    conn.commit()
    conn.close()


def set_budget(amount):
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM budget")
    cursor.execute("INSERT INTO budget (amount) VALUES (?)", (amount,))
    conn.commit()
    conn.close()

def get_budget():
    conn=sqlite3.connect("expenses.db")
    cursor=conn.cursor()
    cursor.execute("SELECT amount FROM budget ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0

def check_monthly_budget():
    conn = sqlite3.connect("expenses.db")
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()

    budget_limit = get_budget()
    if budget_limit==0:
        return 0,0,False
    if df.empty:
        return 0, budget_limit, False
    
    df['date'] = pd.to_datetime(df['date'])
    current_month = datetime.now().month
    current_year = datetime.now().year
    monthly_expenses = df[(df['date'].dt.month == current_month) & (df['date'].dt.year == current_year)]

    total_spent = monthly_expenses['amount'].sum()
    remaining_budget = budget_limit - total_spent
    if remaining_budget < 0:
        remaining_budget = 0
        
    exceeded = total_spent > budget_limit

    return total_spent, remaining_budget, exceeded

