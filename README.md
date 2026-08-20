# Personal Finance Tracker

A simple desktop application written in Python for managing personal income and expenses.

The project was created to practice Python programming, working with JSON data, data analysis and data visualization with Matplotlib.

## Features

* Add income and expenses
* Categorize transactions
* Store transactions in a JSON file
* Display transaction history
* Calculate basic financial statistics
* Calculate average income and expenses
* Calculate total income, expenses and balance
* Visualize financial data using charts
* Simple menu-driven interface

## Technologies

* **Python 3**
* **JSON** – data storage
* **Matplotlib** – data visualization
* **Tkinter** – graphical interface for charts

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd personal-finance-tracker
```

3. Install the required dependencies:

```bash
pip install matplotlib
```

4. Run the application:

```bash
python main.py
```

## Project Structure

```text
personal-finance-tracker/
│
├── main.py
├── tranzakcje.json
├── README.md
└── requirements.txt
```

## Data Storage

Transactions are stored locally in a JSON file.

Example:

```json
{
    "id": 1,
    "type": "expense",
    "amount": 50.00,
    "category": "Food",
    "description": "Lunch"
}
```

## Future Improvements

Planned improvements for future versions:

* PostgreSQL database integration
* Improved graphical user interface
* More advanced financial statistics
* Monthly and yearly reports
* More data visualizations
* Transaction filtering and searching
* Exporting financial reports
* Improved project architecture
* Unit tests

## Purpose

This project is a learning project focused on improving my Python programming skills and understanding how to build a complete application from scratch.

It is also the first version of a project that I plan to gradually expand with more advanced technologies.

## Author

**Marcin Korzeniewski**

GitHub: makocchigod

---

**Version:** 1.0

