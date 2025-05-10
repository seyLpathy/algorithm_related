def getmaxofwindows(arr,width):
    # width: the window width
    # arr : the array
    if not arr or width < 1  or width > len(arr):
        return None
    qmax = []
    result = []
    length = len(arr)
    for i in range(length):
        while qmax and qmax[-1]<=arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0]==i-width:
            qmax.pop(0)
        if i>=width-1:
            result.append(arr[qmax[0]])
    return result

arr = [2,3,5,7,8,5,2,6,3,8,9,14]
width = 3
print(getmaxofwindows(arr,width))
