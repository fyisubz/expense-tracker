# Expense Tracker

We developed a comprehensive **Expense Tracker** application using Python with SQLite database, Tkinter GUI, and advanced data analytics for efficient personal finance management.

• On the **backend**, we created an expense tracking system with SQLite for CRUD operations, budget tracking, and financial analysis with comprehensive data storage and retrieval.

• We integrated sample data and implemented core functionalities: adding, updating, deleting, and viewing expenses with budget management and detailed analysis reports.

• On the **frontend**, we built a **Tkinter GUI** with interactive charts using **Pandas** for data manipulation and **Matplotlib** for beautiful data visualizations and expense analytics.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Tkinter](https://img.shields.io/badge/tkinter-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

## 📸 Application Screenshots

### Main Dashboard
![Main Dashboard](images/dashboard.png)
*Clean and intuitive interface showing expense entry form, data table, and budget management controls*

### Data Visualization
![Expense Analytics](images/analytics-chart.png)
*Interactive bar charts showing expenses by category with detailed breakdowns for Food, Laptop, and College expenses*

### Expense Management
![Expense List](images/expense-list.png)
*Comprehensive expense tracking table with ID, Date, Category, Amount, and Description columns for easy data management*

## 📁 Project Structure

```
ExpenseTracker/
├── images/                 # Screenshot assets
│   ├── dashboard.png
│   ├── analytics-chart.png
│   └── expense-list.png
├── extrack.py              # Main GUI application
├── db.py                   # Database operations
├── models.py               # Data models
├── budget.py               # Budget management
├── analysis.py             # Financial analytics
├── requirements.txt        # Dependencies
├── expenses.db             # SQLite database
└── README.md               # Documentation
```

## ✨ Features

• **Expense Management**: Add, update, delete expense records with category organization
• **Budget Tracking**: Set budgets with real-time monitoring and visual alerts
• **Data Analytics**: Advanced analytics using Pandas with interactive Matplotlib charts
• **Visual Reports**: Bar charts, category summaries, and spending pattern analysis
• **Database Integration**: Reliable SQLite storage with efficient data retrieval
• **Export Functionality**: Export expense data in multiple formats (CSV, Excel)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+ with tkinter
- Required packages: pandas, matplotlib, sqlite3

### Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run application:
```bash
python extrack.py
```

## 📊 Core Modules

- **extrack.py** - Main Tkinter GUI with form inputs and data display
- **db.py** - SQLite database management and CRUD operations
- **models.py** - Data models with validation and structure
- **budget.py** - Budget setting, tracking, and alert systems
- **analysis.py** - Data analytics with Pandas and Matplotlib visualizations

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

Project Link: [https://github.com/yourusername/expense-tracker](https://github.com/yourusername/expense-tracker)
