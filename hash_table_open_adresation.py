import random


class HashTable:

    def __init__(self, entry_number):
        self.entry_number = entry_number
        self.table = [None] * self.entry_number

    def calculate_hash(self, element):
        return element % self.entry_number

    def add(self, element):
        """
        1 - calculate hash and set probe to 0
        2 - if the entry is empty -> add element with its probe
        3 - go to the next entry until the entry is empty -> add element with its probe
        4 - if hash_value + probation more than length of table -> nullify hash
        5 - when probe grown more than length of table -> element can't be added
        :param element:
        :return:
        """
        probe = 0
        hash_value = self.calculate_hash(element)
        if self.table[hash_value] is None:
            self.table[hash_value] = [element, probe]
        else:
            while self.table[hash_value] is not None:
                probe += 1
                if hash_value < self.entry_number - 1:
                    hash_value += 1
                else:
                    hash_value = 0
                if probe >= self.entry_number:
                    print('No place in hash table for: ', element)
                    return
            self.table[hash_value] = [element, probe]

    def add_ordered(self, element):
        """
        1 - calculate hash and set probe to 0
        2 - if the entry is empty -> add element with its probe
        3 - if element less than existed element -> add element and rehash existed
        4 - if vice versa -> go to the next entry (quadratic probation)
        5-  check if hash_value is always less than length of table
        6 - if hash_value + probation more than length of table -> nullify hash
        7 - when probe grown more than length of table -> element can't be added
        :param element:
        :return:
        """
        probe = 0
        hash_value = self.calculate_hash(element)
        if self.table[hash_value] is None:
            self.table[hash_value] = [element, probe]
        else:
            if element < self.table[hash_value][0]:
                tmp = self.table[hash_value][0]
                self.table[hash_value] = [element, probe]
                self.add_ordered(tmp)
            else:  # element >= self.table[hash_value]
                increment = 0
                while self.table[hash_value] is not None:
                    probe += 1
                    if hash_value < self.entry_number - 1:
                        increment += 1
                        hash_value += increment ** 2
                    if probe >= self.entry_number:
                        print('No place in hash table for: ', element)
                        return
                    if hash_value > self.entry_number - 1:
                        hash_value = 0
                self.table[hash_value] = [element, probe]

    def show(self):
        for k in range(self.entry_number):
            print(self.table[k], sep=' | ')

    def show_statistic(self):
        sum_probe = 0
        for i in range(self.entry_number):
            if self.table[i] is not None:
                sum_probe += self.table[i][1]
        avg_probe = sum_probe / self.entry_number
        print(avg_probe)


def get_random_list(length, min_value, max_value):
    random_list = [0]*length
    for i in range(length):
        random_list[i] = random.randint(min_value, max_value)
    return random_list


table = HashTable(101)
for element in get_random_list(101, 1, 3000):
    table.add_ordered(element)
table.show()
table.show_statistic()
