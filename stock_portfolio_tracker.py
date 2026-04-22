# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 2700,
    "MICROSOFT": 320
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")

# User input
n = int(input("Enter number of different stocks you want to buy: "))

for i in range(n):
    stock_name = input(f"Enter stock name {i+1}: ").upper()
    
    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("❌ Stock not available in price list")

# Calculation
print("\n📊 Your Portfolio:")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    
    print(f"{stock} -> {quantity} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment Value = ${total_investment}")

# Save to file (optional)
save = input("Do you want to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        file.write("------------------\n")
        
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock} -> {quantity} × {price} = {investment}\n")
        
        file.write(f"\nTotal Investment = {total_investment}")
    
    print("✅ Data saved to portfolio.txt")

print("🙏 Thank you!")