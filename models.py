from datetime import datetime
import pandas as pd
from db import get_connection

def add_expense(category, amount, description=""):
    conn = get_connection()
    cursor = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("insert into expenses (date, category, amount, description) values (?, ?, ?, ?)", (date, category, amount, description))
    conn.commit()
    conn.close()

def fetch_expenses():
    conn = get_connection()
    df = pd.read_sql("select * from expenses", conn)
    conn.close()
    return df

def summary_by_category():
    df = fetch_expenses()
    if df.empty:
        return None
    return df.groupby("category")["amount"].sum()

def summary_by_date():
    df = fetch_expenses()
    if df.empty:
        return None
    return df.groupby("date")["amount"].sum()


def monthly_summary():
    df = fetch_expenses()
    if df.empty:
        return None

    df['date'] = pd.to_datetime(df["date"])
    df["month_year"] = df["date"].dt.to_period("M")

    return df.groupby("month_year")['amount'].sum()




