# scan products , apply discounts,generate bills,and record transactions

class BillingSystem:
     def __init__(self):
        self.products = {}          # Store products
        self.cart = {}              # Store scanned items
        self.transactions = []   # Store transaction history
     def add_product(self, name, price):
        self.products[name] = price

     def scan_product(self, name, quantity):
        if name in self.products:
            if name in self.cart:
                self.cart[name] += quantity
            else:
                self.cart[name] = quantity
        else:
            print("Product not found!")

     def generate_bill(self):
        total = 0
        print("\n----- BILL -----")
        for item, qty in self.cart.items():
            price = self.products[item]
            subtotal = price * qty
            total += subtotal
            print(item, "x", qty, "=", subtotal)

        discount_amount = total * (self.discount / 100)
        final_amount = total - discount_amount
        print("Total:", total)
        print("Discount:", discount_amount)
        print("Final Amount:", final_amount)

        self.transactions.append(final_amount)
        self.cart.clear()
        def show_transactions(self):
         print("\nTransaction History:")
        for t in self.transactions:
            print("Bill Amount:", t)


# Creating object
shop = BillingSystem()

# Adding products
shop.add_product("Pen", 10)
shop.add_product("Notebook", 50)
shop.add_product("Bag", 500)

# Scanning products
shop.scan_product("Pen", 2)
shop.scan_product("Notebook", 1)

# Applying discount
shop.apply_discount(10)

# Generating bill
shop.generate_bill()

# Show transactions
shop.show_transactions() 
