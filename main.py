
# Arithmetic Operations
print("Arithmetic Operations:")
a = 10
b = 5
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

# Comparison Operations
print("\nComparison Operations:")
x = 10
y = 20
print("x == y is", x == y)  # Equal to
print("x != y is", x != y)  # Not equal to
print("x > y is", x > y)    # Greater than
print("x < y is", x < y)    # Less than
print("x >= y is", x >= y)  # Greater than or equal to
print("x <= y is", x <= y)  # Less than or equal to

# Logical Operations
print("\nLogical Operations:")
p = True
q = False
print("p and q is", p and q)  # Logical AND
print("p or q is", p or q)    # Logical OR
print("not p is", not p)       # Logical NOT

# String Operations
print("\nString Operations:")
s1 = "Hello"
s2 = "World"
print("Concatenation:", s1 + " " + s2)  # String Concatenation
print("Length of s1:", len(s1))           # String Length
print("Substring:", s1[1:4])              # Substring

# List Operations
print("\nList Operations:")
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
my_list.append(6)       # Append an element
print("After Append:", my_list)
my_list.remove(3)       # Remove an element
print("After Remove:", my_list)
my_list.reverse()       # Reverse the list
print("After Reverse:", my_list)

# Dictionary Operations
print("\nDictionary Operations:")
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Original Dictionary:", my_dict)
my_dict['age'] = 31     # Update an entry
print("After Update:", my_dict)
my_dict.pop('city')     # Remove an entry
print("After Pop:", my_dict)
