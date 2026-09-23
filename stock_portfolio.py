import csv

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 150,
}


def calculate_total_investment(holdings):
    """Calculate total value using current stock prices."""
    total = 0
    for stock, quantity in holdings.items():
        if stock not in STOCK_PRICES:
            raise ValueError(f"Price not available for {stock}.")
        total += STOCK_PRICES[stock] * quantity
    return total


def save_portfolio_report(holdings, total_value, file_path="portfolio_report.csv"):
    """Save the portfolio to CSV or TXT depending on the file extension."""
    if file_path.lower().endswith(".txt"):
        lines = ["Stock Portfolio Report", "======================"]
        for stock, quantity in holdings.items():
            price = STOCK_PRICES[stock]
            value = price * quantity
            lines.append(f"{stock}: {quantity} shares @ ${price} = ${value}")
        lines.append(f"Total: ${total_value}")
        with open(file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write("\n".join(lines) + "\n")
        return

    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["stock", "quantity", "price", "value"])

        for stock, quantity in holdings.items():
            price = STOCK_PRICES[stock]
            value = price * quantity
            writer.writerow([stock, quantity, price, value])

        writer.writerow(["total", "", "", total_value])


def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Enter stock symbols and quantities. Type 'done' when finished.\n")

    holdings = {}
    while True:
        stock = input("Enter stock symbol: ").strip().upper()
        if stock.lower() == "done":
            break

        if stock not in STOCK_PRICES:
            print(f"Sorry, {stock} is not in the available price list.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid whole number for quantity.")
            continue

        holdings[stock] = holdings.get(stock, 0) + quantity

    if not holdings:
        print("No stocks were entered. Nothing to calculate.")
        return

    total_value = calculate_total_investment(holdings)
    print(f"\nTotal investment value: ${total_value}")

    export_choice = input("Save report? (csv/txt/n): ").strip().lower()
    if export_choice == "csv":
        save_portfolio_report(holdings, total_value, "portfolio_report.csv")
        print("Portfolio report saved to portfolio_report.csv")
    elif export_choice == "txt":
        save_portfolio_report(holdings, total_value, "portfolio_report.txt")
        print("Portfolio report saved to portfolio_report.txt")
    else:
        print("Report not saved.")


if __name__ == "__main__":
    main()
