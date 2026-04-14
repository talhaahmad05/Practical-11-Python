def modify_list(lst):
      lst.append(4)

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)

def try_modify_string(s):
     s = "new value"
text ="original"
try_modify_string(text)
print(text)


def add_item(item, items=[]):
   items.append(item)
   return items


print(add_item(1))
print(add_item(2))


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
