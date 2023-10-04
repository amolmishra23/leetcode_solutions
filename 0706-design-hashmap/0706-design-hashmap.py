class MyHashMap:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]
    
    def get_bucket(self, key):
        return self.buckets[key % self.bucket_size]
    
    def get_idx_in_bucket(self, bucket, key):
        for i in range(len(bucket)):
            if bucket[i][0]==key: return i
        return -1
    
    def put(self, key: int, value: int) -> None:
        bucket = self.get_bucket(key)
        idx = self.get_idx_in_bucket(bucket, key)
        if idx!=-1:
            bucket[idx][1]=value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.get_bucket(key)
        idx = self.get_idx_in_bucket(bucket, key)
        if idx==-1: return -1
        return bucket[idx][1]

    def remove(self, key: int) -> None:
        bucket = self.get_bucket(key)
        idx = self.get_idx_in_bucket(bucket, key)
        if idx==-1: return 
        del bucket[idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)