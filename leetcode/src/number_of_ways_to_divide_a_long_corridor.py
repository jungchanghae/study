# 2147. Number of Ways to Divide a Long Corridor

'''
Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.
'''

class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        count = 1
        seat_num = 0
        prev_seat_ind = 0
        for i, s in enumerate(corridor):
            if s == 'S':
                seat_num += 1 
                if seat_num > 2 and seat_num % 2 == 1:
                    count = count * (i-prev_seat_ind)
                prev_seat_ind = i
        if seat_num == 2:
            return 1
        elif seat_num < 2 or seat_num % 2 == 1:
            return 0
        return count % (10**9 + 7)
        
        # "SPS|PPSSPSSSS" 2
        # "SPSP|PSSPSSSS"
        # "SPSPP|SSPSSSS" 5
        # "SPSPPSS|PSSSS"
        # "SPSPPSSP|SSSS"
        # "SPSPPSSPSS|SS"
        
        
if __name__== '__main__':
    sol = Solution()
    # test Case
    for corridor in ["SSPPSPS", "PPSPSP", "S", "SPSPPSSPSSSS"]:
        print(sol.numberOfWays(corridor))
        # Answer : 3 1 0