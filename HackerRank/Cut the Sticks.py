def evaluateLst(min,lst):
    newlst = []
    for i in range(len(lst)):
        if lst[i] - min == 0:
            continue
        newlst.append(lst[i] - min)
    return newlst

def cutTheSticks(arr):
    if not arr:
        return
    maps = []
    maps.append(len(arr))
    while len(arr) != 1 and len(arr) > 1:
        print(len(arr))
        mn = min(arr)
        arr = evaluateLst(mn,arr)
        maps.append(len(arr))
    if maps[-1] == 0:
        maps.pop(-1)
    return maps


l = [5,4,4,2,2,8]
print(cutTheSticks(l))