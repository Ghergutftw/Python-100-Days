# new_dict = {new_key:new_value for item in list}
# new_dict = {new_ket:new_value for (key,value) in dict.items() if test}
import random
import pandas

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student: grade for (student, grade) in students_scores.items() if grade > 6}

for (key, value) in passed_students.items():
    print(key)

abibi = {
    "student" : ["Alex", "James"],
    "grade" : ["43", "12"]
}

data_frame = pandas.DataFrame(abibi)
print(data_frame)


for (index,row) in data_frame.iterrows():
    print(row.grade)