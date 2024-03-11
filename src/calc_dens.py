from src.calc_array import calc_array
from src.calc_all import calc_all


def calc_all_dens(argv: list[list[float]]) -> int:
    dens = []

    for i in range(1, len(argv), 2):
        dens.append(calc_array(argv[i]))
        if 0 in dens[-1]:
            exit(84)
    return calc_all(argv)
