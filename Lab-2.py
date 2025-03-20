# Python Program Demonstrating Loops, Functions, and Classes

count = 0
while count < 3:
   count += 1
   print("Hello World")

print("List Iteration")
my_list = ["geeks", "for", "geeks"]
for item in my_list:
   print(item)

my_tuple = ("geeks", "for", "geeks")
for item in my_tuple:
   print(item)

print("String Iteration")
my_string = "GeeksforGeeks"
for char in my_string:
   print(char)

# Iterate over a list using index
my_list = ["geeks", "for", "geeks"]
for index in range(len(my_list)):
   print(index)

# Print all characters except 'e' and 's'
for letter in 'geeksforgeeks':
   if letter == 'e' or letter == 's':
      continue
   print("Current letter:", letter)

# Stop iteration when 'e' or 's' is encountered
for letter in 'geeksforgeeks':
   if letter == 'e' or letter == 's':
      break
   print("Current letter:", letter)

# Function without parameters
def greet():
   print("Hello World")

greet()

# Function with a parameter
def add_suffix(name):
   print(name + " refsens")

add_suffix("Hassan")
add_suffix("Huzaifa")
add_suffix("Fazail")

# Function with a default parameter
def country_info(country="France"):
   print("I am from", country)

country_info("Pakistan")
country_info("India")
country_info()

# Function iterating over a list
def print_food_items(food_list):
   for item in food_list:
      print(item)

food_list = ["apple", "banana", "orange"]
print_food_items(food_list)

# Function returning different data types based on condition
def check_flag(flag):
   if flag == 1:
      return 10
   return "Hello"

print(check_flag(2))

# Function with multiple parameters
def display_children(child3, child2, child1):
   print(child1, child2, child3)

display_children(1, 2, 3)
display_children(child1="a", child2="b", child3="c")
display_children(child3="a", child2="b", child1="c")
display_children('a', child2="b", child1="c")

# Class demonstrating constructor and attributes
class MyClass:
   num = 0
   text = 'dd'

   def __init__(self, value1, value2):
      self.text = value2

obj1 = MyClass(6, "Harry")
print(obj1.text)
