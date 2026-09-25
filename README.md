# CodeAlpha Stock Portfolio Tracker

A simple Python-based **Stock Portfolio Tracker** that allows users to enter stock symbols and quantities, calculate their total investment value, and save the portfolio report in CSV or TXT format.

## 🚀 Features

- Display available stocks and their predefined prices
- Add multiple stocks to the portfolio
- Enter the quantity of each stock
- Automatically calculate the investment value
- Calculate the total portfolio investment
- Validate stock symbols and quantities
- Handle invalid user input
- Export the portfolio report as CSV or TXT

## 🛠️ Technologies Used

- Python
- CSV file handling
- Exception handling
- Functions
- Dictionaries
- Loops
- Conditional statements

## 📂 Project Structure

```text
CodeAlpha_StockPortfolioTracker/
├── stock_portfolio.py
├── portfolio_report.csv
├── portfolio_report.txt
└── README.md
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/gorlabhargavi2006-coder/CodeAlpha_StockPortfolioTracker.git
```

### 2. Open the project folder

```bash
cd CodeAlpha_StockPortfolioTracker
```

### 3. Run the Python program

```bash
python stock_portfolio.py
```

## 💻 How It Works

1. The program displays the available stocks.
2. Enter a stock symbol.
3. Enter the quantity of shares.
4. The program calculates the investment value:

```text
Investment Value = Stock Price × Quantity
```

5. Add multiple stocks as needed.
6. Enter `done` when finished.
7. The program calculates the total investment value.
8. Choose whether to save the portfolio report as a CSV or TXT file.

## 📌 Example

```text
=== Stock Portfolio Tracker ===
Available stocks: AAPL, TSLA, MSFT, GOOG
Enter stock symbols and quantities. Type 'done' when finished.

Enter stock symbol: MSFT
Enter quantity for MSFT: 5
Enter stock symbol: AAPL
Enter quantity for AAPL: 2
Enter stock symbol: done

Total investment value: $1960
Save report? (csv/txt/n): csv
Portfolio report saved to portfolio_report.csv
```

## 📄 Output

The portfolio report can be saved in:

- `portfolio_report.csv` — useful for Excel and data analysis
- `portfolio_report.txt` — a readable text summary
