name = input("Enter your full name: ")
phone_number = input("enter your number: ")

#result = len(name)
#result = name.find("s") # searches from left side
#result = name.rfind("k") # searches from right side
#result = name.capitalize() # capitalizes the first character of the string
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha() # if it has spaces then also it will become false
#result = phone_number.count("-") # counts the dash between the number
result = phone_number.replace("-"," ")

print(result)