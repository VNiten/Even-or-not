## This code is used to tell if the entered number is even or not.

number= int(input('Write a number: '))
if number % 2 == 0:
    print('The number ' + str(number) + ' is even')
else:
    print('The number ' + str(number) + ' is not even')
