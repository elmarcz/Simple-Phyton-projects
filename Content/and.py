#With the and operator both numbers must match for the action to be carried out.
num_one = int(input("Enter the first number: "))
num_two = int(input("Enter the second number: "))
num_three = int(input("Enter the third number: "))
num_four = int(input("Enter the fourth number: "))

if num_one == num_two and num_three == num_four:
    print("The numbers are correct")
else:
    print("The numbers aren't correct")
