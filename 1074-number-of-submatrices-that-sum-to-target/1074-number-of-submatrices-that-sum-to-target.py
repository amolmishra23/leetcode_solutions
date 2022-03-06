class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        One of the most trikiest questions solved till date. Thanks to this video. https://www.youtube.com/watch?v=i5UoDZbQ94Q&feature=emb_title
        This question is, in extension to https://leetcode.com/problems/subarray-sum-equals-k/
        First of all if our matrix is 
        1 1 1 1
        1 1 1 1
        1 1 1 1
        1 1 1 1
        We calculate the pre_sum column wise, and convert our matrix to
        1 2 3 4
        1 2 3 4
        1 2 3 4
        1 2 3 4
        
        Now we have 3 pointers. start_col, to mark the starting column. curr_col to mark last column in current traversal and curr_row to mark the row.
        
        Reset happens at counter, sum_ = {0:1}, 0 because, every curr_col we newly calculate sum_ over all our rows, in the previously mentioned example lets say col2, with all values as 2. Our sum goes on from being 2,4,6,8. When we are 8, we need to know if 4 occured in this cou\lumn, so we can get rid of 4 and add a valid target sub matrix. 
        
        If we only want the sum from [0,1] to [0,2], Its as simple as [0,2]-[0,0] because of the presum we calculated. Is taken care by the condition matrix[curr_row][start_col-1] if start_col>0 else 0. Based on whatever is our start_col for that particular iteration. 
        
        Rest, we are just hoping to find sum_target in counter. So if we remove that part, we are equal to our target sum and a valid submatrix is found. 
        
        Basic idea is, the sum is calculated in the following sequence
        1. [0..0], [0..1], [0..2], [0..3]
        2. [1..1], [1..2], [1..3]
        3. [2..2], [2..3]
        4. [3..3]
        
        This above was just columns, We also need to do across rows. Hence another iteration too. 
        """
        
        rows, cols, count = len(matrix), len(matrix[0]), 0
        
        for i in range(rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i][j-1]
        
        for start_col in range(cols):
            for curr_col in range(start_col, cols):
                counter, sum_ = {0:1}, 0
                for curr_row in range(rows):
                    sum_ += matrix[curr_row][curr_col] - (matrix[curr_row][start_col-1] if start_col>0 else 0)
                    count += counter.get(sum_-target, 0)
                    counter[sum_] = counter.get(sum_, 0)+1
        
        return count