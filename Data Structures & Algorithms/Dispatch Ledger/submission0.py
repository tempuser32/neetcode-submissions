"""def comes_before(a, b):

    if a[1] != b[1]:
        return a[1] < b[1]

    if a[2] != b[2]:
        return a[2] > b[2]

    return False  

def order_dispatches_brute(records):
    remaining = records.copy()
    answer = []

    while remaining:
        best_index = 0

        for i in range(1, len(remaining)):
            if comes_before(remaining[i], remaining[best_index]):
                best_index = i

        answer.append(remaining.pop(best_index)[0])
    return answer

    """

def order_dispatches(records):
    ordered = sorted(
        records,
        key=lambda x: (x[1], -x[2])
    )

    return [record[0] for record in ordered]
