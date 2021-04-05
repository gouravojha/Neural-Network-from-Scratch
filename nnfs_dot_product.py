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


output = np.dot(inputs,np.array(weights).T)+biases
print(output)