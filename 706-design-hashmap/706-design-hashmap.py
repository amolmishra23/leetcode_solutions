class MyHashMap:

    def __init__(self):
        self.BUCKET_SIZE = 1000
        self.buckets = [[] for _ in range(self.BUCKET_SIZE)]  # bucket[i] stores a list of (key, value)

    def getBucket(self, key):
        return self.buckets[key % self.BUCKET_SIZE]

    def findIndexOfKey(self, bucket, key):
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        bucket = self.getBucket(key)
        nodeIndex = self.findIndexOfKey(bucket, key)
        if nodeIndex != -1:
            bucket[nodeIndex][1] = value
        else:
            bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.getBucket(key)
        nodeIndex = self.findIndexOfKey(bucket, key)
        if nodeIndex == -1: return -1
        return bucket[nodeIndex][1]

    def remove(self, key: int) -> None:
        bucket = self.getBucket(key)
        nodeIndex = self.findIndexOfKey(bucket, key)
        if nodeIndex == -1: return
        del bucket[nodeIndex]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)