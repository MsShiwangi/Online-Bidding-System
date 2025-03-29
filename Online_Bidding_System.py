import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",   
    password="pass123", 
    database="bidding_system"
)
cursor = db.cursor()

# def login():
#     print("\nLogin")
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     cursor.execute("SELECT user_id, name, role FROM Users WHERE name = %s AND password = %s", (username, password))
#     result = cursor.fetchone()

#     if result:
#         user_id, name, role = result
#         print(f"Welcome {name} ({role})")
#         return user_id, role  # Return user_id and role
#     else:
#         print("Invalid username or password. Please try again.")
#         return None, None

# Function to add a user (Admin Only)
def add_user(name, password, role):
    cursor.execute("INSERT INTO Users (name, password, role) VALUES (%s, %s, %s)", (name, password, role))
    db.commit()
    print("User added successfully.")

# Function to delete a user (Admin Only)
def delete_user(user_id):
    cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
    db.commit()
    print("User deleted successfully.")

# Function for a seller to add an item for bidding
def add_item(seller_id, description, min_bid):
    cursor.execute("INSERT INTO Items (seller_id, description, min_bid) VALUES (%s, %s, %s)", (seller_id, description, min_bid))
    db.commit()
    print("Item added successfully.")

# Function to view items with open bids (For Buyers)
def view_open_items():
    cursor.execute("SELECT item_id, description, min_bid, max_bid FROM Items WHERE status = 'open'")
    items = cursor.fetchall()
    print("Open items for bidding:")
    for item in items:
        print(f"Item ID: {item[0]}, Description: {item[1]}, Minimum Bid: {item[2]}, Current Max Bid: {item[3]}")

# Function for a buyer to place a bid
def place_bid(item_id, buyer_id, bid_amount):
    cursor.execute("SELECT min_bid, max_bid FROM Items WHERE item_id = %s AND status = 'open'", (item_id,))
    result = cursor.fetchone()
    if result and bid_amount >=result[1] and bid_amount > result[0]:
        cursor.execute("INSERT INTO Bids (item_id, buyer_id, bid_amount) VALUES (%s, %s, %s)", (item_id, buyer_id, bid_amount))
        cursor.execute("UPDATE Items SET max_bid = %s WHERE item_id = %s", (bid_amount, item_id))
        db.commit()
        print("Bid placed successfully.")
    else:
        print("Bid amount is too low or item is closed.")

# Function for a seller to view bids on their item
def view_bids_on_item(seller_id, item_id):
    cursor.execute("SELECT B.buyer_id, B.bid_amount FROM Bids B INNER JOIN Items I ON B.item_id = I.item_id WHERE I.seller_id = %s AND I.item_id = %s", (seller_id, item_id))
    bids = cursor.fetchall()
    print("Bids placed on your item:")
    for bid in bids:
        print(f"Buyer ID: {bid[0]}, Bid Amount: {bid[1]}")

# Function for a seller to close bidding on an item
def close_bidding(item_id):
    cursor.execute("UPDATE Items SET status = 'closed' WHERE item_id = %s", (item_id,))
    db.commit()
    print("Bidding closed for item.")

# Function for a buyer to view won items
def view_won_items(buyer_id):
    cursor.execute("SELECT I.item_id, I.description, I.max_bid FROM Items I INNER JOIN Bids B ON I.item_id = B.item_id WHERE B.buyer_id = %s AND I.status = 'closed' AND B.bid_amount = I.max_bid", (buyer_id,))
    won_items = cursor.fetchall()
    print("Items you've won:")
    for item in won_items:
        print(f"Item ID: {item[0]}, Description: {item[1]}, Winning Bid: {item[2]}")

# Main menu for interaction
def main():
    # user_id, role = login()
    # if user_id is None:
    #     return 
    while True:
        print("\n1. Add User (Admin)")
        print("2. Delete User (Admin)")
        print("3. Add Item for Bidding (Seller)")
        print("4. View Open Items for Bidding (Buyer)")
        print("5. Place Bid (Buyer)")
        print("6. View Bids on Your Item (Seller)")
        print("7. Close Bidding on Item (Seller)")
        print("8. View Won Items (Buyer)")
        print("9. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            password = input("Enter password: ")
            role = input("Enter role (admin, buyer, seller): ")
            add_user(name, password, role)
        elif choice == '2':
            user_id = int(input("Enter User ID to delete: "))
            delete_user(user_id)
        elif choice == '3':
            seller_id = int(input("Enter Seller ID: "))
            description = input("Enter item description: ")
            min_bid = float(input("Enter minimum bid: "))
            add_item(seller_id, description, min_bid)
        elif choice == '4':
            view_open_items()
        elif choice == '5':
            item_id = int(input("Enter Item ID: "))
            buyer_id = int(input("Enter Buyer ID: "))
            bid_amount = float(input("Enter your bid amount: "))
            place_bid(item_id, buyer_id, bid_amount)
        elif choice == '6':
            seller_id = int(input("Enter Seller ID: "))
            item_id = int(input("Enter Item ID to view bids: "))
            view_bids_on_item(seller_id, item_id)
        elif choice == '7':
            item_id = int(input("Enter Item ID to close bidding: "))
            close_bidding(item_id)
        elif choice == '8':
            buyer_id = int(input("Enter Buyer ID: "))
            view_won_items(buyer_id)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
