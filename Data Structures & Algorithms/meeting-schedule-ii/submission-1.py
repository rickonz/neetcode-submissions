"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time_steps = []
        for interval in intervals:
            time_steps.append((interval.start, 1))
            time_steps.append((interval.end, -1))
        
        time_steps.sort(key=lambda x: (x[0], x[1]))
        #Changed time_steps.sort(key=lambda x: x[0]) to time_steps.sort(key=lambda x: (x[0], x[1])) to ensure meeting endings are processed before starts at the same timestamp.

        min_req_room = 0
        curr_req_room = 0
        for time, count in time_steps:
            curr_req_room += count
            min_req_room = max(min_req_room, curr_req_room)
        
        return min_req_room


# idea -- sweep line
# split start and end timestamp, count as +1 or -1, record max_room reached

