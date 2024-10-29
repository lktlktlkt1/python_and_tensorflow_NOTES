def main():
    n = eval(input("enter a integer:"))
    print(f"The factorial of {n} is {factorial(n)}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

main()