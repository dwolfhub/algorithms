class BinarySearch(object):
    """
    holds an ordered list and provides a method
    to determine if an input is in the list
    """

    def __init__(self, list):
        self.list = list
        self.list_len = len(list)

    def in_list(self, item):
        """
        accepts an argument and determines if the item in in the ordered list
        """
        guesses = 0
        min_index = 0
        max_index = self.list_len - 1

        while min_index <= max_index:
            guess = int((min_index + max_index) / 2)
            guesses += 1

            if self.list[guess] == item:
                return True, guesses
            elif self.list[guess] < item:
                min_index = guess + 1
            else:
                max_index = guess - 1

        return False, guesses


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                 61, 67, 71, 73, 79, 83, 89, 97]

ol = BinarySearch(prime_numbers)

print ol.in_list(1)
print ol.in_list(12)
print ol.in_list(61)
print ol.in_list(11)
print ol.in_list(100)
print ol.in_list(10000)
