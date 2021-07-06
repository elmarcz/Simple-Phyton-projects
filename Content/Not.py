#With the not operator, the condition must be false for the action to be carried out.
num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))

if not num_one > num_two:
    print("The numbers are correct")
else:
    print("The numbers aren't correct")
