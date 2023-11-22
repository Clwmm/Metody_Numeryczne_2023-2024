import numpy as np
import matplotlib.pyplot as plt
import time


def numpy_library_time(n, b):
    matrixA = np.ones((n, n)) + 11 * np.eye(n) + 7 * np.eye(n, k=1)

    start = time.time()
    np.linalg.solve(matrixA, b)
    end = time.time()

    return end - start


def sherman_algorithm(n, b, print_y=False):
    matrixA = [[11] * n, [7] * (n - 1) + [0]]

    start = time.time()

    z = [0] * n
    x = [0] * n
    z[n - 1] = b[n - 1] / matrixA[0][n - 1]
    x[n - 1] = 1 / matrixA[0][n - 1]

    for i in range(n - 2, -1, -1):
        z[i] = (b[n - 2] - matrixA[1][i] * z[i + 1]) / matrixA[0][i]
        x[i] = (1 - matrixA[1][i] * x[i + 1]) / matrixA[0][i]

    delta = sum(z) / (1 + sum(x))

    y = [z[i] - x[i] * delta for i in range(len(z))]

    end = time.time() - start

    if not print_y:
        print(y)
    else:
        return end

def print_result():
    n = 80
    b = [5] * n
    sherman_algorithm(n, b)
def compare_timings(n_values_, no_samples):
    numpy_time = [0] * len(n_values_)
    sherman_time = [0] * len(n_values_)

    for i in range(len(n_values_)):
        for sample in range(no_samples):
            n = n_values_[i]
            b = [5] * n
            numpy_time[i] = numpy_library_time(n, b)
            sherman_time[i] = sherman_algorithm(n, b, True)
        numpy_time[i] /= no_samples
        sherman_time[i] /= no_samples

    plt.grid(True)
    plt.title('Program Execution Time')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.yscale('log')

    plt.plot(n_values_, numpy_time)
    plt.plot(n_values_, sherman_time)
    plt.legend(['Numpy Library Time', 'Implemented Algorithm Time'])
    plt.show()


if __name__ == "__main__":
    print_result()

    n_values = list(range(80, 10000, 200))
    compare_timings(n_values, 10)

