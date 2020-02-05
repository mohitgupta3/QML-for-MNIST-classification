# QML-for-MNIST-classification
Quantum machine learning implementation for the classification of MNIST dataset.
Simulates 10 Greenberger–Horne–Zeilinger (GHZ) states with QVM noise model.

The model reduces MNIST data to 16 dimensions using PCA, applies reservoir computing to the output, and finally classifies the data using a neural network.
___
## Running the model
First, you need to get an API key for the [rigetti forest API](https://www.rigetti.com/systems). <br>After installing the remaining packages, run

`$ python cca_nn_classifier.py`

This will run the model end to end.
___
> In the area of quantum information theory, a GHZ state is a certain type of entangled <br>quantum state that involves at     least three subsystems (particle states, or qubits).
>
> QVm stands for Quality Virtual machine...
>
> We recoment Ubuntu operating system with python3.5+ installed.

___
## Sample Results:
### visualize digits separable postreservoir 0
![visualize digits separable postreservoir 0](figures/visualize_digits_separable_postreservoir_0.png?raw=true)
___
### visualize digits separable postreservoir 1
![visualize digits separable postreservoir 1](figures/visualize_digits_separable_postreservoir_1.png?raw=true)
___
### visualize digits separable postreservoir 2
![visualize digits separable postreservoir 2](figures/visualize_digits_separable_postreservoir_2.png?raw=true)
___
### Noise model
![Noise_model](figures/NoiseModelPauliChannel_10_qubit_GHZ_state_1000_Trial_Measurements.png?raw=true)
___
### Confusion Matrix
![Confusion matrix](figures/confusion_matrix.png?raw=true)
