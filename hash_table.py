from linked_list import LinkedList, Iterator
import random


class HashTable:

    def __init__(self, entry_number):
        self.entry_number = entry_number
        self.table = [LinkedList() for _ in range(self.entry_number)]

    def calculate_hash(self, element):
        return element % self.entry_number

    def add(self, element):
        hash_value = self.calculate_hash(element)
        self.table[hash_value].add_right(element)
        return self.table[hash_value].size

    def add_sorted(self, element):
        hash_value = self.calculate_hash(element)
        iterator = Iterator(self.table[hash_value])

        if self.table[hash_value].is_empty():
            return self.add(element)
        else:
            while iterator.has_next():
                if iterator.next() > element:
                    pos = iterator.get_position() - 1
                    self.table[hash_value].insert(pos, element)
                    return pos
            return self.add(element)

    def search(self, element):
        hash_value = self.calculate_hash(element)
        return self.table[hash_value].search(element)

    def search_in_sorted(self, element):
        hash_value = self.calculate_hash(element)
        return self.table[hash_value].search_sorted(element)

    def show(self):
        for k in range(self.entry_number):
            self.table[k].print_llist()
    
    def get_avg_sequence_length(self):
        sum_sequence_length = 0
        for i in range(self.entry_number):
            sum_sequence_length += self.table[i].size
        return sum_sequence_length / self.entry_number


def get_random_list(length, min_value, max_value):
    random_list = [0]*length
    for i in range(length):
        random_list[i] = random.randint(min_value, max_value)
    return random_list


table = HashTable(10)
probe_sum = 0
for i in get_random_list(300, 1, 3000):
    probe_sum += table.add_sorted(i)
table.show()
avg_probe = probe_sum / 300
print(avg_probe)



