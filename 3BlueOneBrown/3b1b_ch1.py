#Code for the 3Blue1Brown video "Vectors" in the LearningCV series
#This code is part of the LearningCV project, which aims to teach computer vision concepts using Python and NumPy.

import numpy as np 

#To a cs student a vector is a list of numbers, but in the context of computer vision, a vector is often a point in space.
#For example, a 2D vector can represent a point in a 2D plane, while a 3D vector can represent a point in 3D space.

#Let's create a 2D vector and a 3D vector using NumPy arrays:
vector_2d = np.array([3, 4])  # A 2D vector
vector_3d = np.array([1, 2, 3])  # A 3D vector

#We can visualize these vectors as arrows in their respective spaces.
#To visualize the 2D vector, we can use matplotlib:
import matplotlib.pyplot as plt
def plot_vector_2d(vector):
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid()
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.title('2D Vector Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

plot_vector_2d(vector_2d)

#Vectors can also be in higher dimensions, such as 3d
def plot_vector_3d(vector):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b')
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.title('3D Vector Visualization')
    plt.show()

plot_vector_3d(vector_3d)

#To add vectors, we can simply use the `+` operator in NumPy:
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
vector_sum = vector_a + vector_b
print(f'Sum of vectors a and b: {vector_sum}')  # Output: [5 7 9]

#To subtract vectors, we can use the `-` operator:
vector_difference = vector_b - vector_a
print(f'Difference of vectors b and a: {vector_difference}')  # Output: [3 3 3]

#To scale a vector by a scalar, we can multiply the vector by the scalar:
scalar = 2
scaled_vector = scalar * vector_a
print(f'Scaled vector a by {scalar}: {scaled_vector}')  # Output: [2 4 6]

#To compute the dot product of two vectors, we can use the `np.dot` function:
dot_product = np.dot(vector_a, vector_b)
print(f'Dot product of vectors a and b: {dot_product}')  # Output: 32

#Remember that the dot product is a measure of how much one vector extends in the direction of another.
#It can also be interpreted as the cosine of the angle between the two vectors multiplied by their magnitudes.
#To compute the magnitude (or length) of a vector, we can use the `np.linalg.norm` function:
magnitude_a = np.linalg.norm(vector_a)
print(f'Magnitude of vector a: {magnitude_a}')  # Output: 3.7416573867739413

#To compute the angle between two vectors, we can use the dot product and magnitudes:
# This is based on the formula: cos(theta) = (a . b) / (||a|| * ||b||)
angle_radians = np.arccos(dot_product / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b)))
angle_degrees = np.degrees(angle_radians)
print(f'Angle between vectors a and b: {angle_degrees} degrees')  # Output: 0.0 degrees since they are parallel

