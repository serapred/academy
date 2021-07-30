"""
The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [left(i), right(i), height(i)]:

left(i) is the x coordinate of the left edge of the ith building.
right(i) is the x coordinate of the right edge of the ith building.
height(i) is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]


Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.
"""

from heapq import heappush, heappop

# naive solution o(n^2)


def skyline(buildings):
    # consider all possible keypoints (definition)
    # for each, update y to the tallest overlapping building
    # remove the keypoint that violate the property
    pass

# optimization divide and conquer? o(nlogn)
# kinda like merge sort, same recursion pattern


def skyline(buildings):
    if len(buildings) == 1:
        return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

    if len(buildings) == 0:
        return []

    n = len(buildings) // 2
    a = buildings[:n]
    b = buildings[n:]

    # return merge(skyline(a), skyline(b))
    # each iteration has n/2 comparisons
    # for log(n) steps (tree-levels)


# alternative with scanning line (heap) o(nlogn)


def skyline(buildings):

    # points -> events to scan -1: start 1: finish
    points = [(s, h, -1, i) for i, (s, f, h) in enumerate(buildings)]
    points += [(f, h, 1, i) for i, (s, f, h) in enumerate(buildings)]

    # since it is a scan line, points are ordered
    # according x values. when more than one point,
    # has the same x, use height and put starts
    # before finishes.
    points.sort(key=lambda x: (x[0], x[1] * x[2]))

    # scanline: highest top at given point
    # active: in-sight building at given point
    # theoricaly could be done with only one
    # of the two, but access/deletion time
    # would be worst (for 2 reasons..)
    # dummy init
    # NOTE: python heaps are mins, so invert
    #       with minus sign where needed
    scanline, view = [(0, -1)], set([-1])
    ans = []

    # "pseudo-lambdas" (declared once)
    def top(x):
        return x[0][0]

    def top_index(x):
        return x[0][1]

    # iterate over all possible keypoints
    for x, h, ptype, building in points:

        # if the point is of start type
        # it is entering view, otherwise
        # is leaving it
        if ptype == -1:
            view.add(building)
        else:
            view.remove(building)

        # check keypoint first, push after
        if ptype == -1:
            # if the current height is bigger
            # than the biggest in view
            if h > -top(scanline):
                ans.append([x, h])  # it is key
            heappush(scanline, (-h, building))
        # pop first, check keypoint after
        else:
            # lazy deletion of inactive buildings
            # leaves the highest active on top
            while scanline and top_index(scanline) not in view:
                heappop(scanline)

            # if h < current tallest: current building
            # already added to ans, ignore
            # if h > current tallest: impossible
            if -top(scanline) != ans[-1][1]:
                ans.append([x, -top(scanline)])

    return ans


# optimization o(n)? maybe a greedy property
# somwhere (probably not..., but.)
# TODO

def skyline(buildings):
    print('YEAH, U WISH!')
    print('intuitively, it might exist...')
    print('inductively seems not.')
    print('Proof of optimum lowerbound?')
    print('Domain transformation -> Greedy?')


if __name__ == '__smain__':

    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]

    print(skyline(buildings))
