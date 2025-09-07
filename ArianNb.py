age = int(input("enter your age:"))
if 1 <= age <= 6:
    print("you are infant!")
elif 6 <= age <= 18:
    print("you are teenager!")
elif 18 <= age <= 45:
    print("you are young!")
elif 45 <= age <= 60:
    print("you are middle-age!")
else:
    print("you are old!")


names = ['sherko', 'mahsa', 'shadi', 'masoud', 'nima']
for names in names:
    if names[0] == 's':
        print(names)


my_str = 'abv4r3e1'
for i in my_str:
    if i in '0, 1, 2, 3, 4, 5, 6, 7 ,8, 9':
        print(i)

        