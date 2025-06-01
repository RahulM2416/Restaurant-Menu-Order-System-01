menu = {
    'Idly':30,
    'Vada':20,
    'Masala DOsa':50,
    'Mini Meals':45,
    'Full Meals':60,
    'Curd Rice':35,
    'Roti Curry':70,
    'Chapathi Palya':45,
    'Pulav':35,
    'Tomato Bath':35,
    'Poori & Curry':50,
}
print("---------------------------------")
print("Welcome to Python Restaurant ")
print("---------------------------------")
print("Idly:30\nVada:20\nMasala DOsa:50\nMini Meals:45\nFull Meals:60\nCurd Rice:35\nRoti Curry:70\nChapathi Palya:45\nPulav:35\nTomato Bath:35\nPoori & Curry:50")
print(" ")
order_total = 0

while True:
     item = input("Enter the food item you need to order : ")
     if item in menu:
        order_total+=menu[item]
        print(f"Your item {item} has been added to you order.")
        print(" ")
     else:
        print(f"Sorry , we dont have {item} in our menu.. ")
     another_order = input("Do you want to add another item ? (yes/no) :")
     print(" ")
     if another_order.lower()!='yes':
        break
print("------------------------------------------")
print(f"Total amount to be paid is {order_total}/- ")
print("-------------------------------------------")
