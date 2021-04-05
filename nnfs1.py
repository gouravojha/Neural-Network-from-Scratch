inputs = [-1.3,2.2,3.1,2.4]

weights = [[
    0.2,0.1,0.3,0.13,
    0.33,0.22,0.11,0.44,
    0.42,0.56,0.54,0.76
]] 

biases = [2,3,0.5]

layers_out = []
for n_weights,n_bias in zip(weights,biases):
    neuron_out = 0
    for n_input,weight in zip(inputs,n_weights):
        neuron_out += n_input*weight
    neuron_out += n_bias
    layers_out.append(neuron_out)
print(layers_out)         