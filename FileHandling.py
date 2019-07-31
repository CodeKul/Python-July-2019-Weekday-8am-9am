'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# f = open("abc.txt", "r")

# s = f.read()
# print(s)

# s = f.read(5)
# print(s)

# s = f.readline(8)
# print(s)

# s = f.readlines()
# print(s)

# f.seek(12,0)
# s = f.read(7)
# print(s)

# Write

f = open("abc.txt", "a")

f.write("abcdefghijkl")

f.close()