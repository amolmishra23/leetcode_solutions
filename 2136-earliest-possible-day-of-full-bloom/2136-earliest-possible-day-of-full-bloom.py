class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        Follow a greedy approach here, and do in descending growTime.
        To let maximum growTime execute first, so that in parallel we can have other planting times. 
        """
        bloom = sorted(zip(plantTime, growTime), key=lambda x: -x[1])
        max_time, plant_time = 0, 0
        for plant, grow in bloom:
            curr_time = plant_time + plant + grow
            max_time = max(max_time, curr_time)
            plant_time += plant
            
        return max_time