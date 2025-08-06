# print("Welcome to Zomato!\n")
 
   


# # Step 1: Food items and prices
# foods = ["Pizza", "Burger", "Pasta", "Biryani", "Chowmein"]
# prices = [250, 120, 180, 220, 100]

# # Step 2: Show food list
# print("Available Food Items:")
# for i in range(len(foods)):
#     print(f"{i+1}. {foods[i]} - Rs.{prices[i]}")
# print()

# # Step 3: User choice
# choice = int(input("Enter the number of the food item you want to order (1-5): "))

# # Step 4: Using if-elif like before (one for each item)
# if choice == 1:
#     food = foods[0]
#     price = prices[0]
#     qty = int(input("Enter quantity: "))
#     if qty > 0:
#         gst = 18 * qty
#         total = price * qty
#         final = total + gst
#         print(f"\nFood: {food}")
#         print(f"Quantity: {qty}")
#         print(f"Total: Rs.{total}")
#         print(f"GST (₹18 per item): Rs.{gst}")
#         print(f"Final Bill: Rs.{final}")
#         print("Thank you for ordering from Zomato!")
#     else:
#         print("Invalid quantity.")

# elif choice == 2:
#     food = foods[1]
#     price = prices[1]
#     qty = int(input("Enter quantity: "))
#     if qty > 0:
#         gst = 18 * qty
#         total = price * qty
#         final = total + gst
#         print(f"\nFood: {food}")
#         print(f"Quantity: {qty}")
#         print(f"Total: Rs.{total}")
#         print(f"GST (₹18 per item): Rs.{gst}")
#         print(f"Final Bill: Rs.{final}")
#         print("Thank you for ordering from Zomato!")
#     else:
#         print("Invalid quantity.")

# elif choice == 3:
#     food = foods[2]
#     price = prices[2]
#     qty = int(input("Enter quantity: "))
#     if qty > 0:
#         gst = 18 * qty
#         total = price * qty
#         final = total + gst
#         print(f"\nFood: {food}")
#         print(f"Quantity: {qty}")
#         print(f"Total: Rs.{total}")
#         print(f"GST (₹18 per item): Rs.{gst}")
#         print(f"Final Bill: Rs.{final}")
#         print("Thank you for ordering from Zomato!")
#     else:
#         print("Invalid quantity.")

# elif choice == 4:
#     food = foods[3]
#     price = prices[3]
#     qty = int(input("Enter quantity: "))
#     if qty > 0:
#         gst = 18 * qty
#         total = price * qty
#         final = total + gst
#         print(f"\nFood: {food}")
#         print(f"Quantity: {qty}")
#         print(f"Total: Rs.{total}")
#         print(f"GST (₹18 per item): Rs.{gst}")
#         print(f"Final Bill: Rs.{final}")
#         print("Thank you for ordering from Zomato!")
#     else:
#         print("Invalid quantity.")

# elif choice == 5:
#     food = foods[4]
#     price = prices[4]
#     qty = int(input("Enter quantity: "))
#     if qty > 0:
#         gst = 18 * qty
#         total = price * qty
#         final = total + gst
            
#      name=input("Please enter your name Sir")
#       number=int(input("Enter your number "))
#       address=input("Enter your location")






#         print(f"\nFood: {food}")
#         print(f"Quantity: {qty}")
#         print(f"Total: Rs.{total}")
#         print(f"GST (₹18 per item): Rs.{gst}")
#         print(f"Final Bill: Rs.{final}")
#         print("Thank you for ordering from Zomato!")
#     else:
#         print("Invalid quantity.")

# else:
#     print("Invalid food selection.")


print("Welcome to Zomato!\n")

# Step 1: Take user details
name = input("Please enter your name: ")
number = input("Enter your mobile number: ")
address = input("Enter your location/address: ")

# Step 2: Food items and prices
foods = ["Pizza", "Burger", "Pasta", "Biryani", "Chowmein"]
prices = [250, 120, 180, 220, 100]

# Step 3: Show food list
print("\nAvailable Food Items:")
for i in range(len(foods)):
    print(f"{i+1}. {foods[i]} - Rs.{prices[i]}")
print()

# Step 4: User choice
choice = int(input("Enter the number of the food item you want to order (1-5): "))

# Step 5: if-elif for each item
if choice == 1:
    food = foods[0]
    price = prices[0]
    qty = int(input("Enter quantity: "))
    if qty > 0:
        gst = 18 * qty
        total = price * qty
        final = total + gst
        print(f"\nFood: {food}")
        print(f"Quantity: {qty}")
        print(f"Total: Rs.{total}")
        print(f"GST (₹18 per item): Rs.{gst}")
        print(f"Final Bill: Rs.{final}")
        print(f"Name: {name}")
        print(f"Mobile No.: {number}")
        print(f"Address: {address}")
        print("Thank you for ordering from Zomato!")
    else:
        print("Invalid quantity.")

elif choice == 2:
    food = foods[1]
    price = prices[1]
    qty = int(input("Enter quantity: "))
    if qty > 0:
        gst = 18 * qty
        total = price * qty
        final = total + gst
        print(f"\nFood: {food}")
        print(f"Quantity: {qty}")
        print(f"Total: Rs.{total}")
        print(f"GST (₹18 per item): Rs.{gst}")
        print(f"Final Bill: Rs.{final}")
        print(f"Name: {name}")
        print(f"Mobile No.: {number}")
        print(f"Address: {address}")
        print("Thank you for ordering from Zomato!")
    else:
        print("Invalid quantity.")

elif choice == 3:
    food = foods[2]
    price = prices[2]
    qty = int(input("Enter quantity: "))
    if qty > 0:
        gst = 18 * qty
        total = price * qty
        final = total + gst
        print(f"\nFood: {food}")
        print(f"Quantity: {qty}")
        print(f"Total: Rs.{total}")
        print(f"GST (₹18 per item): Rs.{gst}")
        print(f"Final Bill: Rs.{final}")
        print(f"Name: {name}")
        print(f"Mobile No.: {number}")
        print(f"Address: {address}")
        print("Thank you for ordering from Zomato!")
    else:
        print("Invalid quantity.")

elif choice == 4:
    food = foods[3]
    price = prices[3]
    qty = int(input("Enter quantity: "))
    if qty > 0:
        gst = 18 * qty
        total = price * qty
        final = total + gst
        print(f"\nFood: {food}")
        print(f"Quantity: {qty}")
        print(f"Total: Rs.{total}")
        print(f"GST (₹18 per item): Rs.{gst}")
        print(f"Final Bill: Rs.{final}")
        print(f"Name: {name}")
        print(f"Mobile No.: {number}")
        print(f"Address: {address}")
        print("Thank you for ordering from Zomato!")
    else:
        print("Invalid quantity.")

elif choice == 5:
    food = foods[4]
    price = prices[4]
    qty = int(input("Enter quantity: "))
    if qty > 0:
        gst = 18 * qty
        total = price * qty
        final = total + gst
        print(f"\nFood: {food}")
        print(f"Quantity: {qty}")
        print(f"Total: Rs.{total}")
        print(f"GST (₹18 per item): Rs.{gst}")
        print(f"Final Bill: Rs.{final}")
        print(f"Name: {name}")
        print(f"Mobile No.: {number}")
        print(f"Address: {address}")
        print("Thank you for ordering from Zomato!")
    else:
        print("Invalid quantity.")

else:
    print("Invalid food selection.")







