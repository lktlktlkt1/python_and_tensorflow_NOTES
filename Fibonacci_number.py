def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else :
        return fib(index-1)+fib(index-2)

def main():
    index = eval(input("Please enter a integer:"))
    print("The fibonacci number at",index,"is",fib(index))

main()
