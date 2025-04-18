# Creating an empty list
my_list = []
print(my_list)
# Appending elements
my_list.append(10)
print(my_list)

my_list.append(20)
print(my_list)

my_list.append(30)
print(my_list)

my_list.append(40)
print(my_list)

# Inserting 15 at the second position (index 1)
my_list.insert(1, 15)
print(my_list)

# Extending the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# Removing the last element
my_list.pop()
print(my_list)

# Sorting the list in ascending order
my_list.sort()
print(my_list)

# Finding the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# print the final state of the list
print("Final list:", my_list)
