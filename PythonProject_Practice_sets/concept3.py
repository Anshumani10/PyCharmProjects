with open("test.txt", "w") as f:
    f.write("Hello World")

try :
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print(e)

