file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\nRead in parts\n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
file.write('Hi, I am Brian and I am 14 years old')
file.close()