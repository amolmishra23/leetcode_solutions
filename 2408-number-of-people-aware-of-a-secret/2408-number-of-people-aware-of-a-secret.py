class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Buffer size to avoid index out of bounds
        buffer_size = (n << 1) + 10  # n * 2 + 10
        
        # Track exact people knowing secret on certain day
        people_knowing_secret = [0] * buffer_size
        
        # Track what new people know secret on each day
        new_people_each_day = [0] * buffer_size
        
        # Day 1: one person initially knows the secret
        new_people_each_day[1] = 1
        
        # Simulate each day from 1 to n
        for day in range(1, n + 1):
            if new_people_each_day[day] > 0:
                # Add new people who learn the secret today
                people_knowing_secret[day] += new_people_each_day[day]
                
                # These people will forget the secret after 'forget' days
                people_knowing_secret[day + forget] -= new_people_each_day[day]
                
                # Calculate when these people can start sharing and stop sharing
                start_sharing_day = day + delay
                stop_sharing_day = day + forget
                
                # Each person shares with one new person per day during their sharing period
                for sharing_day in range(start_sharing_day, stop_sharing_day):
                    new_people_each_day[sharing_day] += new_people_each_day[day]
        
        # Calculate total people who know the secret on day n
        MOD = 10**9 + 7
        total_people_knowing = sum(people_knowing_secret[:n + 1])
        
        return total_people_knowing % MOD