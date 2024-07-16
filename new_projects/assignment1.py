# 1st project
import os
import numpy as np
from PIL import Image

# Training
training_data = []
training_labels = []
for filename in os.listdir('/home/akhila-bejagam/Pictures/training/'):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img = Image.open(os.path.join('/home/akhila-bejagam/Pictures/training/', filename))
        img = img.convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28 pixels
        img_array = np.array(img)
        training_data.append(img_array.flatten())
        training_labels.append(1)  # Example label, adjust based on your dataset

# Initialize weights and bias
weights = np.zeros(len(training_data[0]))
#print(weights)
bias = 0.1

# Train the model
training_accuracy = []
for epoch in range(100):  # adjust the number of epochs as needed
    correct = 0
    for i in range(len(training_data)):
        prediction = np.dot(weights, training_data[i]) + bias
        prediction = 1 if prediction >= 0 else 0
        error = training_labels[i] - prediction
        weights += 0.01 * error * training_data[i]
        bias += 0.01 * error
        correct += 1 if prediction == training_labels[i] else 0
    training_accuracy.append(correct / len(training_data))
    print(f"Epoch {epoch+1}, Training Accuracy: {training_accuracy[-1]:.2f}")

# Validation
validation_data = []
validation_labels = []
for filename in os.listdir('/home/akhila-bejagam/Pictures/validation/'):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img = Image.open(os.path.join('/home/akhila-bejagam/Pictures/validation/', filename))
        img = img.convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28 pixels
        img_array = np.array(img)
        validation_data.append(img_array.flatten())
        validation_labels.append(1)  # Example label, adjust based on your dataset

# Evaluate the model on the validation data
predictions = []
for i in range(len(validation_data)):
    prediction = np.dot(weights, validation_data[i]) + bias
    prediction = 1 if prediction >= 0 else 0
    predictions.append(prediction)
accuracy = np.mean(predictions == validation_labels)
print(f"Validation Accuracy: {accuracy:.2f}")

# Testing
testing_data = []
testing_labels = []
for filename in os.listdir('/home/akhila-bejagam/Pictures/testing/'):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img = Image.open(os.path.join('/home/akhila-bejagam/Pictures/testing/', filename))
        img = img.convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28 pixels
        img_array = np.array(img)
        testing_data.append(img_array.flatten())
        testing_labels.append(1)  # Example label, adjust based on your dataset

# Evaluate the model on the testing data
predictions = []
for i in range(len(testing_data)):
    prediction = np.dot(weights, testing_data[i]) + bias
    prediction = 1 if prediction >= 0 else 0
    predictions.append(prediction)
accuracy = np.mean(predictions == testing_labels)
print(f"Testing Accuracy: {accuracy:.2f}")
