import csv
import os
import tempfile
import unittest

from stock_portfolio import calculate_total_investment, save_portfolio_report


class StockPortfolioTests(unittest.TestCase):
    def test_calculate_total_investment(self):
        holdings = {"AAPL": 2, "TSLA": 1}
        self.assertEqual(calculate_total_investment(holdings), 610)

    def test_save_portfolio_report_creates_csv_file(self):
        holdings = {"AAPL": 2, "TSLA": 1}
        total = 610

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "portfolio_report.csv")
            save_portfolio_report(holdings, total, file_path)

            with open(file_path, newline="") as csv_file:
                reader = csv.reader(csv_file)
                rows = list(reader)

            self.assertEqual(rows[0], ["stock", "quantity", "price", "value"])
            self.assertIn(["AAPL", "2", "180", "360"], rows)
            self.assertIn(["TSLA", "1", "250", "250"], rows)
            self.assertEqual(rows[-1], ["total", "", "", "610"])

    def test_save_portfolio_report_creates_txt_file(self):
        holdings = {"AAPL": 2, "TSLA": 1}
        total = 610

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "portfolio_report.txt")
            save_portfolio_report(holdings, total, file_path)

            with open(file_path, "r", encoding="utf-8") as txt_file:
                content = txt_file.read()

            self.assertIn("AAPL", content)
            self.assertIn("TSLA", content)
            self.assertIn("Total: $610", content)


if __name__ == "__main__":
    unittest.main()
