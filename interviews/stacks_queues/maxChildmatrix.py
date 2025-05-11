def max_child_matrix(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    max_area = 0
    height = [0] * len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            height[col] = 0 if matrix[row][col] == 0 else height[col] + 1
        max_area = max(max_area, max_rec_from_top(height))
    return max_area


def max_rec_from_top(height):
    if not height or len(height) == 0:
        return 0
    max_area = 0
    stack = []
    length = len(height)
    for i in range(length):
        while stack and height[i] <= height[stack[-1]]:
            j = stack.pop()
            k = -1 if not stack else height[j]
            cur_area = (i - k - 1) * height[j]
            max_area = max(max_area, cur_area)
        stack.append(i)
    while stack:
        j = stack.pop()
        k = -1 if not stack else stack[-1]
        cur_area = (len(height) - k - 1) * height[j]
        max_area = max(max_area, cur_area)
    return max_area
maxtrix=[[1,0,1,1],[1,1,1,1],[1,1,1,0]]
print(max_child_matrix(maxtrix))