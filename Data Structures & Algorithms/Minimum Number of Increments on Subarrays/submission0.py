"""def min_number_operations_brute(target):
    remaining = target.copy()
    operations = 0

    while any(remaining):
        i = 0
        while i < len(remaining):
            if remaining[i] == 0:
                i += 1
            else:
                operations += 1

                while i < len(remaining) and remaining[i] > 0:
                    remaining[i] -= 1
                    i += 1
    return operations
  """
def min_number_operations(target):
    operations = 0
    previous = 0

    for height in target:
        operations += max(0, height - previous)
        previous = height

    return operations
