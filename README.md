# 💰 Smart Expense Tracker

A modern desktop-based expense management system developed using **Python, Tkinter (CustomTkinter), and SQLite**.

The application helps users manage daily expenses, categorize spending, and analyze financial habits through a clean and interactive graphical user interface.

---

## 📌 Project Overview

Smart Expense Tracker is a GUI-based desktop application that allows users to:

- Add and manage expenses
- Categorize spending
- Store records in SQLite database
- Generate financial reports
- Visualize spending patterns

This project is designed to simplify personal expense management through an easy-to-use desktop interface.

---

## ✨ Features

### 💸 Expense Management
- Add new expenses
- Categorize expenses (Food, Travel, Bills, Shopping, etc.)
- Save data securely using SQLite

### 📊 Reports & Analytics
- Monthly expense tracking
- Expense summary
- Spending analysis using charts

### 🎨 GUI Features
- Modern UI using CustomTkinter
- Clean dashboard interface
- Responsive buttons and forms

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Tkinter | GUI Development |
| CustomTkinter | Modern UI Design |
| SQLite | Database |
| Matplotlib | Charts & Graphs |
| Pandas | Data Analysis |

---

## 📂 Project Structure

```txt
SmartExpenseTracker/
│── main.py
│── database.py
│── login.py
│── dashboard.py
│── add_expense.py
│── reports.py
│
│── assets/
│   ├── icon.png
│   ├── bg.png
│
│── database/
│   └── expense.db

```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SmartExpenseTracker.git
```

### 2. Navigate to Project Folder

```bash
cd SmartExpenseTracker
```

### 3. Install Required Libraries

```bash
pip install customtkinter matplotlib pandas pillow
```

### 4. Run the Project

```bash
python main.py
```

---

## 🗄️ Database Schema

### Table: `expenses`

| Column Name | Data Type |
|-------------|------------|
| id | INTEGER |
| title | TEXT |
| amount | REAL |
| category | TEXT |
| date | TEXT |

--

---

## 🚀 Future Enhancements

- Dark/Light mode
- Expense prediction
- Budget alerts
- Export reports to PDF/CSV
- Multi-user login system

---

## 👨‍💻 Author

Om Tarade  
Computer Engineering Student


This project is created for educational and learning purposes.
