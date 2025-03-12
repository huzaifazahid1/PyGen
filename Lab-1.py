y = 2
# The initial value of y is 2
if y > 0:
    print("These are two comments")  # print a string

print("Statement 1")
print("Statement 2")
# You can write two statements in the following way

print("Statement 1"); print("Statement 2")

# Incorrect indentation (will cause an error)
# y = 2
# if y > 0:
# print("The statement has no indentation ")
# print("The statement has no indentation ")

# Single space indentation
y = 2
if y > 0:
 print("The statement has a single space indentation")
 print("The statement has a single space indentation")

# Tab indentation
y = 2
if y > 0:
	print("The statement has a single tab indentation")
	print("The statement has a single tab indentation")

# Space + tab indentation
y = 2
if y > 0:
	 print("The statement has a single space + tab indentation")
	 print("The statement has a single space + tab indentation")


#data types 

p = 15
print(type(p))

q = -15
print(type(q))

r = 0
print(type(r))

s = 2.05
print(type(s))

t = 11.11
print(type(t))

u = 3.14e-5
print(type(u))

v = 6E100
print(type(v))

# Complex numbers
comp1 = complex(2, 3)
print(type(comp1))
print(2+3j)

comp2 = 2+3j
print(type(comp2))

comp3 = 2+3J
print(type(comp3))

# Boolean values
flag1 = True
print(type(flag1))

flag2 = False
print(type(flag2))


#strings

strA = "Python"  # Double quotes
print(strA)

strB = 'Programming'  # Single quotes
print(strB)

# Incorrect string usage (will cause an error)
# strC = "String'  
# print(strC)

# strD = 'String"  
# print(strD)

strE = "Day's"  # Single quote within double quotes
print(strE)

strF = 'Day"s'  # Double quote within single quotes
print(strF)

# Escape sequences
print("This is a backslash (\\) symbol.")
print("This is tab \t key")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line\nNew line")

#string indexing


text = "PYTHON COURSE"
print(text[0])   # First character
print(text[-14]) # First character
print(text[13])  # Last character
print(text[-1])  # Last character
print(text[5])   # 5th character
print(text[-9])  # 5th character
# print(text[15]) # Out of index range - would cause error

#Lists in python 

num_list = [7, 22, 33, 44]  # List of integers
print(num_list)

color_list = ['yellow', 'blue', 'black', 'white']  # List of strings
print(color_list)

mixed_list = ['green', 25, 99.99]  # List with different data types
print(mixed_list)

empty_list = []
print(empty_list)

color_options = ["RED", "Blue", "Green", "Black"]  # List with four elements
print(color_options[0])  # First element
print(color_options[0], color_options[3])  # First and last elements
print(color_options[-1])  # Last element
# print(color_options[4])  # Would cause an error - index out of range

#list slicing


color_samples = ["RED", "Blue", "Green", "Black"]

print(color_samples[0:2])  # Cut first two items
print(color_samples[1:2])  # Cut second item
print(color_samples[1:-2]) # Cut second item
print(color_samples[:3])   # Cut first three items
print(color_samples[:])    # Copy of the original list


