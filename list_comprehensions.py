list = [1,2,3,4,5,6,7,8,9]

my_list = [n*n for n in list]
print(my_list)

even_list = [n for n in list if n%2==0]
print (even_list)

letter_num_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(letter_num_list)

names=['Bruce', 'Clark','Peter','Logan','Wade']
heroes=['Batman','Superman','Spiderman','Wolverine','Deadpool']
print(zip(names,heroes))

#dictionary comprehension
my_dict = {name:hero for name,hero in zip(names,heroes)}
print(my_dict)

#set comprehension
sets= [1,1,2,3,4,5,6,6,2,3,3,8,9,9,4,5,7]

my_set={n for n in sets}
print(my_set)