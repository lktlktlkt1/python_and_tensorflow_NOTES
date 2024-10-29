for second in range(1,10):
    for first in range(1,10):
        if first <= second :
            print(f"{first}*{second}={first*second}",end ="\t")
        else :
            print("")
            break

