inp = [2, 5, 2, 1, 2]
inp.sort()  # only if the values are not unique (multiple of the same value in a list)
res = []


def dfs(nums, n, ls=[]):
    if n == 0:
        res.append(ls)
        return

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # this consolidates the repeated values
            continue
        dfs(nums[i:], n - 1, ls + [nums[i]])


dfs(inp, 3, [])  # the three value is the size of the combination / permuatation

print(res)
