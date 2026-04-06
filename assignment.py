import numpy as np
import matplotlib.pyplot as plt

def create_array():
    return np.arange(1, 11)

def array_arithmetic(a, b):
    return np.add(a, b)

def slicing_example(arr):
    return arr[:5]

def matrix_multiplication(a, b):
    return np.matmul(a, b)

def random_numbers():
    return np.random.rand(5)

def plot_graph():
    x = np.arange(0, 11)
    y = x**2
    plt.plot(x, y)
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
