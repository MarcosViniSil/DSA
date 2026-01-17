def sliding_window_linear(nums:list[int],k:int) -> int:

    n = len(nums)

    max_sum = float("-inf")

    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - nums[i] + nums[i + k]
        max_sum = max(window_sum,max_sum)
    
    return max_sum

print(sliding_window_linear(nums=[5, 2, -1, 0, 3],k=3))
print(sliding_window_linear(nums=[1, 4, 2, 10, 23, 3, 1, 0, 20],k=4))


