from numpy import array, roll
class Solution(object):
    @staticmethod
    def shiftGrid(grid, k):  # Solution 1
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        flatgrid = []
        for i in range(m):
            flatgrid = flatgrid + grid[i]

        l = len(flatgrid)
        if l != k and l != 1:
            for i in range(k):
                flatgrid = flatgrid[-1:] + flatgrid[:-1]
            return (array(flatgrid).reshape((m, n))).tolist()
        return grid

    @staticmethod
    def shiftGridNumpy(grid, k):
        m = len(grid)
        n = len(grid[0])
        flatgrid = list(array(grid).flatten())
        l = len(flatgrid)
        if l != k and l != 1:
            return ((roll(flatgrid, k)).reshape((m, n))).tolist()
        return grid


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
Solution.shiftGrid(grid, k)
