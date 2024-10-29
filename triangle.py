#倒置三角形
for j in range(1,101):
    for i in range(1,101):
        if i+j>=101:
            print("*",end = "")
        else:
            print(end=" ")
    print()
#尝试用双重循环写



b = int(input("输入等腰三角形的底边长度(奇数）："))
a = (b+1)//2
for j in range(a):
    for q in range(a-j-1):
            print(end=" ")
    for r in range(j*2+1):
            print("*",end="")
    for s in range(5-j):
            print(end=" ")
    print()


