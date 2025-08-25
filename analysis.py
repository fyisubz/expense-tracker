import seaborn as sns
import matplotlib.pyplot as plt
from models import fetch_expenses

def visualise_by_category():
    df = fetch_expenses()
    if df.empty:
        print("No data")
        return
    
    plt.figure(figsize=(6,4))
    sns.barplot(x="category", y="amount", data=df, estimator=sum, ci=None)
    plt.title("Expenses by Category")
    plt.show()

def export_csv():
    df = fetch_expenses()
    if df.empty:
        print("No data")
        return
    else:
        df.to_csv("expenses.csv", index=False)