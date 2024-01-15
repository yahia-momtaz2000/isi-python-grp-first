emp_name = 'Ahmed Omar'
print(emp_name)
#---------------
print(emp_name.upper())
print(emp_name.lower())
print(emp_name)
up_emp_name = emp_name.upper()
print(up_emp_name)
print('---------------')
print(up_emp_name.isupper())
print(up_emp_name.islower())
if up_emp_name.isupper():
    print('yes it is all upper')
else:
    print('no it is not upper')
print('--------------------')
mobile = '01123131271'
if mobile.startswith('011'):
    print('Etisalat no.')
else:
    print('Other phone')
print('--------------')
file_path = 'C:\my_files\learn_python.PdF'
if file_path.lower().endswith('pdf'):  # ignore case sensitive
    print('it is a book')
else:
    print('not a book')

print(mobile.isnumeric())
print('------------------')
student_information = 'He is Ahmed Ahmed lives in cairo'
# convert string to List : every word is list element : split function
words_list = student_information.split(' ')
print(words_list)

# convert from list to string and space inbetween
new_string = ' '.join(words_list)
print(new_string)










