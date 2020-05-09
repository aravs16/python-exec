f = open('test.csv', 'r')

for line in f:
    print(line)

f.close()

fw = open('new.txt', 'w')

fw.write("Hello World")

fw.close()

