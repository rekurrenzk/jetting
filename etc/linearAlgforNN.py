import numpy as np

A = np.array([
    [-1,3],
    [3,2]
    ], dtype=np.dtype(float))

b = np.array([7,1], dtype=np.dtype(float))

print(f"matrix a is {A}")
print(f"\narray for b is {b}")


print()

print(f"shape of A is {A.shape}")
print(f"shape of b is {b.shape}")

print()

X = np.linalg.solve(A, b)
print(f"solution: {X}")

print()

### CALCULATING THE DETERMINANT ###

d = np.linalg.det(A)
print(f"determinant of matrix A: {d:.2f}")


newly = np.array([[-1,3,7],
                 [3,2,1]])

print("###############" *3)
A_system = np.hstack((newly, b.reshape((2,1))))
print(A_system, "\n")
print(A_system[1])

try:
    x2 = np.linalg.solve(newly, b)
except np.linalg.LinAlgError as err:
    print(err)
