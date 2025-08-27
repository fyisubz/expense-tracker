# Expense Tracker

We developed a comprehensive **Expense Tracker** application using Python with SQLite database, Tkinter GUI, and advanced data analytics for efficient personal finance management.

• On the **backend**, we created an expense tracking system with SQLite for CRUD operations, budget tracking, and financial analysis.

• We integrated sample data and implemented core functionalities: adding, updating, deleting, and viewing expenses with budget management and analysis reports.

• On the **frontend**, we built a **Tkinter GUI** with interactive charts using **Pandas** for data manipulation and **Matplotlib/Seaborn** for beautiful visualizations.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Tkinter](https://img.shields.io/badge/tkinter-4B8BBE?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

## 📸 Application Screenshots

### Main Dashboard
![Main Dashboard](https://raw.githubusercontent.com/fyisubz/expense-tracker/main/images/main-dashboard.png)
*Clean interface with expense entry form, data table, and comprehensive budget management controls*

### Data Visualization
![Expense Analytics](https://raw.githubusercontent.com/fyisubz/expense-tracker/main/images/expense-analytics.png)
*Interactive bar chart showing detailed expenses by category breakdown (Food, Laptop, College)*

## 📁 Project Structure

```
ExpenseTracker/
├── images/                 # Application screenshots
│   ├── main-dashboard.png
│   └── expense-analytics.png
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

• Add, update, delete expense records with category organization
• Budget tracking with alerts and visual notifications  
• Advanced analytics using Pandas for data insights
• Beautiful Matplotlib and Seaborn charts: bar charts and category breakdowns
• Interactive Tkinter dashboard with real-time tracking
• Export capabilities (CSV, Excel formats)

## 🚀 Getting Started

### Prerequisites
- Python 3.7+ with tkinter

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

- **extrack.py** - Main Tkinter GUI interface
- **db.py** - SQLite database management  
- **models.py** - Data models with validation
- **budget.py** - Budget tracking and alerts
- **analysis.py** - Pandas/Matplotlib/Seaborn analytics and visualizations

## 🤝 Contributing

1. Fork the project
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file.

Project Link: [https://github.com/yourusername/expense-tracker](https://github.com/yourusername/expense-tracker)
