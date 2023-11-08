import sys
import time
import matplotlib.pyplot as plt

def fun_NUM3(n):
    # creating matrix with given numbers
    matrixA = []
    matrixA.append([0] + [0.2] * (n - 1))
    matrixA.append([1.2] * n)
    matrixA.append([0.1 / i for i in range(1, n)] + [0])
    matrixA.append([0.15 / i ** 2 for i in range(1, n - 1)] + [0] + [0])

    # creating a given vector x
    x = list(range(1, n + 1))

    # calculating matrices L, U with storing result in matrix A
    for i in range(1, n - 2):
        matrixA[0][i] = matrixA[0][i] / matrixA[1][i - 1]
        matrixA[1][i] = matrixA[1][i] - matrixA[0][i] * matrixA[2][i - 1]
        matrixA[2][i] = matrixA[2][i] - matrixA[0][i] * matrixA[3][i - 1]

    matrixA[0][n - 2] = matrixA[0][n - 2] / matrixA[1][n - 3]
    matrixA[1][n - 2] = matrixA[1][n - 2] - matrixA[0][n - 2] * matrixA[2][n - 3]
    matrixA[2][n - 2] = matrixA[2][n - 2] - matrixA[0][n - 2] * matrixA[3][n - 3]

    matrixA[0][n - 1] = matrixA[0][n - 1] / matrixA[1][n - 2]
    matrixA[1][n - 1] = matrixA[1][n - 1] - matrixA[0][n - 1] * matrixA[2][n - 2]

    # calculating determinant by multiplying all the numbers on the diagonal
    determinant = 1
    for i in range(n):
        determinant *= matrixA[1][i]

    # calculating vector y with given formula: y = A^-1 x
    # using the LU distribution we can split this into two formulas
    # 1. L z = x
    # 2. U y = z

    # 1.)
    for i in range(1, n):
        x[i] = x[i] - matrixA[0][i] * x[i - 1]

    # 2.)
    x[n - 1] = x[n - 1] / matrixA[1][n - 1]
    x[n - 2] = (x[n - 2] - (matrixA[2][n - 2] * x[n - 1])) / matrixA[1][n - 2]

    for i in range(n - 3, -1, -1):
        x[i] = (x[i] - (matrixA[2][i] * x[i + 1]) - (matrixA[3][i] * x[i + 2])) / matrixA[1][i]

    result = [x, determinant]
    # returning calculated vector y and determinant of matrix A
    return result


def createPlot(n_values_, fun, no_samples):
    execution_time = [0] * len(n_values_)

    for i in range(len(n_values_)):
        for sample in range(no_samples):
            star_time = time.time()
            fun(n_values_[i])
            end_time = time.time()
            fun_time = end_time - star_time
            execution_time[i] += fun_time
        execution_time[i] /= no_samples


    plt.plot(n_values_, execution_time)
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('NUM3')
    plt.grid(True)
    plt.show()


# MAIN PROGRAM #
if len(sys.argv) != 2:
    print("Please enter argument:\n'y' - calculating y vector\n'time' - calculating time of function in range(124,1000)\n'det' - calculating determinant of the matrix A")
    exit(0)

if sys.argv[1] == "y":
    print("Calculated vector y:\n")
    print(fun_NUM3(124)[0])

elif sys.argv[1] == "time":
    n_values = list(range(124, 1000))
    createPlot(n_values, fun_NUM3, 50)

elif sys.argv[1] == "det":
    print("Calculated determinant of the matrix A:\n")
    print(fun_NUM3(124)[1])

else:
    print("Wrong argument:\n'y' - calculating y vector\n'time' - calculating time of function in range(124,1000)\n'det' - calculating determinant of the matrix A")

exit(0)