class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            root = i
            left = 2 * i + 1
            right = left + 1
            if left < n and nums[left] > nums[root]:
                root = left
            if right < n and nums[right] > nums[root]:
                root = right
                
            if root != i:
                nums[i], nums[root] = nums[root], nums[i]
                heapify(n, root)
                
        def heapsort():
            n = len(nums)
            
            for i in range(n//2 -1, -1, -1):
                heapify(n, i)
            
            for i in range(n-1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)
                
        heapsort()
        return nums