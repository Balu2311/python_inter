# high closet value
def takeClosest(myList, myNumber):
    newlst = []
    my_list = [int(x) for a,x in enumerate(str(myList))]
    res = [(a, b) for idx, a in enumerate(my_list) for b in my_list[idx + 1:]]
    for i in res:
        i = ''.join(str(x) for x in i)
        newlst.append(int(i))
    newlst.extend(my_list)
    print(newlst)
    newlst.sort()
    l=[]
    for i in newlst:
        if i > myNumber:
            l.append(i)
    return l[0]
myList = 25
myNumber = 2
print(takeClosest(myList,myNumber))
