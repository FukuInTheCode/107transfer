import sys
import numpy as np
import matplotlib.pyplot as plt

def calculate_polynomial(coefs, x):
    """
    Calculate the value of a polynomial given its coefficients and x.
    """
    degree = len(coefs) - 1
    result = 0
    for i in range(degree + 1):
        result += coefs[i] * (x ** (degree - i))
    return result

def main():
    if len(sys.argv) < 2:
        print("USAGE: ./107transfer [num den]+")
        sys.exit(0)

    for arg in sys.argv[1:]:
        try:
            arg = list(map(float, arg.split("*")))
        except:
            sys.exit(84)
        x_values = np.linspace(-10, 10, 1000)

        y_values = [calculate_polynomial(arg[::-1], x) for x in x_values]

        plt.plot(x_values, y_values)
        plt.title('Plot of the Polynomial Function')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

