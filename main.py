def bubble(list1):
    a = len(list1)-1
    x = False
    while not x:
        x = True
        for i in range(0,a):
            if list1[i] > list1[i+1]:
                x = False
                list1[i], list1[i+1] = list1[i+1],list1[i]
    return list1

print(bubble([5,6,4,8,2,9]))
print(bubble([2,6,5,4,7,2,59,14]))
print(bubble([54,65,89,24,15,75]))

