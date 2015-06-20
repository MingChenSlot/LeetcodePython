__author__ = 'mingchen'

# @param num, a list of integer
# @return an integer
def rob(num):
    max_money = list(num)
    for index, item in enumerate(num):
        if index == 0:
            max_money[index] = max_money[0]
        elif index == 1:
            max_money[index] = max(max_money[0], num[1])
        else:
            max_money[index] = max(max_money[index - 2] + num[index],
                               max_money[index - 1])

    return 0 if len(num) == 0 else max_money[len(num) - 1]

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(rob([0]), 0);
        self.assertEqual(rob([3, 1]), 3);
        self.assertEqual(rob([1, 3, 3]), 4);
        self.assertEqual(rob([2, 1, 2, 3, 5]), 9);
        self.assertEqual(rob([2, 6, 2, 2, 5]), 11);



