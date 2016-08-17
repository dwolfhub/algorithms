

class BinarySearch(object):
    """holds an ordered list and provideds a method to determine if an input is in the list"""

    def __init__(self, list):
        self.list = list
        self.guesses = 0

    def guess_halfway(self, x, min_index, max_index):
        """
        determines the index in between min and max, guesses that,
        then modifies the min and max and calls itself
        """
        self.guesses = self.guesses + 1
        index_to_try = int((min_index + max_index) / 2)

        if index_to_try == min_index:
            return x == self.list[min_index] or x == self.list[max_index]

        if self.list[index_to_try] == x:
            return true
        elif x > self.list[index_to_try]:
            return self.guess_halfway(x, index_to_try + 1, max_index)
        elif x < self.list[index_to_try]:
            return self.guess_halfway(x, min_index, index_to_try - 1)

    def search(self, item):
        self.guesses = 0
        """accepts an argument and determines if the item in in the ordered list"""
        min_index = 0
        max_index = len(self.list) - 1

        return self.guess_halfway(item, min_index, max_index), self.guesses


ol = BinarySearch([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

print ol.search(1)
print ol.search(12)
print ol.search(61)
print ol.search(11)
print ol.search(100)
print ol.search(10000)

