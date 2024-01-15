# for i loop
for i in range(1, 11):
    print(i)
print('------------')
for i in range(11):
    print(i)
print('----- continue -- break -------')
for i in range(1, 11):
    if i in (3, 5):
        continue    # skip this iteration
    elif i == 8:
        break       # end the loop
    print(i, end=' ')

print('\n---------- Nested Loops : Mutliplication table -----')
for i in range(1, 11):
    for j in range(1, 11):
        if i * j < 10:
            print(i * j, end='   ')
        else:
            print(i * j, end='  ')
    print()