b = int(input("输入等腰三角形的底边长度(奇数）："))
a = (b+1)//2
for j in range(a):
    for q in range(b):
        if a-(j-1)<=q<=b+1-(a-j+1):
            print("*",end = "")
        else:
            print(" ",end = "")
    print()