def twoSum(nums: list[int], target: int) -> list[int]:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    lst.append(i)
                    lst.append(j)
                    break
        return lst

nums = [int(input("Enter list element: ")) for i in range(5)]
target = int(input("Enter target: "))

print(twoSum(nums, target))