# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        self.visited = set()
        self._DFS(robot, (0,0), 0)
        
    def _DFS(self, robot, currCell, currDir):
        robot.clean()
        self.visited.add(currCell)
        
        # turn towrads all 4 directions one-by-one and try moving.
        dirs = ((-1,0), (0,1), (1,0), (0,-1))
        for _ in range(4):
            x, y = currCell[0]+dirs[currDir][0], currCell[1]+dirs[currDir][1]
            if (x,y) not in self.visited and robot.move():
                self.visited.add((x,y))
                self._DFS(robot, (x,y), currDir)
            
            robot.turnRight()
            currDir = (currDir + 1) % 4
            
        
        # backtrack to the previous cell and face the same direction as earlier.
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
