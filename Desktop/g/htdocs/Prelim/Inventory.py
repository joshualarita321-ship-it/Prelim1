def get_price_category(price):
    # Logic to determine if Budget, Mid-range, or Premium
    if price < 100:
        return "Budget"
    elif price < 500:
        return "Mid-range"
    else:
        return "Premium"


def check_stock_level(stock):
    # Logic to determine if stock is sufficient
    if stock >= 10:
        return "OK"
    else:
        return "LOW STOCK - Reorder needed"


def save_product(name, price, category, stock, stock_status):
    # File handling logic to record the data
    with open('inventory.txt', 'a') as file:
        file.write(f"Product: {name} | Price: P{price:.2f} | Category: {category} | Stock: {stock} | Status: {stock_status}\n")


while True:
    # 1. COLLECTION: Get data from user
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))

    # 2. PROCESSING: Call the functions
    category = get_price_category(price)
    stock_status = check_stock_level(stock)

    # 3. OUTPUT: Display results
    print("\n--- PRODUCT INFO ---")
    print(f"Name: {name}")
    print(f"Price: P{price:.2f}")
    print(f"Category: {category}")
    print(f"Stock: {stock}")
    print(f"Stock Status: {stock_status}")

    # Save to file
    save_product(name, price, category, stock, stock_status)
    print("Product saved to inventory.txt\n")

    # Ask user to continue
    choice = input("Add another product? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting program...")
        break