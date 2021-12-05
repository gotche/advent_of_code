import sys
from collections import defaultdict
from dataclasses import dataclass

# read file
data = sys.stdin.readlines()

# clean
@dataclass
class Direction:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_line(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def line_points(self):
        if not self.is_line():
            raise ValueError
        if self.is_horizontal():
            x1, x2 = min(self.x1, self.x2), max(self.x1, self.x2)
            return [(i, self.y1) for i in range(x1, x2 + 1)]
        if self.is_vertical():
            y1, y2 = min(self.y1, self.y2), max(self.y1, self.y2)
            return [(self.x1, i) for i in range(y1, y2 + 1)]


points = []
for line in data:
    a, b = line.split("->")
    x1, y1 = [int(i) for i in a.split(",")]
    x2, y2 = [int(i) for i in b.split(",")]
    points.append(Direction(x1, y1, x2, y2))

# process
grid = defaultdict(int)

for point in points:
    if point.is_line():
        for line_point in point.line_points():
            grid[line_point] += 1

print(sum(1 for value in grid.values() if value > 1))
