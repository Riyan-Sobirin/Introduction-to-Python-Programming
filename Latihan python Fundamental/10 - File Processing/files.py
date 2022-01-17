# Reading (Read Text)
# file = open("10 - File Processing/coding-studio.txt", "r")

# print(file.read())

# Writing (update text)
# file = open("10 - File Processing/coding-studio.txt", "w")
# file.write("Ini adalah text yang baru")
# file.close()

# Append (Add Text)
file = open("10 - File Processing/coding-studio.txt", "a")
file.write("\nIni adalah text yang diappend dengan enter")
file.close()
