# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)
with open("my_file.txt", "a") as file:
    content = file.write("COCK")
    print(content)

