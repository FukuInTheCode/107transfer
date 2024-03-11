#!/usr/bin/python3

def display_result(x: list[float], y: list[float]) -> int:
    for i in range(len(x)):
        print(f"{x[i]:.3f} -> {y[i]:.5f}")
    return 0
