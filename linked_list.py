class LinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self.size = 0

    def search(self, element):
        curr = self.end
        while curr is not None:
            if curr[2] == element:
                return True
            curr = curr[1]
        return False

    def search_sorted(self, element):
        curr = self.end
        while curr is not None:
            if curr[2] == element:
                return True
            if curr[2] > element:
                return False
            curr = curr[1]
        return False

    def add_right(self, x):
        if self.begin is None:
            self.begin = [self.begin, self.begin, x]
            self.end = self.begin
            self.size += 1
        else:
            tmp = self.begin
            self.begin = [self.begin, self.begin[1], x]
            tmp[1] = self.begin
            self.size += 1

    def add_left(self, x):
        if self.end is None:
            self.end = [self.end, self.end, x]
            self.begin = self.end
            self.size += 1
        else:
            tmp = self.end
            self.end = [self.end[0], self.end, x]
            tmp[0] = self.end
            self.size += 1

    def insert(self, pos: int, x):
        curr = self.end
        k = 1
        while k != pos and curr is not None:
            curr = curr[1]
            k += 1
        if curr is not None:
            if k == 1:
                self.add_left(x)
            else:
                prev = curr[0]
                prev[1] = [prev, curr, x]
                curr[0] = prev[1]
                self.size += 1

    def is_empty(self):
        return self.begin is None and self.end is None

    def del_right(self):
        if self.begin is not None:
            self.begin[0][1] = self.begin[1]
            self.begin = self.begin[0]
            self.size -= 1

    def del_left(self):
        if self.end is not None:
            self.end[1][0] = self.end[0]
            self.end = self.end[1]
            self.size -= 1

    def print_llist(self):
        p = self.end
        while p is not None:
            print(p[2], end=' -> ')
            p = p[1]
        print('\n')

    def print_reverse_llist(self):
        p = self.begin
        while p is not None:
            print(p[2], end=' -> ')
            p = p[0]
        print('\n')


class Iterator:

    def __init__(self, llist: LinkedList):
        self.it = llist.end
        self.counter = 1

    def get_position(self):
        return self.counter

    def has_next(self):
        return self.it is not None

    def next(self):
        if self.has_next():
            element = self.it[2]
            self.it = self.it[1]
            self.counter += 1
            return element
        return None

