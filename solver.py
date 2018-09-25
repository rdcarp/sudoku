
NUMBER_RANGE = range(1, 10)

class Square:
    def __init__(self):
        self._ruled_out = set()
        self._possibilities = set(NUMBER_RANGE)

    def is_(self, n):
        for i in NUMBER_RANGE:
            if i != n:
                self._ruled_out.add(i)

    def isnt(self, *n):
        for i in n:
            self._ruled_out.add(i)

    @property
    def answer(self):
        if len(self.possibilities) == 1:
            return list(self.possibilities)[0]

        raise Exception()

    @property
    def is_solved(self):
        return len(self.possibilities) == 1

    @property
    def possibilities(self):
        return self._possibilities.difference(self._ruled_out)

    def __str__(self):
        return ",".join([str(x) for x in self.possibilities])

    @property
    def possibilities_as_int(self):
        return sum([2**(i-1) if i not in self._ruled_out else 0 for i in list(self._possibilities)])
     

class Puzzle:
    def __init__(self):
        self._squares = [Square() for i in range(0, 9*9)]

    @property
    def rows(self):
        return [Nine([self._squares[9*r + i] for i in range(0, 9)]) for r in range(0, 9)]
    
    @property
    def columns(self):
        return [Nine([self._squares[9*i + r] for i in range(0, 9)]) for r in range(0, 9)]

    @property
    def grids(self):
        _grid_cells = [
            [0, 1, 2, 9, 10, 11, 18, 19, 20],
            [3, 4, 5, 12, 13, 14, 21, 22, 23],
            [6, 7, 8, 15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]
        ]

        a = []
        for l in _grid_cells:
            a.append(Nine([self._squares[a] for a in l]))

        return a

    def print_as_grid(self):
        for i in range(0, 9):
            print("\t".join([str(self._squares[i*9 + j].possibilities_as_int) for j in range(0, 9)]))

class Nine:
    def __init__(self, squares):
        self._squares = squares

    @property
    def missing(self):
        for s in self._squares:
            print(s)
            print(s.is_solved)
        known = set([s.answer for s in self._squares if s.is_solved])
        return set(NUMBER_RANGE).difference(known)

if __name__ == "__main__":
    p = Puzzle()

    # p.print_as_grid()
    # p._squares[0].isnt(8, 1)
    # print()
    # p.print_as_grid()
    # print()
    # p._squares[1].is_(1)


    # # s = Square()
    # # s.is_(5)
    # squares = [Square() for _ in range(10)]
    # squares[0].is_(3)
    # squares[5].is_(7)
    # n1 = Nine(set(squares[0:8]))
    # n2 = Nine(set(squares[1:9]))
    # print(n1.missing)
    # print(n2.missing)

    print(p.grids)
    g1: Nine = p.grids[0]
    p._squares[4].is_(5)
    for r in p.columns:
        print(r.missing)