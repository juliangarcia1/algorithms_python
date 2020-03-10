# Given nums = [0,0,1,1,1,2,2,3,3,4],
# Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
# It doesn't matter what values are set beyond the returned length.


def removeDuplicates(nums):
    i=1
    ref=0
    while i < len(nums):
        if nums[i]!=nums[ref]:
            ref=ref+1
            nums[ref]=nums[i]
        i=i+1
    return nums, f'Size {ref+1}. Resultant array: {nums[:ref+1]}'


nums_set = [[0,1,2,3,4,5,6,7,8],
            [0,0,1,1,2,2,3,3,4],
            [0,0,1,1,1,2,2,2,2],
            [0,0,1,1,2,2,3,3,3],
            [0,1,1,2,3,3,3,4,5],
           ]
for nums in nums_set:
    print(removeDuplicates(nums))