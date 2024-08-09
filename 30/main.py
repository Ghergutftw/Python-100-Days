# FileNotFound
# with open("a_file.txt") as f:
#     f.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)
try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except TypeError as error_message:
    print(f"Error: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")

raise TypeError("This is an error message.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


