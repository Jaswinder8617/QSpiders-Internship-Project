

# Welcome Message
print("Welcome to SINGH Cinemas")
print("Thanks for visiting us!\n")

# Movie names and prices stored separately
movie_names = [
    "Jawan", "Pathaan", "Animal", "Pushpa 2", "RRR",
    "KGF 2", "Drishyam 2", "Brahmastra", "Vikram", "The Kashmir Files"
]

movie_prices = [
    150, 180, 200, 250, 220,
    230, 170, 160, 190, 140
]

# Display Movies
print("Available Movies:")
print("1. Jawan - ₹150")
print("2. Pathaan - ₹180")
print("3. Animal - ₹200")
print("4. Pushpa 2 - ₹250")
print("5. RRR - ₹220")
print("6. KGF 2 - ₹230")
print("7. Drishyam 2 - ₹170")
print("8. Brahmastra - ₹160")
print("9. Vikram - ₹190")
print("10. The Kashmir Files - ₹140")

total = 0

# First movie booking
choice1 = int(input("\nEnter the number of the first movie you want to book: "))
if choice1 == 1:
    qty = int(input("How many tickets for Jawan? "))
    total += 150 * qty
elif choice1 == 2:
    qty = int(input("How many tickets for Pathaan? "))
    total += 180 * qty
elif choice1 == 3:
    qty = int(input("How many tickets for Animal? "))
    total += 200 * qty
elif choice1 == 4:
    qty = int(input("How many tickets for Pushpa 2? "))
    total += 250 * qty
elif choice1 == 5:
    qty = int(input("How many tickets for RRR? "))
    total += 220 * qty
elif choice1 == 6:
    qty = int(input("How many tickets for KGF 2? "))
    total += 230 * qty
elif choice1 == 7:
    qty = int(input("How many tickets for Drishyam 2? "))
    total += 170 * qty
elif choice1 == 8:
    qty = int(input("How many tickets for Brahmastra? "))
    total += 160 * qty
elif choice1 == 9:
    qty = int(input("How many tickets for Vikram? "))
    total += 190 * qty
elif choice1 == 10:
    qty = int(input("How many tickets for The Kashmir Files? "))
    total += 140 * qty
else:
    print("Invalid selection.")

# Optional second movie
more = input("Do you want to book another movie? (yes/no): ")
if more.lower() == "yes":
    choice2 = int(input("Enter the number of the second movie: "))
    if choice2 == 1:
        qty = int(input("How many tickets for Jawan? "))
        total += 150 * qty
    elif choice2 == 2:
        qty = int(input("How many tickets for Pathaan? "))
        total += 180 * qty
    elif choice2 == 3:
        qty = int(input("How many tickets for Animal? "))
        total += 200 * qty
    elif choice2 == 4:
        qty = int(input("How many tickets for Pushpa 2? "))
        total += 250 * qty
    elif choice2 == 5:
        qty = int(input("How many tickets for RRR? "))
        total += 220 * qty
    elif choice2 == 6:
        qty = int(input("How many tickets for KGF 2? "))
        total += 230 * qty
    elif choice2 == 7:
        qty = int(input("How many tickets for Drishyam 2? "))
        total += 170 * qty
    elif choice2 == 8:
        qty = int(input("How many tickets for Brahmastra? "))
        total += 160 * qty
    elif choice2 == 9:
        qty = int(input("How many tickets for Vikram? "))
        total += 190 * qty
    elif choice2 == 10:
        qty = int(input("How many tickets for The Kashmir Files? "))
        total += 140 * qty
    else:
        print("Invalid selection.")

# Collect customer details
name = input("\nEnter your name: ")

# Validate 10-digit mobile number starting with 9/8/7/6
while True:
    mobile = input("Enter your mobile number: ")
    if mobile.isdigit() and len(mobile) == 10 and mobile[0] in ['9', '8', '7', '6']:
        break
    else:
        print("Invalid mobile number. Please enter a valid 10-digit number starting with 9, 8, 7, or 6.")

# Final Calculation
gst = 18
final_total = total + gst

# Print Bill
print("\n----------- YOUR TICKET BILL -----------")
print(f"Name: {name}")
print(f"Mobile Number: {mobile}")
print(f"Total Amount (without GST): ₹{total}")
print(f"GST (Fixed): ₹{gst}")
print(f"Total Amount to Pay: ₹{final_total}")
print("----------------------------------------")
print("Enjoy your movie!\n")
print("Thank you for visiting SINGH Cinemas")
