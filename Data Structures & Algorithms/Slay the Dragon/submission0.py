"""def minimum_coins_brute(nums, dragon):
    total = sum(nums)
    best = float("inf")

    attack_required = dragon[0]
    defense_required = dragon[1]

    for attacker in nums:
        defenders = total - attacker

        coins = max(0, attack_required - attacker)
        coins += max(0, defense_required - defenders)

        best = min(best, coins)

    return best"""

def minimum_coins_optimal(nums, dragon):
    nums = sorted(nums)
    total = sum(nums)
    attack_required = dragon[0]
    defense_required = dragon[1]
    left = 0
    right = len(nums)
    while left < right:
        middle = (left + right) // 2
        if nums[middle] < attack_required:
            left = middle + 1
        else:
            right = middle

    index = left
    best = float("inf")

    if index < len(nums):
        attacker = nums[index]
        defenders = total - attacker
        coins = max(0, attack_required - attacker)
        coins += max(0, defense_required - defenders)
        best = min(best, coins)

    if index > 0:
        attacker = nums[index - 1]
        defenders = total - attacker

        coins = max(0, attack_required - attacker)
        coins += max(0, defense_required - defenders)

        best = min(best, coins)

    return best
