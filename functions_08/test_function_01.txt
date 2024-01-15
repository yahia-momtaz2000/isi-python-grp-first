# function : program to print number from 1 to 10
def print_numbers_func(max_no):
    sum = 0
    for i in range(1, max_no):
        sum = sum + i
        print(i, end=' ')
    print()
    return sum

# main program
# call function
result1 = print_numbers_func(11)
print(result1)
result = print_numbers_func(result1)
print(result)
result = print_numbers_func(26)
print(result)
