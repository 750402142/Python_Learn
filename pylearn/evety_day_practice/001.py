


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #在不创建新的列表的情况下
    slow = 0
    fast = 0
    while fast<len(nums):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow]= nums[fast]
        fast += 1
    return slow+1
lists = [1,2,3,3]
length = removeDuplicates(lists)
print(lists)