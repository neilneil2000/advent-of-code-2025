import pytest
from day9 import lines_cross, is_point_internal_to_polygon

a = ((0, 0), (0, 4))
b = ((2, 0), (2, 4))
c = ((4, 0), (4, 4))
d = ((2, 5), (2, 8))
e = ((4, 5), (4, 8))
f = ((0, 4), (4, 4))
g = ((0, 2), (4, 2))
h = ((0, 0), (4, 0))
i = ((5, 4), (8, 4))
j = ((5, 2), (8, 2))

lines_cross_params = [
    (a, b),
    (a, c),
    (a, d),
    (a, e),
    (a, f),
    (a, g),
    (a, h),
    (a, i),
    (a, j),
    (b, c),
    (b, d),
    (b, e),
    (b, f),
    # (b, g),
    (b, h),
    (b, i),
    (b, j),
    (c, d),
    (c, e),
    (c, f),
    (c, g),
    (c, h),
    (c, i),
    (c, j),
    (c, b),
    (c, c),
    (a, d),
    (c, e),
    (c, f),
    (c, g),
    (c, h),
    (c, i),
    (c, j),
    (d, e),
    (d, f),
    (d, g),
    (d, h),
    (d, i),
    (d, j),
    (e, f),
    (e, g),
    (e, h),
    (e, i),
    (e, j),
    (f, g),
    (f, h),
    (f, i),
    (f, j),
    (g, h),
    (g, i),
    (g, j),
    (h, i),
    (h, j),
    (i, j),
]


@pytest.mark.parametrize("x,y", lines_cross_params)
def test_lines_cross_false(x, y):
    assert lines_cross(x, y) == False


def test_lines_cross_true():
    assert lines_cross(b, g) == True


# ............................ (0,0 at top left)
# ......X######X..............
# ......#iiiiii#..............
# .X####XiiiiiiX############X.
# .#iiiiiiiiiiiiiiiiiiiiiiii#.
# .X######XiiiiX#######Xiiii#.
# ........#iiii#.......#iiii#.
# ........#iiii#..X##X.#iiii#.
# .X######Xiiii#..#iiX#Xiiii#.
# .X###########X..X#########X.

lines = [
    ((6, 1), (13, 1)),
    ((13, 1), (13, 3)),
    ((13, 3), (26, 3)),
    ((26, 3), (26, 9)),
    ((26, 9), (16, 9)),
    ((16, 9), (16, 7)),
    ((16, 7), (19, 7)),
    ((19, 7), (19, 8)),
    ((19, 8), (21, 8)),
    ((21, 8), (21, 5)),
    ((21, 5), (13, 5)),
    ((13, 5), (13, 9)),
    ((13, 9), (1, 9)),
    ((1, 9), (1, 8)),
    ((1, 8), (8, 8)),
    ((8, 8), (8, 5)),
    ((8, 5), (1, 5)),
    ((1, 5), (1, 3)),
    ((1, 3), (6, 3)),
    ((6, 3), (6, 1)),
]
external_points = [
    ((1, 1), lines),
    ((20, 1), lines),
    ((1, 6), lines),
    ((2, 7), lines),
    ((14, 6), lines),
    ((15, 6), lines),
    ((21, 6), lines),
    ((20, 7), lines),
]
internal_points = [((7, 2), lines), ((7, 3), lines)]


@pytest.mark.parametrize("point, lines", external_points)
def test_point_internal_false(point, lines):
    assert is_point_internal_to_polygon(point, lines) == False


@pytest.mark.parametrize("point, lines", internal_points)
def test_point_internal_true(point, lines):
    assert is_point_internal_to_polygon(point, lines) == True
