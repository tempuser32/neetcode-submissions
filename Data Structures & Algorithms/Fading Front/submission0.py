"""def fading_front_brute(nums):
    remain = nums.copy()
    reached = 0

    while remain:
        for i in range(len(remain)):
            remain[i] -= 1

        reached += remain.count(0)

        if 0 in remain:
            first_zero = remain.index(0)
            remain = remain[:first_zero]

    return reached"""
def fading_front_optimal(nums):
    reached = 0
    minimum_so_far = float("inf")

    for num in nums:
        if num <= minimum_so_far:
            reached += 1
            minimum_so_far = min(minimum_so_far, num)

    return reached
