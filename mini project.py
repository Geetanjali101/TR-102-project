# MINI PROJECT
import pprint
print("~~~~~~~~~~~~~~~~~~~The Table By Basant~~~~~~~~~~~~~~~~~~~~~")
print("Reviews: 4.1 ")
print("Reviewed by : 113.8k  Customers")
print("Specialisation: North Indian , Italian , South Indian")
print("\nPromo codes: GOBIG, CRAVINGS, ZOMATO")
print("\n\n\n")

print("~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~")
products = {
            "Margherita": 380,
            "Exotic Veggies": 485,
            "Panner Tikka Pizza" : 515,
            
            "Alfredo Pasta": 260,
            "Mix Sauce Pasta": 210,

            "Dal Makhani": 120,
            "Palak Paneer": 130,
            "Shahi Paneer": 230,
            "Chana Masala": 110,
            "Paneer Butter Masala": 250,
            "Cheese Tomato": 130,
            "Mixed Vegtables": 90,
            "Veg Pulao": 120,
            "Idli": 50,
            "Vada": 70,
            "Masala Dosa": 110,
            "Coconut Chutney": 30,
            "The Table Special Thali (Dal Makhani + Shahi Paneer + Ratia + 3Butter Roti": 230,

            "Chocolate Shake": 100,
            "Oreo Shake": 150,
            "Carmel fudge Shake": 190,
            "Browine Shake": 140,
            "Kitkat Shake": 170,

            "Ice Cream": 80,
            "Sundae": 250,
            "Gulab Jamun ": 25,
            "Rasgulla": 20
            }

land = pprint.pformat(products)
print("\n", land)

print("~~~~~~~~~~~~~~~~~~~~LETS START BUILDING YOUR CART~~~~~~~~~~~~~~~~~~~~~~~~")
cart = []
choice = "yes"

while choice == "yes":
    product = input("Enter Product of Your Choice:")
    cart.append(products[product])
    choice = input("Would you like to add another product in your cart (yes/no):")

print("Your Cart has ", len(cart), " item:")
print(cart)

total = 0

for i in cart:
    total = int(total) + int(i)

if total >= 100:
    promo_code = input("Enter Promo Code:")
    if promo_code == "GOBIG":
        discount = total * 0.4

        if discount >= 100:
            discount = 100

        taxes = 0.1 * total

        amount = total - discount + taxes
        print("Required amount to be paid is:", amount, "\n please proceed for checkout!!")

    elif promo_code == "CRAVINGS":
        discount = total * 0.5

        if discount >= 100:
            discount = 100

        taxes2 = 0.1 * total

        amount = total - discount + taxes2
        print("Required amount to be paid is:", amount)

    else:
        print("This code does not exists or no code has been applied")
        taxes2 = 0.1 * total
        amount = total + taxes2

else:
    print("Your total amount is lower than 100 please add more items to be eligible for the application of the promo code!")
    print("Required amount to be paid is:", total)

if len(cart) > 2 and total >= 100:
    print(
        "Congratulations! you bought more than two items and your order is eligible for a complimentary gift of a coca cola 150 ml bottle worth RS. 20")

print("Please proceed for checkout\n ORDER CONFIRMED! \n THANKS FOR ORDERING")
