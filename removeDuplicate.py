class Solution:
    def removeDuplicate(self, nums):
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count += 1
        return count
    
sl = Solution()
print(sl.removeDuplicate([1, 1, 2, 3, 3]))