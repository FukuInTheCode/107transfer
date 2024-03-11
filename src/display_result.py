#!/usr/bin/python3

def display_result(x: list[float], y: list[float]) -> int:
    for i in range(len(x)):
        print(f"{x[i]:.4f} -> {y[i]:.4f}")
    return 0
