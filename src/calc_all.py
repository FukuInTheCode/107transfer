from src.calc_array import calc_array
from src.display_result import display_result


def calc_all(polys: List[list[float]]) -> int:
    ys = []
    for poly in polys:
        ys.append(calc_array(poly))
    return display_result([[i / 1000 for i in range(1001)], ys])
