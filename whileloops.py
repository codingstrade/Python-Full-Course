"""
 loops are control structures that allow you
 to execute a block of code multiple times.
 There are two types of loops in Python: for loops and while loops.
"""

count = 1

while count <= 5:
    print(count)
    count = count + 1 # count +=1

# # break keyword
# count = 1
# while count < 5:
#     print(count)
#     if count == 3:
#         break
#     count = count + 1  # count =+1

#break
i = 0

while i < 10:
    i += 1
    if i == 6:
        continue
    print(i)
