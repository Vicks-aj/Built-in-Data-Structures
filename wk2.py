#create an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at the second position
my_list.insert(1,15)

#extend with another list: [50,60,70]
my_list.extend([50,60,70])

#remove the last element in my_list
del my_list[-1]

#sort my_list in an ascending order
my_list.sort()

#find and print the index of value 30
print(my_list.index(30))




