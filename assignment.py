# To Create an empty list
my_list = []

# To Append the elements 10, 20, 30, 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# To Insert the value 15 at the second position
my_list.insert(1, 15)

# To Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# To Remove the last element from the list
my_list.pop()

# To Sort the list in ascending order
my_list.sort()

# To Find and print the index of the value 30 in the list
index_of_30 = my_list.index(30)
print(f"The index of the value 30 in my_list is: {index_of_30}")