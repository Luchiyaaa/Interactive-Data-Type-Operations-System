print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")


while True:
    choice = input("Enter the number of your choice (1-4): ")

    if choice == '1':
        print('Your choice - Strings:')
        sentence = input()
        new_sentence = sentence.replace('fun', 'awesome')
        print(new_sentence.upper())

    elif choice == '2':
        print('Your choice - Numbers:')
        first_number = int(input())
        second_number = int(input())
        if second_number == 0:
            print('ZeroDivisionError!\nCannot divide by zero.\nPlease, enter valid number.')
        else:
            print(f'Addition of the numbers: {first_number} + {second_number} = {first_number + second_number}.')
            print(f'Subtraction of the numbers: {first_number} - {second_number} = {first_number - second_number}.')
            print(f'Multiplication of the numbers: {first_number} * {second_number} = {first_number * second_number}.')
            print(f'Division of the numbers: {first_number} / {second_number} = {first_number / second_number}.')
            print(f'{first_number} raised to power of {second_number} = {first_number ** second_number}.')

    elif choice == '3':
        print('Your choice - Booleans:')
        luchi_uchi = True
        python_is_fun = False
        print(f'The result of {luchi_uchi} and {python_is_fun} is: {luchi_uchi and python_is_fun}')
        print(f'The result of {luchi_uchi} or {python_is_fun} is: {luchi_uchi or python_is_fun}')
        print(f'The result of not {luchi_uchi} is: {not luchi_uchi}')
        print(f'The result of not {python_is_fun} is: {not python_is_fun}')
        print(f'The result of {10 > 5} and {5 == 5} is: {10 > 5 and 5 == 5}')


    elif choice == '4':
        print('Your choice - Additional Data Types (List, Tuple, Dictionary):\n')
        print('List:')
        my_list = ['6', '27', 'Bella', 'True']
        print(f'This is the current list: {my_list}.\nIf you want to add new item enter - Yes\n'
              f'If you want to remove an item enter - No')
        action = input()
        if action == 'Yes':
            new_item = input()
            my_list.append(new_item)
            print(f'Updated list: {my_list}\nThe forth element of the list is: {my_list[4]}\n')
        if action == 'No':
            print('Enter name of the item you want to delete:')
            target = input()
            my_list.remove(target)
            print(my_list)

        print('Tuple:')
        my_tuple = ('blueberry', 'watermelon', 'banana')
        print(f'This is the current tuple: {my_tuple}.\nThe length of the tuple is: {len(my_tuple)}\n'
              f'If you want to add new item enter - Yes\n'
              f'If you want to remove an item enter - No')
        action = input()
        if action == 'Yes':
            print('Tuples are immutable so you cannot modify them.\n')
        if action == 'No':
            print('Tuples are immutable so you cannot modify them.\n')

        print('Dictionary:')
        my_dictionary = {
            'name': 'Luchia',
            'age': '25',
            'in happy mood': True
        }
        print(f'This is the current dictionary: {my_dictionary}\nIf you want to add new item enter - Yes\n'
              f'If you want to remove an item enter - No')
        action = input()
        if action == 'Yes':
            print('Enter a key and a value:')
            new_key = input()
            new_value = input()
            my_dictionary[new_key] = new_value
            print(my_dictionary)
        if action == 'No':
            print('Enter the key you want to remove:')
            dictionary_target = input()
            my_dictionary.pop(dictionary_target)
            print(my_dictionary)

    else:
        print('Invalid selection of data type.\nPlease try again.')
        exit()
