class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        def merge(arr, L, M, R):
            left = arr[L:M+1]
            right = arr[M+1: R+1]

            i, l, r = L, 0, 0

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    arr[i] = left[l]
                    l+=1
                else:
                    arr[i] = right[r]
                    r+= 1
                i+= 1
            while l < len(left):
                arr[i] = left[l]
                l += 1
                i += 1

            while r < len(right):
                arr[i] = right[r]
                r += 1
                i += 1
        
        def mergeSort(arr, l, r):
            if l >= r:
                return arr
            m = (l+r) //2 
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        mergeSort(nums, 0, len(nums)-1)
        