# create a sample list
my_list = [1, 2, 3, 4, 5]

# append method
my_list.append(6)
print(my_list)  # output: [1, 2, 3, 4, 5, 6]

# extend method
my_list.extend([7, 8, 9])
print(my_list)  # output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert method
my_list.insert(0, 0)
print(my_list)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# remove method
my_list.remove(0)
print(my_list)  # output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop method
my_list.pop()
print(my_list)  # output: [1, 2, 3, 4, 5, 6, 7, 8]

# index method
print(my_list.index(5))  # output: 4

# count method
print(my_list.count(5))  # output: 1

# sort method
my_list.sort()
print(my_list)  # output: [1, 2, 3, 4, 5, 6, 7, 8]

# reverse method
my_list.reverse()
print(my_list)  # output: [8, 7, 6, 5, 4, 3, 2, 1]

# copy method
new_list = my_list.copy()
print(new_list)  # output: [8, 7, 6, 5, 4, 3, 2, 1]

# clear method
new_list.clear()
print(new_list)  # output: []

# len method
print(len(my_list))  # output: 8

# min method
print(min(my_list))  # output: 1

# max method
print(max(my_list))  # output: 8

# sum method
print(sum(my_list))