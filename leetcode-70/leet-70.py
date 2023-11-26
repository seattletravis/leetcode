
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    2:2
    3:3
    4:5
    5:8
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    pointer = 3
    a = 1
    b = 2

    while pointer < n + 1:
        temp = a
        a = b
        b = temp + b
        pointer += 1
    return b 

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
