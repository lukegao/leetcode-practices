from typing import List


class Point:

    def __init__(self, ords):

        self.ords = ords
        self.key = ords[0] ** 2 + ords[1] ** 2

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return self.key == other.key

    def __le__(self, other):
        return self.key <= other.key

    def __ge__(self, other):
        return self.key >= other.key

    def __repr__(self):
        return f"<{id(self)}: {self.ords} --> {self.key}>"


class MinHeap:

    def __init__(self):
        self.data = [None]

    @staticmethod
    def from_list(inputs):
        heap = MinHeap()
        heap.data.extend(inputs)
        heap.heapify()

        return heap

    def __len__(self):
        return len(self.data) - 1

    def _siftdown(self, index):
        # recursively compare to its children
        if index > len(self):
            return None

        current = index

        while current <= len(self):
            left = current * 2
            right = current * 2 + 1

            if right <= len(self) and self.data[right] < self.data[left]:
                min_child = right
            elif left <= len(self):
                min_child = left
            else:
                break

            if self.data[current] > self.data[min_child]:
                self.data[current], self.data[min_child] = self.data[min_child], self.data[current]
                current = min_child
            else:
                break

        return current

    def _siftup(self, index):
        # recursively compare to its parent
        if index > len(self):
            return None
        current = index

        while current > 1:
            parent = current // 2
            if parent > 0 and self.data[current] < self.data[parent]:
                self.data[current], self.data[parent] = self.data[parent], self.data[current]
                current = parent
            else:
                break
        return current

    def heapify(self):
        # start at index at length/2

        start = len(self) // 2

        for i in range(start, 0, -1):
            self._siftdown(i)

    def insert(self, key):
        self.data.append(key)

        self._siftup(len(self))

    def pop(self):
        if len(self) < 1:
            return None

        self.data[1], self.data[len(self)] = self.data[len(self)], self.data[1]

        popped = self.data.pop()

        self._siftdown(1)

        return popped


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= K:
            return points

        heap = MinHeap()
        for item in points:
            point = Point(item)
            heap.insert(point)

        k_heap = MinHeap()
        root = heap.data[1]
        root.index = 1
        k_heap.insert(root)
        result = []

        count = K
        while count:
            count -= 1
            current = k_heap.pop()

            left = current.index * 2
            right = current.index * 2 + 1

            if left <= len(heap):
                lnode = heap.data[left]
                lnode.index = left
                k_heap.insert(lnode)
            if right <= len(heap):
                rnode = heap.data[right]
                rnode.index = right
                k_heap.insert(rnode)
            result.append(current.ords)

        return result
