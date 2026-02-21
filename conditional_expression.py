# conditional expression = A one line shortcut  for the if else statement (ternary operator)
#                          print or assign one of two values based on condition
#                          X if condition else Y

num = 5
a = 10
b = 11

max_num = a if a > b else b

print("positive" if num > 0 else "negative")
print(max_num)