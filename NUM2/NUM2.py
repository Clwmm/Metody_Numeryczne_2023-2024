# Mateusz Kalwa
import numpy as np


def printOperation(text, matrix, vector):
    print(text)
    print(np.linalg.solve(matrix, vector))


A1 = np.array([[2.554219275, 0.871733993, 0.052575899, 0.240740262, 0.316022841],
               [0.871733993, 0.553460938, -0.070921727, 0.255463951, 0.707334556],
               [0.052575899, -0.070921727, 3.409888776, 0.293510439, 0.847758171],
               [0.240740262, 0.255463951, 0.293510439, 1.108336850, -0.206925123],
               [0.316022841, 0.707334556, 0.847758171, -0.206925123, 2.374094162]])

A2 = np.array([[2.645152285, 0.544589368, 0.009976745, 0.327869824, 0.424193304],
               [0.544589368, 1.730410927, 0.082334875, -0.057997220, 0.318175706],
               [0.009976745, 0.082334875, 3.429845092, 0.252693077, 0.797083832],
               [0.327869824, -0.057997220, 0.252693077, 1.191822050, -0.103279098],
               [0.424193304, 0.318175706, 0.797083832, -0.103279098, 2.502769647]])

b = np.array([-0.642912346, -1.408195475, 4.595622394, -5.073473196, 2.178020609])

print("Przed zaburzeniem:")
printOperation("A1y = b:", A1, b)
printOperation("\nA2y = b:", A2, b)

# generowanie wektora z 5 losowymi liczbami z przedziału 0 do 1 * 10^-6 do zaburzania wektora b
random_values = np.random.rand(5) * 1e-6

# zaburzenie wektora b
b = b + random_values

print("\n\nPo zaburzeniu:")
printOperation("A1y = b:", A1, b)
printOperation("\nA2y = b:", A2, b)
