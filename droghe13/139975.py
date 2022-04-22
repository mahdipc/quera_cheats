def lengthOfLIS(nums) -> int:
    def binary_search(val, arr) -> int:
        left, right = 0, len(arr)-1

        while left <= right:
            mid = left + (right - left) // 2

            if val < arr[mid]:
                right = mid - 1
            elif val > arr[mid]:
                left = mid + 1
            else:
                return mid

        return left

    sub = []

    for num in nums:
        if not sub or num > sub[-1]:
            sub.append(num)
            continue

        sub[binary_search(num, sub)] = num

    return len(sub)


n = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]
print(lengthOfLIS(numbers))
