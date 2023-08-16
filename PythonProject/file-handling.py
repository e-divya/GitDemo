print("-------------File Handling in Python with condition------------------")
# #Read a file in Python
#
# file = open('test.txt')
# #Read by characters
# print(file.read(11)) #reads first 11 characters from the file
#
# #Read one single line at a time readLine()
# print(file.readline())
#
# #Line by Line Reading
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
# for line in file.readlines():
#     print(line)
# file.close()
#Reverse content of file and write
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


