from src.calc_array import calc_array
from src.display_result import display_result


def calc_all(polys: list[list[float]]) -> int:
    ys = []
    result = [1 for i in range(1001)]

    for poly in polys:
        ys.append(calc_array(poly))
    for i in range(0, len(ys), 2):
        for j in range(len(ys[i])):
            result[j] *= ys[i][j] / ys[i + 1][j]
    return display_result([i / 1000 for i in range(1001)], result)
