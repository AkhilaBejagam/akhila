import os
import numpy as np
from PIL import Image

# Define paths to your data folders
training_dir = '/home/akhila-bejagam/Pictures/training'
validation_dir = '/home/akhila-bejagam/Pictures/validation'
testing_dir = '/home/akhila-bejagam/Pictures/testing'

# Hyperparameters
epochs = 5
learning_rate = 0.01

# Load and preprocess training, validation, and testing data
training_data = []
training_labels = []
for filename in os.listdir(training_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(training_dir, filename)
        img = Image.open(img_path)
        img = img.convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28 pixels
        img_array = np.array(img)
        training_data.append(img_array.flatten())
        training_labels.append(1)  # Example label, adjust based on your dataset

validation_data = []
validation_labels = []
for filename in os.listdir(validation_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(validation_dir, filename)
        img = Image.open(img_path)
        img = img.convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28 pixels
        img_array = np.array(img)
        validation_data.append(img_array.flatten())
        validation_labels.append(1)  # Example label, adjust based on your dataset

testing_data = []
testing_labels = []
for filename in os.listdir(testing_dir):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img_path = os.path.join(testing_dir, filename)
        img = Image.open(img_path)
        img = img.convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28 pixels
        img_array = np.array(img)
        testing_data.append(img_array.flatten())
        testing_labels.append(1)  # Example label, adjust based on your dataset

# SGD Training
weights_sgd = np.random.randn(len(training_data[0]))
bias_sgd = 0.1
training_accuracy_sgd = []
for epoch in range(epochs):
    correct = 0
    for i in range(len(training_data)):
        prediction = np.dot(weights_sgd, training_data[i]) + bias_sgd
        prediction = 1 if prediction >= 0 else 0
        error = training_labels[i] - prediction
        weights_sgd += learning_rate * error * training_data[i]
        bias_sgd += learning_rate * error
        correct += 1 if prediction == training_labels[i] else 0
    training_accuracy_sgd.append(correct / len(training_data))
    print(f"Epoch {epoch+1}, SGD Training Accuracy: {training_accuracy_sgd[-1]:.2f}")

# Evaluate on validation data with SGD
predicted_labels = (np.dot(np.expand_dims(weights_sgd, axis=0), np.transpose(validation_data)) + bias_sgd) >= 0
predicted_labels = predicted_labels.astype(int)
validation_accuracy_sgd = np.mean(predicted_labels == validation_labels)

print(f"SGD Validation Accuracy: {validation_accuracy_sgd:.2f}")

# Evaluate on testing data with SGD
predicted_labels = (np.dot(np.expand_dims(weights_sgd, axis=0), np.transpose(testing_data)) + bias_sgd) >= 0
testing_accuracy_sgd = np.mean(np.all(predicted_labels == testing_labels, axis=1))


print(f"SGD Testing Accuracy: {testing_accuracy_sgd:.2f}")

# Mini-Batch Gradient Descent (MBGD) Training
weights_mbgd = np.random.randn(len(training_data[0]))
bias_mbgd = 0.1
training_accuracy_mbgd = []
for epoch in range(epochs):
    correct = 0
    for i in range(0, len(training_data), 32):  # Batch size of 32
        batch_data = training_data[i:i+32]
        batch_labels = training_labels[i:i+32]
        for j in range(len(batch_data)):
            prediction = np.dot(weights_mbgd, batch_data[j]) + bias_mbgd
            prediction = 1 if prediction >= 0 else 0
            error = batch_labels[j] - prediction
            weights_mbgd += learning_rate * error * batch_data[j]
            bias_mbgd += learning_rate * error
            correct += 1 if prediction == batch_labels[j] else 0
    training_accuracy_mbgd.append(correct / len(training_data))
    print(f"Epoch {epoch+1}, MBGD Training Accuracy: {training_accuracy_mbgd[-1]:.2f}")

# Evaluate on validation data with MBGD
predicted_labels = (np.dot(np.expand_dims(weights_mbgd, axis=0), np.transpose(validation_data)) + bias_mbgd) >= 0
validation_accuracy_mbgd = np.mean(np.all(predicted_labels == validation_labels, axis=1))
print(f"MBGD Validation Accuracy: {validation_accuracy_mbgd:.2f}")

# Evaluate on testing data with MBGD

predicted_labels = (np.dot(np.expand_dims(weights_mbgd, axis=0), np.transpose(testing_data)) + bias_mbgd) >= 0
testing_accuracy_mbgd = np.mean(np.all(predicted_labels == testing_labels, axis=1))



print(f"MBGD Testing Accuracy: {testing_accuracy_mbgd:.2f}")

# Gradient Descent (GD) Training
weights_gd = np.random.randn(len(training_data[0]))
bias_gd = 0.1
training_accuracy_gd = []
for epoch in range(epochs):
    correct = 0
    for i in range(len(training_data)):
        prediction = np.dot(weights_gd, training_data[i]) + bias_gd
        prediction = 1 if prediction >= 0 else 0
        error = training_labels[i] - prediction
        weights_gd += learning_rate * error * training_data[i]
        bias_gd += learning_rate * error
        correct += 1 if prediction == training_labels[i] else 0
    training_accuracy_gd.append(correct / len(training_data))
    print(f"Epoch {epoch+1}, GD Training Accuracy: {training_accuracy_gd[-1]:.2f}")

#Evaluate on validation data with GD
predicted_labels = (np.dot(np.expand_dims(weights_gd, axis=0), np.transpose(validation_data)) + bias_gd) >= 0
validation_accuracy_GD = np.mean(np.all(predicted_labels == validation_labels, axis=1))
print(f"GD Validation Accuracy: {validation_accuracy_mbgd:.2f}")

# Evaluate on testing data with GD

predicted_labels = (np.dot(np.expand_dims(weights_gd, axis=0), np.transpose(testing_data)) + bias_gd) >= 0
testing_accuracy_GD = np.mean(np.all(predicted_labels == testing_labels, axis=1))


