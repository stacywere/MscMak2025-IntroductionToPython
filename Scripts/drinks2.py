import sys
age = int(sys.argv[1])
if age < 7:
    print('Have a glass of milk.')
elif age>=7 and age <21:
    print('Have a coke.')
else:
    print('Have a martini.')