#!/usr/bin/python3

def argv_to_arrays(argv: list[str]) -> list[float]:
    result = []
    for arg in argv:
        if 'x' in arg:
            x_parts = arg.split('*')
            result.extend(map(float, x_parts))
        else:
            result.append(float(arg))
    return result
