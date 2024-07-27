with open('./Input/Names/invited_names.txt',mode='r') as names:
    all_names = names.readlines()

with open('./Input/Letters/starting_letter.txt', mode='r') as file:
    letter = file.read()
    for name in all_names:
        stripped_name = name.strip()
        new_letter = letter.replace('[name]', stripped_name)
        # creating
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as complete:
            complete.write(new_letter)

