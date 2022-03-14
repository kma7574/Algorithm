def removeDuplicates(self, nums: List[int]) -> int:
    for i in nums:
        while nums.count(i) > 1:  # 중복된 숫자가 모두 제거될 때 까지 반복하며 제거
            nums.remove(i)
    return len(nums)