
item = input("What would you like to purchase?: ")
prize = float(input("What is the prize?: "))
quantity = int(input("how many would you like?: "))
total = quantity * prize

print(f"you have bought {quantity} {item}/s")
print(f"Your total is {total}")