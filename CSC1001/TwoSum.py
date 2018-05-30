###
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
###

## Sol1:
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numo = nums
        nums = sorted(nums)
        for n1 in range(len(nums)):
            for n2 in range(n1 + 1, len(nums)):
                if n1 != n2 and nums[n1] + nums[n2] == target:
                    n1s = numo.index(nums[n1])
                    numo.reverse()
                    n2s = len(nums) - numo.index(nums[n2]) -1
                    return [n1s,n2s]
                elif nums[n1] + nums[n2] > target:
                    break

## Sol2:
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         d = {}
#         for i in range(len(nums)):
#             if nums[i] in d:
#                 return [d[nums[i]], i]
#             else:
#                 d[target - nums[i]] = i