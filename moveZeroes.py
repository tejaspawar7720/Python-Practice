class Solution:
    def moveZeroes(self, nums):
        res = []
        count = 0
        for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(nums[i])
                elif nums[i] == 0:
                    count += 1
        for j in range(count):
                        res.append(0)
        return res
    
sl = Solution()
print(sl.moveZeroes([0,1,0,12,3]))