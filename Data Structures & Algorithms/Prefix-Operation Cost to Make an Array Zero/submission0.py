"""
def prefix_operation_brute(a):
    target = a.copy()
    cost = 0

    while target:
        num = target[-1]
        add = -num

        cost += abs(add)

        target = [x + add for x in target]
        target = target[:-1]

    return cost
    """
def prefix_operation_optimal(a):
    operations = abs(a[-1])

    for i in range(len(a) - 1):
        operations += abs(a[i] - a[i + 1])

    return operations
