numbers = [1, 2, 3]
name = "Angela"
# crazy
# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
new_nums = [n + 1 for n in numbers]
new_name = [n.upper() for n in name]
new_numbers = [n * 2 for n in range(1, 6)]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

new_names = [name.upper() for name in names if len(name) <= 4]


