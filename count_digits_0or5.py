n = int(input("Please type an integer here\n>"))

count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10

print(count)

