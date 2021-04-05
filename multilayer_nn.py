import numpy as np

inputs = [
    [-1.3,2.2,3.1,2.4],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,0.8]
]

weights = [
    [0.2,0.1,0.3,0.13],
    [0.33,0.22,0.11,0.44],
    [0.42,0.56,0.54,0.76]
] 
biases = [2,3,0.5]

weights2 = [
    [0.4,0.5,0.3],
    [0.23,0.2,0.01],
    [0.62,0.54,0.59]
]
biases2 = [1,2,-0.5]



layer1_output = np.dot(inputs,np.array(weights).T)+biases
layer2_output = np.dot(layer1_output,np.array(weights2).T)+biases2
print(layer2_output)