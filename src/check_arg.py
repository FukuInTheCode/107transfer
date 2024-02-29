#!/usr/bin/python3


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_arg(abrs: list[str]) -> int:
    if len(abrs) % 2 != 0:
        exit(84)
    return 0
