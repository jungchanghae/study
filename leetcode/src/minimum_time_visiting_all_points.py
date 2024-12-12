# 1266. Minimum Time Visiting All Points

'''
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
'''

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        n = len(points)
        for i in range(1,n):
            coord_x_diff = abs(points[i-1][0] - points[i][0])
            coord_y_diff = abs(points[i-1][1] - points[i][1])
            result += max(coord_x_diff,coord_y_diff)
        return result
        
if __name__ == '__main__':
    sol = Solution()
    for points in [[[1,1],[3,4],[-1,0]], [[3,2],[-2,2]]]:
        print(sol.minTimeToVisitAllPoints(points))