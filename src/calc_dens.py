from src.calc_array import calc_array


def calc_all_dens(argv: list[list[float]]) -> int:
    dens = []

    for i in range(1, len(argv), 2):
        dens.append(calc_array(argv[i]))
        if 0 in dens[-1]:
            return 84
    return 0
