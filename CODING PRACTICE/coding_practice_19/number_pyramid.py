n = int(input())
for i in range(1, n+1):
    spaces = " "*(n - i)
    left_nums = ""
    right_nums = ""
    for j in range(2, i+1):
        left_nums = str(j) + left_nums
        right_nums = right_nums + str(j)
    print(spaces + left_nums + "1"+right_nums)
