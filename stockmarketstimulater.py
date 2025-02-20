def get_stock_purchase(username, credentials):
    """Gets stock purchase information from the user and stores it."""

    if username not in [user[0] for user in credentials]:  # Verify username exists
        print("Invalid username.")
        return None  # Indicate failure

    try:
        ticker = input("Enter stock ticker symbol (e.g., AAPL, MSFT): ").upper()  # Uppercase for consistency
        if not ticker.isalpha(): #Basic Validation
            raise ValueError("Ticker must be alphabetic.")
        quantity = int(input("Enter quantity to buy: "))
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Store the purchase data (in a real application, you'd likely 
        # use a database or more structured data storage).  Here, I'm
        # using a dictionary.
        purchase_data = {
            "ticker": ticker,
            "quantity": quantity,
        }

        # In a real app, you wouldn't just print it.  You'd store it.
        print(f"{username} purchased {quantity} shares of {ticker}.")
        return {username: purchase_data} # Returning a dictionary for this user's purchase


    except ValueError as e:
        print(f"Invalid input: {e}")
        return None  # Indicate failure
    except Exception as e:  # Catch other potential errors
        print(f"An error occurred: {e}")
        return None


def main():
    credentials = [("alice", "password"), ("bob", "secret")]  # Example credentials

    username = input("Enter your username: ")
    purchase_info = get_stock_purchase(username, credentials)

    if purchase_info:
       # In a real application, you would now store purchase_info in a database, file, etc.
       print("Purchase information to be stored:", purchase_info) # Just printing for now.

if __name__ == "__main__":
    main()
