list1=[1,2,5,3,6,9,8,7,10,12,23,34]
print(list1)
def list_data(list1):
    l=len(list1)//2
    first=list1[:l]
    first=sorted(first)
    last=list1[l:]
    last=sorted(last, reverse=True)
    output= first +last
    print(output)
list_data(list1)
