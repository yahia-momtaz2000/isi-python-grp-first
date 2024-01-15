# create tuple
my_tuple = (101, 'Yahia Momtaz', 7000.0, 'Cairo')
print(my_tuple)
print(type(my_tuple))
# access index no 2 : salary
print(my_tuple[2])
job_tuple = ('Python developer', 'Senior')
my_tuple = my_tuple + job_tuple # concat
print(my_tuple)
## my_tuple[2] = 9000  :: Error
# Loop over the tuple : for i loop | for each loop
# for i loop
for i in range(len(my_tuple)):
    print(my_tuple[i])

print('------------- for each ------')
for item in my_tuple:
    print(item)

