#The elif allows us to choose a route from among several routes, based on the value of a variable that acts as a selector.
num_one = int(input("Enter a number: "))

if num_one == 1:
    print("The numbers is 1")
elif num_one == 2:
    print("The numbers is 2")
elif num_one == 3:
    print("The numbers is 3")
else:
    print("The number is greater than three")
