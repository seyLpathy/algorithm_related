# 给定数组arr 和整数num，共返回有多少个子数组满足如下情况：
# max(arr[i..j]) - min(arr[i..j]) <= num
# max(arr[i..j])表示子数组arr[i..j]中的最大值，min(arr[i..j])表示子数组arr[i..j]中的最小值
def get_num(arr, num):
    if not arr or len(arr) == 0 or num == 0:
        return 0
    qmin = []
    qmax = []
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            if not qmin or qmin[-1] != j:
                while qmin and arr[qmin[-1]] >= arr[j]:
                    qmin.pop()
                qmin.append(j)
                while qmax and arr[qmax[-1]] <= arr[j]:
                    qmax.pop()
                qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j = j + 1
        res += j - i
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        i += 1
    return res
