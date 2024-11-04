def getMatrix():
    matrix=[]
    numberofRows = eval(input("Enter the number of rows:"))
    numberofColumns = eval(input("Enter the number of column:"))
    for row in range(numberofRows):
        matrix.append([])
        for column in range(numberofColumns):
            value = eval(input("PLease enter a number and press Enter:"))
            matrix[row].append(value)

    return matrix

def accumulate(n):
    total = 0
    for row in n:
        total += sum(row)

    return total

def main():
    n = getMatrix()
    print(n)

    print("\nThe sum of all elements is",accumulate(n))

main()
