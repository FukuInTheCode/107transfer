#!/usr/bin/python3

from src.argv_to_arrays import argv_to_array


def check_error(argv: list[str]) -> int:
    if len(argv) == 0 or len(argv) % 2 != 0:
        exit(84)
    argv_to_array(argv)
    return 0
