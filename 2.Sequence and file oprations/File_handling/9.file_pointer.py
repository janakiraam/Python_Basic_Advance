# .tell() method tells the position of file pointer

fo = open('bye.txt', 'r')
print(fo.tell())
fo.read(2)
print(fo.tell())

fo.close()