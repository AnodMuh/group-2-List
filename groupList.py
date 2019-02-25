def groupList(aList):
    grouppedList = []
    for i in aList:
        for j in i:
            grouppedList.append(j)
    return grouppedList

alist=[[8,5],[2,7]]
print(groupList(aList))