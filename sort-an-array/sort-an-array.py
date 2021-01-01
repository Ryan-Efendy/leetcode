class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums: List[int], i: int, j: int):
            if i < j:
                pivot = nums[i + (j-i)//2]
                index = partition(nums, i, j, pivot)
                quickSort(nums, i, index-1)
                quickSort(nums, index, j)
            
        def partition(nums: List[int], i:int, j:int, pivot:int): # -> int
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            return i
        
        quickSort(nums, 0, len(nums)-1)
        return nums
