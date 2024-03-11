def calc_value(x: float, poly: list[float]) -> float:
    y = poly[0]
    my_x = x
    for c in poly[1:]:
        y += my_x * c
        my_x *= x
    return y


def calc_array(poly: list[float]) -> list[float]:
    xs = [i / 1000 for i in range(1001)]
    ys = []
    for x in xs:
        ys.append(calc_value(x, poly))
    return ys
