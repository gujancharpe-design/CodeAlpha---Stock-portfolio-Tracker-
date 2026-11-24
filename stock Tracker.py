import csv


def stock_portfolio_tracker():
    # Hardcoded dictionary of stock prices (example values from task)
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 420,
        "AMZN": 185,
    }

    portfolio = []
    total_investment = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:", stock_prices)
    print("Type 'done' as the stock name when you finish adding stocks.\n")

    while True:
        stock_name = input("Enter stock name (or 'done' to finish): ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print(f"'{stock_name}' is not in the price list. Please choose from {list(stock_prices.keys())}.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        portfolio.append({
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "investment": investment,
        })
        print(f"Added {quantity} x {stock_name} @ ${price} = ${investment}\n")

    if not portfolio:
        print("\nNo stocks added. Exiting.")
        return

    print("\n=== Portfolio Summary ===")
    for item in portfolio:
        print(f"{item['stock']}: {item['quantity']} shares @ ${item['price']} = ${item['investment']}")
    print(f"\nTotal Investment Value: ${total_investment}")

    # Optional file saving (.txt or .csv)
    save_choice = input("\nDo you want to save the result? (txt / csv / no): ").strip().lower()

    if save_choice == "txt":
        filename = "portfolio_summary.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-" * 30 + "\n")
            for item in portfolio:
                f.write(
                    f"{item['stock']}: {item['quantity']} x ${item['price']} = ${item['investment']}\n"
                )
            f.write("-" * 30 + "\n")
            f.write(f"Total Investment Value: ${total_investment}\n")
        print(f"Saved summary to {filename}")

    elif save_choice == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Investment"])
            for item in portfolio:
                writer.writerow([item["stock"], item["quantity"], item["price"], item["investment"]])
            writer.writerow(["Total Investment", "", "", total_investment])
        print(f"Saved summary to {filename}")

    else:
        print("Result not saved.")


if __name__ == "__main__":
    stock_portfolio_tracker()