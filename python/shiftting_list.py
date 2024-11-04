def shift(list):
    temp = list[0]
    for i in range(1,len(list)):
        list[i-1]=list[i]
    list[len(list)-1]=temp

list=[1,2,3,4]
print(list)
shift(list)
print(list)