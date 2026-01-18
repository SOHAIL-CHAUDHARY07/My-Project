line = input("enter a line you wants to add:")
with open("app.py","a+") as file:
    file.write(line)
    file.read()
    print("line added successfully")