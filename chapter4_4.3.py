list=[1,2,3,4]
it=iter(list)
print(next(it),end=" ")
print(next(it))

maps=["mirage","ancient","dust_2"]
for map in maps:
    print(map)

for map_like in maps:
    print(f"everyone like {map_like.title()}\n")
    #title为每一个元素print消息

for count in range(1,5):#到4截止！
    print(count)
    
print(end=" \n")

for count_2 in range(5):#from zero!
    print(count_2)

#print(list(range(2)))

##
squares=[]
for value_2 in range(1,11):
    square = value_2**2
    squares.append(square)

print(squares)
## 

#min(),max(),sum()

squares=[value**2 for value in range(1,11)]
print(squares)
#line25-28

#practice4.3
counts=[]
for count4_3 in range(1,21):
    count_range=count4_3
    counts.append(count_range)
print(counts)