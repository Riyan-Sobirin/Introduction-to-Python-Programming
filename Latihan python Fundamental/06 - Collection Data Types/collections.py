# # append , insert (Create)
# listExample = [42, 'Python', 3.85, 50]
# listExample.insert(1, 'Data Science')
# listExample.append('Javascript')
# print(listExample)


# # remove, pop, del, clear (Delete)
# listExample = [42, 'Python', 3.85, 50]
# print(listExample)
# # remove
# listExample.remove('Python')
# print(listExample)


# listExample = [42, 'Python', 3.85, 50]
# print(listExample)
# # pop
# listExample.pop()
# print(listExample)


# listExample = [42, 'Python', 3.85, 50]
# print(listExample)
# # del
# del listExample[2]
# print(listExample)


# listExample = [42, 'Python', 3.85, 50]
# print(listExample)
# # clear
# listExample.clear()
# print(listExample)


# List Iteration (Read) - berfungsi untuk logic tambahan
# listExample = [40, 55, 20, 75, 80]

# for item in listExample:
#   if item % 2 == 0:
#     print(item)


#  Check if an item exists in list (Read)
listExample = [40, 55, 20, 75, 80]

# if 40 in listExample:
#   print("Terdapat angka 40 di dalam listExample")


# Methods: len, copy, concat (+ dan extend), index, sort, reverse (update)
listExample = [40, 55, 20, 75, 80]

# # Copy
# listExample2 = listExample.copy()
# listExample2[0] = 100
# print(listExample)
# print(listExample2)


# length = len(listExample)


# listExample = [40, 55, 20]
# listExample2 = [70, 100]
# concat (+)
# print(listExample+listExample2)

# # concat (extend)
# listExample.extend(listExample2)
# print(listExample)

# index
listExample = [40, 55, 20]
# print(listExample.index(55))

# Sort
# listExample.sort()
# print(listExample)

# reverse
listExample.reverse()
print(listExample)