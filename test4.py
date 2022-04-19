def merge(nums_1, nums_2):
    """
    Merges the numbers in the two lists in-place
    pass nums_1 = [1,3,6,8,9,0,0,0,0] nums_2 = [2,4,5,7]
    merge(nums_1, nums_2) print(nums_1) > [1,2,3,4,5,6,7,8,9]
    """
    new_l = []
    for i in nums_1:
        if i:
            new_l.append(i)
    new_l.extend(nums_2)
    return sorted(new_l)

def reverse(string):
    new_s = ''
    for i in string:
        new_s = i+new_s
    return new_s

from unittest import TestCase
class SimpleTest(TestCase):

    def test_reverse_pass(self):
        expected_output = 'dlroW'
        output = reverse('World')
        self.assertEqual(output, expected_output)

    def test_reverse_fail(self):
        expected_output = 'dlroW'
        output = reverse('Word')
        self.assertNotEqual(output, expected_output)

if __name__ == '__main__':
    x = [1,3,6,8,9,0,0,0,0]
    y = [2,4,5,7]
    print(merge(x, y))
    s = 'Hello World'
    print(reverse(s))