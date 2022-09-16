import sys
from copy import deepcopy

def p(*s):
    return
    print(*s, sep='\n', end='\n_________\n')


def place_figure(f1, f2, xp, yp):
    """ sums two matrices and returns the sum IF no collisions, otherwise returns None
        xp, yp are horizontal and vertical shifts >=0. If f2 doesn't fit into f1 with these shifts,
        then returns None as well, because we should stop shifting earlier"""

    f = deepcopy(f1)

    for j in range(len(f2)):
        for i in range(len(f2[j])):
            if 0 <= j + yp < len(f1) and 0 <= i + xp < len(f1[i]):
                f[j + yp][i + xp] += f2[j][i]
                if f[j + yp][i + xp] > 1:
                    return None
            else:
                return None
    return f

def check_pos(f1, f2, xp):
    """ check if after falling down in pos xp one row is filled
    True <=> one row is filled"""
    yp = 0
    t = []
    while r := place_figure(f1, f2, xp, yp):
        t = r
        p(*t)
        yp += 1
    p(*[(sum(t[j]) == len(t[j])) for j in range(len(t))])
    p(any([sum(t[j]) == len(t[j]) for j in range(len(t))]))
    return any([sum(t[j]) == len(t[j]) for j in range(len(t))])

def solution(field, figure):
    for xp in range(len(field[0]) + 1 - len(figure[0])):
        if check_pos(field, figure, xp):
            return xp
    else:
        return -1




import unittest


class TestCase1(unittest.TestCase):
    def test1(self):
        field = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [1, 0, 0],
                 [1, 1, 0]]
        figure = [[0, 0, 1],
                  [0, 1, 1],
                  [0, 0, 1]]

        self.assertEqual(solution(field, figure), 0)

    def test2(self):
        field = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 0],
                 [1, 0, 1, 0, 1]]
        figure = [[1, 1, 1],
                  [1, 0, 1],
                  [1, 0, 1]]

        self.assertEqual(solution(field, figure), 2)

    def test3(self):
        field = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 1],
                 [1, 1, 0, 1]]
        figure = [[1, 1, 0],
                  [1, 0, 0],
                  [1, 0, 0]]

        self.assertEqual(solution(field, figure), -1)

    def test4(self):
        field = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1],
                 [1, 1, 0, 1, 1]]
        figure = [[1, 0, 0],
                  [1, 0, 0],
                  [1, 0, 0]]

        self.assertEqual(solution(field, figure), 0)

    def test5(self):
        field = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 0],
                 [1, 1, 1, 1, 0, 1],
                 [1, 1, 0, 1, 0, 0],
                 [1, 1, 1, 1, 0, 1],
                 [1, 0, 1, 1, 0, 0]]
        figure = [[1, 1, 1],
                  [1, 0, 1],
                  [1, 0, 1]]

        self.assertEqual(solution(field, figure), 3)

    def test6(self):
        field = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1]]
        figure = [[1, 1, 1],
                  [0, 1, 0],
                  [0, 1, 0]]

        self.assertEqual(solution(field, figure), -1)

    def test7(self):
        field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                 [1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
                 [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]
        figure = [[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 1]]

        self.assertEqual(solution(field, figure), 7)

    def test8(self):
        field = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 0, 0, 1],
                 [1, 1, 1, 0, 1, 1, 1, 1]]
        figure = [[0, 0, 0],
                  [1, 1, 0],
                  [1, 1, 0]]

        self.assertEqual(solution(field, figure), -1)



if __name__ == '__main__':
    unittest.main()
