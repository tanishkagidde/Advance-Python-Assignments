	'''
  7. Product Inventory System					
						
	Develop a Python application to manage product records.					
						
	Requirements					
	Create a Product class with:					
		Product ID				
		Product Name				
		Price				
	Categorize products as:					
		Expensive				
		Affordable				
	Create an Inventory class.					
	Display all products.		
  '''
class Product:
    EXPENSIVE_THRESHOLD = 500.0

    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_category(self) -> str:
        """Categorizes product based on its price."""
        return "Expensive" if self.price >= self.EXPENSIVE_THRESHOLD else "Affordable"

    def __str__(self) -> str:
        return f"ID: {self.product_id:<8} | Name: {self.name:<20} | Price: ₹{self.price:,.2f} | Category: {self.get_category()}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product_id: str, name: str, price: float):
        product = Product(product_id, name, price)
        self.products.append(product)
        print(f"Added product: {name}")

    def display_all_products(self):
        print("\n--- Product Inventory Records ---")
        if not self.products:
            print("No products currently in inventory.")
            return

        print("-" * 65)
        for product in self.products:
            print(product)
        print("-" * 65)


#Example Usage
if __name__ == "__main__":
    store_inventory = Inventory()

    # Adding product records
    store_inventory.add_product("P101", "Wireless Headphones", 1200.00)
    store_inventory.add_product("P102", "USB-C Cable", 250.00)
    store_inventory.add_product("P103", "Mechanical Keyboard", 3500.00)
    store_inventory.add_product("P104", "Mouse Pad", 150.00)

    # Displaying all products and their categories
    store_inventory.display_all_products()
  """
  OUTPUT :
  Added product: Wireless Headphones
Added product: USB-C Cable
Added product: Mechanical Keyboard
Added product: Mouse Pad

--- Product Inventory Records ---
-----------------------------------------------------------------
ID: P101     | Name: Wireless Headphones  | Price: ₹1,200.00 | Category: Expensive
ID: P102     | Name: USB-C Cable          | Price: ₹250.00 | Category: Affordable
ID: P103     | Name: Mechanical Keyboard  | Price: ₹3,500.00 | Category: Expensive
ID: P104     | Name: Mouse Pad            | Price: ₹150.00 | Category: Affordable
-----------------------------------------------------------------
  """
						
