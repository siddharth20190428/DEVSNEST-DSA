"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

---------------
Constraints
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

"""


def merge(intervals):
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


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1,4],[4,5]]

print(merg(intervals))