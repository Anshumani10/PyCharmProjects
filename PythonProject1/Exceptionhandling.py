ItemsInCart = 0

if ItemsInCart !=2:#raise Exception("Products cart count not matched")
    pass
assert ItemsInCart == 0

#try, catch

try:
    with open('testlog.txt', 'r') as file:
        file.read()

except Exception as e:

    print(e)

finally:
    print("Cleaning up resources")

