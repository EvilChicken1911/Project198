def swap():
    file1 = input("Enter file 1:")
    file2 = input("Enter file 2:")
    with open(file1, 'r') as a:
        dataA = a.read()
    with open(file2, 'r') as b:
        dataB = b.read()
    with open(file1, 'w') as a:
        a.write(dataB)
    with open(file2, 'w') as b:
        b.write(dataA)

swap()