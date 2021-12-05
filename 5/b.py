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
        return self.is_vertical() or self.is_horizontal() or self.is_diagonal()

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_horizontal(self):
        return self.y1 == self.y2

    def is_diagonal(self):
        return abs(self.x1 - self.x2) == abs(self.y1 - self.y2)

    def line_points(self):
        if not self.is_line():
            raise ValueError
        if self.is_horizontal():
            x1, x2 = min(self.x1, self.x2), max(self.x1, self.x2)
            return [(i, self.y1) for i in range(x1, x2 + 1)]
        if self.is_vertical():
            y1, y2 = min(self.y1, self.y2), max(self.y1, self.y2)
            return [(self.x1, i) for i in range(y1, y2 + 1)]
        if self.is_diagonal():
            # 2 cases
            if (self.x2 > self.x1 and self.y2 > self.y1) or (
                self.x1 > self.x2 and self.y1 > self.y2
            ):
                x1, x2 = min(self.x1, self.x2), max(self.x1, self.x2)
                y1, y2 = min(self.y1, self.y2), max(self.y1, self.y2)
                return [(x1 + i, y1 + i) for i in range(y2 - y1 + 1)]
            else:
                x1 = self.x1
                y1 = self.y1
                x2 = self.x2
                y2 = self.y2
                if self.x1 > self.x2:
                    return [(x1 - i, y1 + i) for i in range(y2 - y1 + 1)]
                else:
                    return [(x1 + i, y1 - i) for i in range(y1 - y2 + 1)]


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
