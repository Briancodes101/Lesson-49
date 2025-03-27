file_read = open('Codingal.txt', 'r')
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode....")
file_write.write("Hi, I am Brian and I love to code")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("File in write mode....")
file_append.write("Hi, I am Brian")
file_append.close()