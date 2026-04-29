class solution:
    def twoSum(self, lis, target):
        for i in range(len(lis)):
            for j in range(i+1, len(lis)):
                if lis[i] + lis[j] == target:
                    return i,j

sl =solution()               
print(sl.twoSum([2, 7, 11, 15 ], 9))