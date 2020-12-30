# Normal usage :
# ================
# =================

list_of_name = ['raam', 'janaki', 'ravi']
new_list_of_name = list_of_name

list_of_name.append('raju')


print(list_of_name)
print(new_list_of_name)
print('\n')

new_list_of_name.append('aravind')
print(list_of_name)
print(new_list_of_name)
print('\n')
print("id for old list and new list")
print(id(list_of_name),'\n', id(new_list_of_name))
print('\n\n')
print("id for old list,new list 2nd element")
print(id(list_of_name[1]),'\n', id(new_list_of_name[1]))


#with copy
#==============

#Shallow copy

#================

#below code will give out put as copy will not affect the old_list

#[[1, 2, 3], [4, 5, 6], [6, 7, 8], [9, 10, 11]]
#[['a', 'b', 'c'], [4, 5, 6], [6, 7, 8], [9, 10, 11]]

import copy
old_list = [[1,2,3],[4,5,6],[6,7,8],[9,10,11]]
new_list = copy.copy(old_list)
new_list[0] = ['a','b','c']
print(old_list)
print(new_list)
print('\n')
print("id for old list and new list")
print(id(old_list),'\n', id(new_list))
print('\n\n')
print("id for old list,new list 2nd element")
print(id(old_list[0][2]),'\n', id(new_list[0][2]))

#below code will give out put as copy will affect the old_list

#[[1, 2, 'c'], [4, 5, 6], [6, 7, 8], [9, 10, 11]]
#[[1, 2, 'c'], [4, 5, 6], [6, 7, 8], [9, 10, 11]]

import copy
old_list1 = [[1,2,3],[4,5,6],[6,7,8],[9,10,11]]
new_list1 = copy.copy(old_list1)
new_list1[0][2] = 'c'
print(old_list1)
print(new_list1)
print("id for old list and new list")
print(id(old_list1),'\n', id(new_list1))
print('\n\n')
print("id for old list,new list 2nd element")
print(id(old_list1[0][2]),'\n', id(new_list1[0][2]))


#shallow copy creates a copy of the object but refernces each element of the object.

#deepcopy
#=============

#[[1, 2, 3], [4, 5, 6], [6, 7, 8], [9, 10, 11]]
#[[1, 2, 'c'], [4, 5, 6], [6, 7, 8], [9, 10, 11]]

old_list2 = [[1,2,3],[4,5,6],[6,7,8],[9,10,11]]
new_list2 = copy.deepcopy(old_list2)
new_list2[0][2] = 'c'
print(old_list2)
print(new_list2)

##shallow copy creates a copy of the object and the element of the object.