def check_alternating(nums):
    for i in range(1, len(nums)):
        if nums[i] % 2 == nums[i - 1] % 2:
            return i
    return 0

numbers = [2, 5, 4, 7, 6, 9]
result = check_alternating(numbers)

if result == 0:
    print("Четные и нечетные числа чередуются.")
else:
    print(f"Закономерность нарушается на позиции {result}.")
