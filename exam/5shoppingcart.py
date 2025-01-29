def add_items(dictionary):
    item = input("Enter the item name: ")
    value = int(input("Enter the price of the item: "))
    dictionary[item] = value
#check cart
def viewcart(dictionary):
    if not dictionary:
        print("Cart is empty")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
#calculate price
def calculate_price(dictionary):
    total_price = sum(dictionary.values())
    print(f"Total price: {total_price}")
def main():
    dictionary={}
    while True:
        print("1.ADD ITEM\t2.VIEW CART\n3.CALCULATE TOTAL PRICE\t4.EXIT")
        n=int(input("enter a option"))
        if n==1:
            add_items(dictionary)
        elif n==2:
            viewcart(dictionary)
        elif n==3:
            total_amount=calculate_price(dictionary)
            print(f"total amount of cart= {total_amount}")
        elif n==4:
            break
main()