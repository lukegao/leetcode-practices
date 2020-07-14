
import collections
import heapq

Building = collections.namedtuple('Building', ('left', 'right', 'height'))
HeightRight = collections.namedtuple('HeightRight', ('height', 'right'))
KeyPoint = collections.namedtuple('KeyPoint', ('left', 'height'))


class Solution(object):

    def getSkyline(self, buildings):
        buildings = [Building(b[0], b[1], b[2]) for b in buildings]
        skyline, liveHR = [], []
        i, n = 0, len(buildings)

        while i < n or liveHR:
            if not liveHR or (i < n and buildings[i].left <= -liveHR[0].right):
                x = buildings[i].left
                while i < n and buildings[i].left == x:
                    heapq.heappush(liveHR, HeightRight(-buildings[i].height, -buildings[i].right))
                    i += 1
            else:
                x = -liveHR[0].right
                while liveHR and -liveHR[0].right <= x:
                    heapq.heappop(liveHR)

            height = -liveHR[0].height if liveHR else 0
            if not skyline or height != skyline[-1].height:
                skyline.append(KeyPoint(x, height))

        return [[kp.left, kp.height] for kp in skyline]


if __name__ == '__main__':
	s = Solution()
	test = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

	print(s.getSkyline(test))
