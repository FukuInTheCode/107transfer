#!/usr/bin/python3

from argv_to_array import argv_to_arrays


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_arg(abrs: list[str]) -> int:
    if len(abrs) % 2 != 0:
        exit(84)
    for i in range(0, len(abrs), 2):
        if int(abrs[i + 1]) == 0:
            exit(84)
        if is_float(abrs[i]):
            exit(84)

    return 0
