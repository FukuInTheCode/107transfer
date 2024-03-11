#!/usr/bin/python3


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def arg_array(arg: str) -> list[float]:
    result = []
    for num in arg.split("*"):
        if is_float(num):
            result.append(float(num))
        else:
            exit(84)
    return result


def args_array(args: list[str]) -> list[list[float]]:
    all_list = []
    for arg in args:
        all_list.append(arg_array(arg))
    return all_list


def argv_to_array(argv: list[str]) -> int:
    result = args_array(argv)
    return 0
