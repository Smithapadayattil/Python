shopping_cart={}
total=0
while True:
    item=input("Add an item to your cart(e for exit): ")
    if item.lower() == "e":
        break
    else:
        price=(float(input("Enter the price of {item}: ")))
        shopping_cart[item] = price
        total += price
print("Your shopping cart")
for key,value in shopping_cart.items():
    print(f"{key}:{value}")
while True:
    item=input("Enter the item to remove(n for nothing): ")
    if item.lower()=="n":
        break
    elif item in shopping_cart:
        del shopping_cart[item]
    else:
        print("Item not available in shopping cart")
print(f"Total price:{total:.2f}")
