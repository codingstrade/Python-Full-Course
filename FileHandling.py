import os
# Create a file in python with second parameter of x
# file = open("testFile.txt", "x")
# file = open("testFile.txt", "r")
# print(file.read())

# file2 = open("testFile.txt", "a")
# file2.write(" coding test in python")
# file2.close()

# file2 = open("testFile.txt", "w")
# file2.write("lets see what happens!")
# file2.close()
# x = create a file
# r = read a file
# a = append the text of the file
# w = overwrites everything in the file

# delete a file
if os.path.exists("fortesting/testFile.txt"):
    os.remove("fortesting/testFile.txt")
else:
    print('File doesnt exist')

# os.rmdir("fortesting")