"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

--------------
Constraints
1.You may assume the interval's end point is always bigger than its start point.
2.Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

"""


def eraseOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0

    remove = 0
    intervals = sorted(intervals, key=lambda x: x[1])

    end = intervals[0][0]
    for times in intervals:
        start = times[0]
        if start < end:
            remove += 1
        else:
            end = times[1]
    return remove


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals = [[1, 2], [1, 2], [1, 2]]
intervals = [[1, 2], [2, 3]]

print(eraseOverlapIntervals(intervals))