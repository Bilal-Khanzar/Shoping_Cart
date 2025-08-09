#define product class 

class Product:
    def __init__(self, name , price):
        self.name = name 
        self.price = price 

        
#define shopingcard 

class ShopingCard:
    def __init__(self):
        self.items = []
    
    # add products to our card 
    def add_itemes(self,product):
        self.items.append(product)  # self.items  we added items here 

    #remove product from shop by name ,when we wwant to reomeve the items ,we should us name

    def Remove_items(self, name):
        self.items = [item for item in self.items if item.name != name]

    #displa all items 

    def view_card(self):
        if not self.items:  #self.items
            print(f"cart is empty {self.items}")  # self.items
        else:
            for id, item in enumerate(self.items,1):  # enumerate 
                print(f"{id}. {item.name} - ${item.price}")  #  item.name

    #calculate total price 

    def total(self):
        return sum(item.price for item in self.items )
    
    #main app 

def main():
        cart = ShopingCard()

        products = [

            Product("Shoes", 50),
            Product("T-shirt", 20),
            Product("Tie", 70),
            Product("Jense", 150),
            Product("Watch", 2000),
            Product("Cap", 44),
            Product("Coat", 600)
            
        ]
        while  True:
            print("\n=== Shoping menu ==== ")

            print("1. view products")

            print("2. add to cart ")

            print("3. remove from cart ")

            print("4.  view cart ")

            print("5. checkout ")

            print("6. Exit")  # "6"

            choice = input("Select option: " )

            if choice == "1":
                for i,p in enumerate(products,1):
                    print(f"{i} - {p.name} - {p.price}")

            elif choice == "2":

                p_id = int(input("enter product number : "))-1

                if 0 <= p_id < len(products):
                    cart.add_itemes(products[p_id])
                    print("Add to Cart ")

                else:
                 print("invalid products . ")  # invalid
            elif choice == "3":
                name = input("Enter product name to remove  : ")
                cart.Remove_items(name)

                print("Removed from cart ")

            elif choice == "4":
                cart.view_card()
            

            elif choice == "5":
                 cart.view_card()

                 print("total : $  ", cart.total())  # total price it will show us how much is total coust 

            elif choice == "6":
                print("thanks for shoping ")  #  thanks

                break
            else:

                print("invalid Choice . ")  # invalid 

            
main()
