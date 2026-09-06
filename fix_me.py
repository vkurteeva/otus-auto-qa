def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count


result = calculate_average([10, 15, 20])
print("The average is:", result)
