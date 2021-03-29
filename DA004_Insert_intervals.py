"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

-------------------
Constraints
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 10^5
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 10^5

"""


def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda x: x[0])
    res = []
    curr = intervals[0]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if curr[1] < interval[0]:
            res.append(curr)
            curr = interval
        else:
            curr[1] = max(curr[1], interval[1])
    res.append(curr)

    return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]

# intervals = []
# newInterval = [5,7]

# intervals = [[1,5]]
# newInterval = [2,3]

# intervals = [[1,5]]
# newInterval = [2,7]

print(insert(intervals, newInterval))
