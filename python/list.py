list_1=[1,2,3]
print(list_1)

list_1.append(4)#append添加到末尾，insert中间加入
print(list_1)

list_1.insert(3,0)#这里前面3表示加进去后的位置
print(list_1)

list_2=list_1.pop()#pop有记忆删除，del无记忆可选择
print(list_2,list_1)

maps=["mirage","ancient","dust2"]
maps.sort()
print(maps)
#line 17 18如何简化?
maps.sort(reverse=True)
maps_reverse=maps
#
print(maps_reverse)

list_1.reverse()
print(list_1)


length_list_1=len(list_1)
print(length_list_1)













