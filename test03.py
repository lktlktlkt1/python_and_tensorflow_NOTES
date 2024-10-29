print("Please type 5 numbers one by one")
num_01 = eval(input("1st number:\n>"))
num_02 = eval(input("2nd number:\n>"))
num_03 = eval(input("3rd number:\n>"))
num_04 = eval(input("4th number:\n>"))
num_05 = eval(input("5th number:\n>"))

if num_01 >= num_02 and num_01 >= num_03 and num_01 >= num_04 and num_01 >= num_05:
    print(f"The biggest number is {num_01}")

if num_02 >= num_01 and num_02 >= num_03 and num_02 >= num_04 and num_02 >= num_05:
    print(f"The biggest number is {num_02}")

if num_03 >= num_02 and num_03 >= num_01 and num_03 >= num_04 and num_03 >= num_05:
    print(f"The biggest number is {num_03}")

if num_04 >= num_02 and num_04 >= num_03 and num_04 >= num_01 and num_04 >= num_05:
    print(f"The biggest number is {num_04}")

if num_05 >= num_02 and num_05 >= num_03 and num_05 >= num_04 and num_05 >= num_01:
    print(f"The biggest number is {num_05}")




print("please type 5 numbers,we will find the biggest one.")
num_bigger = float(input("Please type 1st number:\n>"))

num_02 = float(input("Please type 2nd number:\n>"))
if num_bigger <= num_02:
    num_bigger = num_02

num_03 = float(input("Please type 3rd number:\n>"))
if num_bigger <= num_03:
    num_bigger = num_03

num_04 = float(input("Please type 4th number:\n>"))
if num_bigger <= num_04:
    num_bigger = num_04

num_05 = float(input("Please type 5th number:\n>"))
if num_bigger <= num_05:
    num_bigger = num_05

num_biggest = num_bigger
print(f"The biggest number is {num_biggest}!")




n1 = float(input("first"))
n2 = float(input("second"))
n3 = float(input("third"))
n4 = float(input("fourth"))
n5 = float(input("fifth"))

list_test = [n1,n2,n3,n4,n5]
list_max = max(list_test)
print(list_max)



#找最大，次大数















