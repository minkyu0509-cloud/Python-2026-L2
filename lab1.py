import math
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle with radius {radius} is: {area:.2f}")

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

def check_prime():
    num = int(input("Enter a number to check if it's prime: "))
    if num <= 1:
        print(f"{num} is not a prime number.")
        return
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return
    print(f"{num} is a prime number.")

def check_perfect_number():
    num = int(input("Enter a number to check if it's a perfect number: "))
    if num < 1:
        print(f"{num} is not a perfect number.")
        return
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

def find_favorite_color():
    my_colors = ["blue", "green","yellow", "red", "white"]
    user_color = input("Enter your favorite color: ").lower()
    try:
        color_index = my_colors.index(user_color)
        print(f"{user_color.capitalize()} is one of my favorite colors!")  
    except ValueError:
        print(f"{user_color.capitalize()} is not one of my favorite colors.")

def create_sequences():
    range1 = range(7)
    range2 = range(1,11,3)
    range3 = range(5,0,-1)
    range4 = range(6,-3,-2)
    print("Range 1:", list(range1))
    print("Range 2:", list(range2))
    print("Range 3:", list(range3))
    print("Range 4:", list(range4))

def remove_dollar_sign(s):
    newstring = s.replace("$", "")
    return newstring


def extract_even(l):
    even_numbers = [num for num in l if num % 2 == 0]
    return even_numbers
sample_list = [1, 4, 5, -1, 10]
result = extract_even(sample_list)

print("Given list:", sample_list)
print("Even items:", result)

def calculate_factorial():
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        return None
    if n in (0,1):
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        return factorial

def get_all_divisors():
    num = int(input("Enter a number to find its divisors: "))
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    print(f"The divisors of {num} are: {divisors}")

def calculate_distance():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"The distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")

def print_pattern():
    n = int(input("Enter the number of rows for the pattern: "))
    m = int(input("Enter the number of columns for the pattern: "))
    if m<=0 or n<=0:
        print("Number of rows and columns must be positive integers.")
        return  
    for i in range(m):
        print("* " * n)

print ("ex 1: Calculate Circle Area")
calculate_circle_area()
print("\nex 2: Celsius to Fahrenheit")
celsius_to_fahrenheit()
print("\nex 3: Check Prime Number")
check_prime()
print("\nex 4: Check Perfect Number")
check_perfect_number()
print("\nex 5: Find Favorite Color")
find_favorite_color()
print("\nex 6: Create Sequences")
create_sequences()
print("\nex 7: Remove Dollar Sign")
test_string = input("Enter a string to remove dollar signs: ")
cleaned_string = remove_dollar_sign(test_string)
print("Cleaned string:", cleaned_string)
print("\nex 8: Extract Even Numbers")
extract_even(sample_list)
print("\nex 9: Calculate Factorial")
calculate_factorial()
print("\nex 10: Get All Divisors")
get_all_divisors()
print("\nex 11: Calculate Distance")
calculate_distance()
print("\nex 12: Print Pattern")
print_pattern()