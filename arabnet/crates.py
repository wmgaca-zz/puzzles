#!/usr/bin/env python
import math


LIMIT = 25


class Node(object):

    def __init__(self, crates):
        self.crates = crates

    def __str__(self):
        return '[ %s ]' % ' '.join([str(crate) for crate in self.crates])

    @property
    def items(self):
        return sum(map(len, self.crates))

    @property
    def over_limit(self):
        return max(map(sum, self.crates)) > LIMIT

    def spawn(self, element):
        nodes = []
        for i in range(len(self.crates)):
            nodes.append(Node(list([list(crate) for crate in self.crates])))
            nodes[-1].crates[i].append(element)
        return nodes


def dfs(crates, count):
    crates = sorted(crates)[::-1]
    queue = [Node([[] for x in range(count)])]
    
    while True:
        # Get the first one from the list
        current = queue.pop(0)
        # This node is over limit, don't populate further
        if current.over_limit:
            continue
        # Found the solution, yay!
        if current.items == len(crates):
            return current
        # Populate, prepend the list
        queue = current.spawn(crates[current.items]) + queue

        if not len(queue):
            return None


def solve(crates=[1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 8, 8, 9, 10, 12, 13, 16, 17, 18, 19]):
    crates_no = int(math.ceil(sum(crates) / 25.0))

    while True:
        try:
            result = dfs(crates, crates_no)
        except IndexError:
            crates_no += 1
        else:
            print 'Crates => %s' % crates_no
            return result

print solve()

