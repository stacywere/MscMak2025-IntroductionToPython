import sys
#age = sys.argv[1]
age = int(input('Enter your age:'))
if age < 7:
    print('Have a glass of milk.')
elif age>=7 and age <21:
    print('Have a coke.')
else:
    print('Have a martini.')