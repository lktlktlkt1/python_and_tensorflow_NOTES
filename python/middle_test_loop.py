total = 0
while True:
    response = input("Please enter the next number,leave other string to end\n")
    if not response.isdigit():
        break
    total += int(response)

print(f"the total number is {total}")

#小数？