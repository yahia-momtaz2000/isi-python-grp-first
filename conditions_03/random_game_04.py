import random
# for i loop
count_correct = 0
count_wrong = 0
for i in range(1, 6):
    print('Question no : '+str(i) )
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    correct_result = first_number + second_number
    print(str(first_number) + ' + '+ str(second_number) + ' = ')
    user_result = input('')
    user_result = int(user_result)

    if correct_result == user_result:
        count_correct = count_correct + 1
        print('Congrats - you are correct')
    else:
        count_wrong = count_wrong + 1
        print('Failed - Try again')
    print('---------------------')

# loop has finished
print('Correct answers = '+str(count_correct))
print('wrong answers = '+str(count_wrong))