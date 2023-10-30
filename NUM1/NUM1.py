# Mateusz Kalwa
import sys
import numpy as np
import matplotlib.pyplot as plt


# Determination of the function given in the task
def my_fun(point_x, v_system):
    return v_system(np.sin(v_system(point_x) ** v_system(2)))


# Determine the derivative of the function given in the task
def exact_my_fun_derivative(point_x, v_system):
    return v_system(2) * v_system(point_x) * v_system(np.cos(point_x ** 2))


def my_fun_2(point_x, v_system):
    return v_system(np.cos(v_system(2) * (v_system(point_x) ** v_system(2))))


def exact_my_fun_derivative_2(point_x, v_system):
    return v_system(-4) * v_system(point_x) * v_system(np.sin(v_system(2) * (v_system(point_x) ** v_system(2))))


# Determination of the forward derivative from subsection a. in the task
def forward_derivative(point_x, h, function, v_system):
    return v_system((function(point_x + h, v_system) - function(point_x, v_system)) / h)


# Determine the central derivative from subsection b. in the task
def central_derivative(point_x, h, function, v_system):
    return v_system((function(point_x + h, v_system) - function(point_x - h, v_system)) / (2 * h))


# Function that calculates the absolute value of the difference of the exact derivative from the absolute value
# approximation formula
# The values of the number h are stored in the array h_values_
# Function returns arrays with an error values
def calculate_error(point_x, h_values_, exact_derivative, other_derivative, function, v_system):
    return [np.absolute(other_derivative(point_x, h_, function, v_system) - exact_derivative(point_x, v_system)) for h_
            in h_values_]


# The function that generates the graph
def create_plot_graph(h_values_, errors_forward_derivative_, errors_central_derivative_, variable, used_function_name):
    plt.grid(True)
    if used_function_name == "1":
        plt.title("f(x) = sin(x^2)")
    if used_function_name == "2":
        plt.title("f(x) = cos(2x^2)")
    plt.xlabel('h')
    plt.ylabel("Error")
    plt.loglog(h_values_, errors_forward_derivative_, label='Forward derivative error for: ' + variable)
    plt.loglog(h_values_, errors_central_derivative_, label='Central derivative error for ' + variable)
    plt.legend()
    plt.show()


# MAIN PROGRAM #

# Terms of the program arguments
if len(sys.argv) != 3:
    print("Invalid arguments")
    exit(0)

if sys.argv[1] == "float":
    system = np.float32
    h_start = -7

elif sys.argv[1] == "double":
    system = np.float64
    h_start = -16

else:
    print("Invalid arguments")
    exit(0)

if sys.argv[2] == "1":
    used_function = my_fun
    used_exact_derivative = exact_my_fun_derivative

elif sys.argv[2] == "2":
    used_function = my_fun_2
    used_exact_derivative = exact_my_fun_derivative_2

else:
    print("Invalid arguments")
    exit(0)

# Determining the point given in the task
x = system(0.2)
h_numbers = 250

# Creation of an array of h numbers according to the selected variable
h_values = np.logspace(h_start, 0, h_numbers, dtype=system)

# Calculating the error values table of the approximation function
errors_central_derivative = calculate_error(x, h_values, used_exact_derivative, central_derivative, used_function, system)
errors_forward_derivative = calculate_error(x, h_values, used_exact_derivative, forward_derivative, used_function, system)

# Create a graph from previously created errors values
create_plot_graph(h_values, errors_forward_derivative, errors_central_derivative, sys.argv[1], sys.argv[2])
