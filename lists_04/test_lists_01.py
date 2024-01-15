# create lists
numbers_list = [13, 20, 5, 6, 10, 15]
# print lists
print(numbers_list)
print(type(numbers_list))
# adding new element to the end of list : use function append
numbers_list.append(66)
print(numbers_list)
# adding new element at index 2nd : use function insert
numbers_list.insert(2, 77)
print(numbers_list)
# access element in the list : the 3rd element
print( numbers_list[3] )
# change the 3rd element in the list to 55
numbers_list[3] = 55
print(numbers_list)
# count of the element in the list : use general function: len
count_elements = len(numbers_list)
print(count_elements)
print('---------(1) loop over list using for i loop - index ---')
for i in range(0, len(numbers_list)):
    print(numbers_list[i])

print('---------(2) loop over list using for in (each) loop --')
for item in numbers_list:
    print(item)

print('---------- reverse -----------')
print(numbers_list)

numbers_list.reverse()
print(numbers_list)

print('--------- sort -----------')
numbers_list.sort() # asc
numbers_list.sort(reverse=True) # desc
print(numbers_list)

print('------sum, max, min ---')
print(sum(numbers_list))
print(max(numbers_list))
print(min(numbers_list))

