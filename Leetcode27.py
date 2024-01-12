def removeElement(nums: list[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

nums = [int(input("Enter list element: ")) for i in range(4)]
val = int(input("Enter val: "))

print(removeElement(nums, val))