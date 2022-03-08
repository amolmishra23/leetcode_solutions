class SnapshotArray(object):

    def __init__(self, n):
        # initially all are at version -1. non existant
        # current snap id, lets make it 0. 
        # we keep appending element as [self.snap_id, val]
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        # while snapshotting, just curr snapshots we make it as 1 version ahead
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        # find the location where it is present in the array
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        # return the element. 
        return self.A[index][i][1]
