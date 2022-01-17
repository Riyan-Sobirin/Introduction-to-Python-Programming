NIM = "171011400799"
Nama = 'Riyan'
print(Nama + " memiliki NIM " + NIM)

# Escape Character

print("Selamat datang di \"python fundamental\"!")

# String Methods
text = "Belajar Python"

print(text.upper())
print(text.lower())
print(len(text))
print(text.split(' '))
print(text.capitalize())
print(text.index('a'))

# Slicing Strings
#  P  Y   T   H   O   N
#  0  1   2   3   4   5
#  -6 -5  -4  -3  -2  -1
text = "PYTHON"

print(text[0])
print(text[2:])
print(text[:4])
print(text[3:5])
print(text[:])
print(text[-2])
print(text[-4:-1])


# String Concatenation
x = "Belajar"
y = "Python"

print(x + y)
print(x + " " + y)
print(x + " " + y + " " + str(100))


# String  Format
mangga = 5
apel = 7
pisang = 4
text = "Cecep membeli {} mangga, {} apel dan {} pisang."
print(text.format(mangga, apel, pisang))


# In vs Not In
text = "Aku senang belajar Python."
print("Python" in text)
print("Javascript" in text)
print("Javascript" not in text)








