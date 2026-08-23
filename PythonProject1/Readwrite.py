file = open('test.txt')
#Read all the components of file

#print(file.read(7))
#print(file.readline())
#print(file.readline())

#Print line by line using readline method
#line = file.readline()
#while line !='':
    #print(line)
    #line = file.readline()
# Values in list
for line in file.readlines():
    print(line)

file.close()

