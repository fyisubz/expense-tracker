import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from models import fetch_expenses, monthly_summary
from tkinter import messagebox, simpledialog, filedialog

def visualise_by_category():
    df = fetch_expenses()
    if df.empty:
        print("No data")
        return
    
    plt.figure(figsize=(6,4))
    sns.barplot(x="category", y="amount", data=df, estimator=sum, ci=None)
    plt.title("Expenses by Category")
    plt.show()


    
    summary = summary.reset_index()
    summary['month_year'] = summary['month_year'].astype(str)

    plt.figure(figsize=(8,5))
    sns.barplot(x="month_year", y="amount", data=summary, ci=None)
    plt.title("Monthly Expenditure")
    plt.xticks(rotation=45)
    plt.show()

def visualise_monthly_summary():
    summary = monthly_summary()
    if summary is None:
        messagebox.showinfo("Monthly Summary", "No data available")
        return
    summary.plot(kind='bar', figsize=(8,5), title="Monthly Expenditure")
    plt.xlabel("Month-Year")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()


def visualise_monthly_expenditure():
    df = fetch_expenses()
    if df.empty:
        print("No data")
        return
    
    df['date']=pd.to_datetime(df['date'], errors='coerce')
    df['month']=df['date'].dt.to_period('M')
    monthly_summary=df.groupby('month')['amount'].sum().reset_index()

    monthly_summary['month']=monthly_summary['month'].astype(str)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='month', y='amount', data=monthly_summary, ci=None)

    plt.title('Monthly Expenditure', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Total Amount', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def export_expenses():

    choice = simpledialog.askstring(
        "Export Choice",
        "Do you want to export 'monthly' or 'yearly' data?"
    )
    if not choice:
        return

    df = fetch_expenses()
    if df.empty:
        messagebox.showinfo("Export", "No data available to export")
        return

    
    try:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
    except Exception as e:
        messagebox.showerror("Error", f"Date parsing failed: {e}")
        return

    if choice.lower() == "monthly":
        year = simpledialog.askinteger("Year", "Enter the year (e.g., 2025):")
        month = simpledialog.askinteger("Month", "Enter the month (1-12):")

        if year is None or month is None:
            return

        monthly_df = df[(df["date"].dt.year == year) & (df["date"].dt.month == month)]

        if monthly_df.empty:
            messagebox.showinfo("No data", "No expenses found for this month.")
            return

        
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title=f"Save Expenses for {year}-{month:02d}"
        )
        if filename:
            
            monthly_df = monthly_df[["date", "category", "amount", "description"]]
            monthly_df.to_csv(filename, index=False)
            messagebox.showinfo("Export", f"Monthly expenses exported successfully to {filename}")

    elif choice.lower() == "yearly":
        year = simpledialog.askinteger("Year", "Enter the year (e.g., 2025):")
        if year is None:
            return

        yearly_df = df[df["date"].dt.year == year]

        if yearly_df.empty:
            messagebox.showinfo("No data", "No expenses found for this year.")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title=f"Save Expenses for {year}"
        )
        if filename:
            yearly_df = yearly_df[["date", "category", "amount", "description"]]
            yearly_df.to_csv(filename, index=False)
            messagebox.showinfo("Export", f"Yearly expenses exported successfully to {filename}")

    else:
        messagebox.showerror("Invalid Choice", "Please enter 'monthly' or 'yearly'.")


def export_csv():
    df = fetch_expenses()
    if df.empty:
        print("No data")
        return
    else:
        df.to_csv("expenses.csv", index=False)