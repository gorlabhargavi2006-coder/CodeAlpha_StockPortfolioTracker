# CodeAlpha_StockPortfolioTracker

A simple Python-based **Stock Portfolio Tracker** that allows users to enter stock symbols and quantities, calculate their total investment value, and save the portfolio report in CSV or TXT format.

## 🚀 Features

* Display available stocks and their predefined prices
* Add multiple stocks to the portfolio
* Enter the quantity of each stock
* Automatically calculate the investment value
* Calculate the total portfolio investment
* Validate stock symbols and quantities
* Handle invalid user input
* Export the portfolio report as:

  * CSV
  * TXT

## 🛠️ Technologies Used

* Python
* CSV File Handling
* Exception Handling
* Functions
* Dictionaries
* Loops
* Conditional Statements

## 📂 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio.py
├── portfolio_report.csv
├── portfolio_report.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Open the project folder

```bash
cd Stock-Portfolio-Tracker
```

### 3. Run the Python program

```bash
python stock_portfolio.py
```

## 💻 How It Works

1. The program displays the available stocks.
2. The user enters a stock symbol.
3. The user enters the quantity of shares.
4. The program calculates:

```text
Investment Value = Stock Price × Quantity
```

5. The user can add multiple stocks.
6. After entering `done`, the program calculates the total investment.
7. The user can save the portfolio report as a CSV or TXT file.

## 📌 Example

```text
=== Stock Portfolio Tracker ===

Available stocks:
AAPL, TSLA, MSFT, GOOG

Enter stock symbol: MSFT
Enter quantity for MSFT: 5

Enter stock symbol: AAPL
Enter quantity for AAPL: 2

Enter stock symbol: done

Total investment value: $2000
```

## 📄 Output

The portfolio report can be saved in:

* `portfolio_report.csv` — useful for Excel and data analysis
