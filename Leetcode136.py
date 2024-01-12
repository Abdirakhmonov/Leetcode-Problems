def singleNumber(nums: list[int]) -> int:
        for i in range(len(nums)):
           if (nums.count(nums[i])) == 1:
               n = nums[i]
               break
        return n

nums = [int(input("Enter list element: ")) for i in range(5)]
print(singleNumber(nums))