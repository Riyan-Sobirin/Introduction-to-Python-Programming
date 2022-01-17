# Tuple
# tupleExample = ('Python', 20, 3.8, True, 20)

# print(tupleExample)

# Tuple tidak bisa update nilai
# tupleExample[1] = 30

# print(tupleExample[-2])


# Dictionary
# customer = {
#   "nama": "Cecep",
#   "umur": 30
# }
# customer["pekerjaan"] = "programmer"
# customer.pop("umur")
# customer["nama"] = "Dodi"

# print(customer)
# print(customer['nama'])
# print(customer['umur'])


# Materi Set
# Variable 1
# numbers2 = {3, 4, 10, 7, 8}
# numbers1 = {1, 3, 5, 4, 10}

# Union
# {1, 3, 4, 5, 7, 8, 10}
# numbers_union = numbers1.union(numbers2)
# print(numbers_union)

# Difference
# {1, 5}
# difference1 = numbers1.difference(numbers2)
# print(difference1)

# Variable 2
numbers1 = {1, 3, 5, 4, 10}
numbers2 = {3, 4, 10, 7, 8}

# Symetric Difference
# {1, 5, 7, 8}
# sym_difference = numbers1.symmetric_difference(numbers2)
# print(sym_difference)

# Intersection
# {10, 3, 4}
intersect = numbers1.intersection(numbers2)
print(intersect)