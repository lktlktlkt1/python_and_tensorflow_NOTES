list1=[]
print("enter 5 numbers:")
for i in range(5):
    list1.append(eval(input()))

list1.sort()
print(list1)

s = input("Enter 5 numbers separated by spaces from one line: ")
items = s.split()
list2 = [eval(i) for i in items]
list2.sort()
print(list2)