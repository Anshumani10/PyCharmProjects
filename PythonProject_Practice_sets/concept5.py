#List of dictionaries
data = [{
    "name" : "Bob", "age" : 25
         },
    {
        "name" : "Alice", "age" : 28
    }]

print(data[1]["name"])


dict = {"name" : "Bob", "age" : 25}

print("************************")

def add(x, y):
    return x + y

print(add(1, 2))

add = lambda x, y : x + y
print(add(1, 3))

print("************************")

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x : x * 2, numbers)
print(list(squared_numbers))

print("***********************")

check = filter(lambda x : x%2 == 0, numbers)
print(list(check))

print("***********************")

num = [6, 3, 5, 1]
print(sorted(num))



