# ---------------------------------------------------------
# Python Coffee Selling App
# Developed for BSIT 3rd Semester - Leads University
# Topic: OOP + Logic + Menu-driven program
# ---------------------------------------------------------

class CoffeeShop:
    def __init__(self):
        # Coffee menu using dictionary
        self.menu = {
            1: {"name": "Espresso", "price": 250},
            2: {"name": "Cappuccino", "price": 300},
            3: {"name": "Latte", "price": 280},
            4: {"name": "Mocha", "price": 320},
            5: {"name": "Americano", "price": 270},
        }
        self.order_list = []  # stores orders

    def display_menu(self):
        print("\n=== ☕ Welcome to Python Coffee Shop ☕ ===")
        print("----------- MENU -----------")
        for key, item in self.menu.items():
            print(f"{key}. {item['name']} - Rs. {item['price']}")
        print("-----------------------------")

    def take_order(self):
        while True:
            try:
                choice = int(input("Enter coffee number (1-5) or 0 to finish: "))
                if choice == 0:
                    break
                elif choice in self.menu:
                    qty = int(input("Enter quantity: "))
                    coffee = self.menu[choice]
                    total_price = coffee['price'] * qty
                    self.order_list.append({
                        "name": coffee['name'],
                        "qty": qty,
                        "total": total_price
                    })
                    print(f"✅ Added {qty}x {coffee['name']} = Rs.{total_price}")
                else:
                    print("❌ Invalid selection! Try again.")
            except ValueError:
                print("⚠️ Please enter valid numbers.")

    def generate_bill(self):
        print("\n======= 🧾 BILL SUMMARY =======")
        total = 0
        for order in self.order_list:
            print(f"{order['name']} x {order['qty']} = Rs.{order['total']}")
            total += order['total']

        print("------------------------------")
        print(f"💰 Grand Total: Rs.{total}")
        print("☕ Thank you for visiting Python Coffee Shop!")
        print("===============================")


# -------- Main Program Execution --------
if __name__ == "__main__":
    shop = CoffeeShop()
    shop.display_menu()
    shop.take_order()
    shop.generate_bill()
