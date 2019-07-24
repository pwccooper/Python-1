print('********************')
print('    WELCOME!   ')
print('********************')

age = input('Please print your age: ')

print(age)
print(type(age))

the_age = int(age)
print(the_age + 1)

name = input("Please tell me your name: ")

print("Welcome: " + name )
name_length = len(name)
print('Your name has' + str(name_length) + 'letters on it')

print(name.upper())
print(name.lower())
print(name.replace('S', 'Z'))

has_E = "e" in name
print("Your name contains e: " + str(has_E))

print('~' * 20)
pet = input('What pet do you have? ')

if(pet == 'Lion'):
    print("well done!")
elif (pet == 'Cat'):
    print("Getting there!")
else:
    print("Get a Lion!")