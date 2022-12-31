
fo1=open(r"C:\pytonPractice21\day9\abc5.txt")
fo2=open(r"C:\pytonPractice21\day9\abc5.txt")
temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("file copied")

