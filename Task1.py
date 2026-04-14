def greet(name):
    print(f"Hello, {name}!")
greet ("Talha")

def my_function():
 x = 10 # Local variable
 print(x)
my_function()

y = 20 # Global variable

def access_global():
 print(y) # Can access global variable

access_global() # Output: 20

def modify_global():
 global y
 y = 30 # Now modifying the global variable

modify_global()
print(y)


def modify_list(lst):
 lst.append(4) # Modifies the  list

numbers = [1, 2, 3]
modify_list(numbers)
# Output: [1, 2, 3, 4]

def try_modify_string(s):
 s = "new value" # Creates a new local string

text = "Original"
try_modify_string(text)
print(text)

def add_item(item, items=None):
 if items is None:
  items = []
 items.append(item)
 return items
print(add_item(1))
print(add_item(2))


def create_counter():
 count = 0
 def increment():
  nonlocal count
  count += 1
  return count
 return increment

counter = create_counter()
print(counter()) # 1
print(counter()) # 2

#Hello

