# N_parent = (N_child -1) // 2
# N_left = 2*N_parent + 1
# N_right = 2*N_parent + 2


class Heap:
    def __init__(self):
        self.values = []
        self.size = len(self.values)

    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)

    def delete(self, i):
        self.values[i], self.values[-1] = self.values[-1], self.values[i]
        self.values.pop()
        self.size -= 1
        self.sift_up(i)

    def sift_down(self, i):
        while 2*i + 1 < self.size:
            j = i
            if self.values[2*i + 1] < self.values[i]:
                j = 2*i + 1
            if 2*i + 2 < self.size and self.values[2*i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def extract_min(self):
        if self.size == 0:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return tmp

    def extract_max(self):
        if self.size == 0:
            return None
        max = self.values[0]
        max_idx = 0
        for i in range(1, len(self.values)):
            if self.values[i] > max:
                max = self.values[i]
                max_idx = i
        heap.delete(max_idx)
        return max

    def print_heap(self):
        pass


def list_to_heap(a: list):
    heap = Heap()
    for x in a:
        heap.insert(x)
    return heap


def heap_to_sort_list(heap: Heap, asc=True):
    a = []
    if asc:
        while heap.size:
            a.append(heap.extract_min())
        return a
    else:
        while heap.size:
            a.append(heap.extract_max())
        return a


def heap_sort(a: list, asc=True):
    return heap_to_sort_list(list_to_heap(a), asc)


a = [46, 24, 3, 4, 21, 79, 61, 1, 5, 23]
heap = list_to_heap(a)
print(heap.values)
print(heap.extract_max())
print(heap.size, heap.values)