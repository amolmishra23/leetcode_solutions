class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Logic is we keep last pointer at m+n-1 index.
        Now keep comparing, which element is bigger from the end. nums1[i] or nums2[j]
        Accordingly, we will swap it on. 
        """
        i, j = m-1, n-1
        k = m+n-1
        
        while j>=0:
          if i>=0 and nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i-=1
            k-=1
          else:
            nums1[k] = nums2[j]
            j-=1
            k-=1