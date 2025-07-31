class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # This set will store all unique results of bitwise ORs from subarrays
        my_set = set(A)  # Start by adding all individual elements (each is a subarray of length 1)

        curr = 0  # Not used in the final logic, can be removed
        prev = set()  # This will store all OR results ending at the previous index
        prev.add(A[0])  # Initialize with the first element
        # Iterate through the array starting from the second element
        for num in A[1:]:
            temp = set()  # Temporary set to store new OR results ending at current index

            # For each OR result from the previous step, OR it with the current number
            for p in prev:
                temp.add(num | p)  # OR operation with current number
                my_set.add(num | p)  # Add result to the global set of unique ORs
            prev = temp  # Update prev to be the current set of ORs
            prev.add(num)  # Also include the current number as a new subarray
            my_set.add(num)  # Add current number to the global set

        return len(my_set)  # The number of unique OR results from all subarrays
