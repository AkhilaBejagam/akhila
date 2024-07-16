
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

# Define directories
train_dir = '/home/akhila-bejagam/Pictures/training/'
val_dir = '/home/akhila-bejagam/Pictures/validation/'
test_dir = '/home/akhila-bejagam/Pictures/testing/'

# Load images
train_images = [os.path.join(train_dir, img) for img in os.listdir(train_dir)]
val_images = [os.path.join(val_dir, img) for img in os.listdir(val_dir)]
test_images = [os.path.join(test_dir, img) for img in os.listdir(test_dir)]

# Define transformations
transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
])

# Create data loaders
train_loader = DataLoader([transform(Image.open(img)) for img in train_images], batch_size=32, shuffle=True)
val_loader = DataLoader([transform(Image.open(img)) for img in val_images], batch_size=32, shuffle=False)
test_loader = DataLoader([transform(Image.open(img)) for img in test_images], batch_size=32, shuffle=False)

# Define the model
model = nn.Sequential(
    nn.Linear(784, 128),
    nn.ReLU(),
    nn.Linear(128, 2)
)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(10):
    running_loss = 0.0
    correct = 0
    total = 0
    for inputs in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs.view(-1, 784))
        labels = torch.tensor([0] * outputs.size(0))  # Replace with actual labels
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    train_accuracy = correct / total
    print(f"Epoch [{epoch+1}/10],Train Accuracy: {train_accuracy:.4f}, Train Loss: {running_loss/len(train_loader):.4f}")

    # Validation
    if epoch == 9:  # Print validation results only after the last epoch
        val_correct = 0
        val_total = 0
        val_running_loss = 0.0
        with torch.no_grad():
            for val_inputs in val_loader:
                val_outputs = model(val_inputs.view(-1, 784))
                val_labels = torch.tensor([0] * val_outputs.size(0))  # Replace with actual labels
                _, val_predicted = torch.max(val_outputs.data, 1)
                val_total += val_labels.size(0)
                val_correct += (val_predicted == val_labels).sum().item()
                val_loss = criterion(val_outputs, val_labels)
                val_running_loss += val_loss.item()
        val_accuracy = val_correct / val_total
        print(f"Validation Accuracy: {val_accuracy:.4f}, Validation Loss: {val_running_loss/len(val_loader):.4f}")

# Test the model
test_correct = 0
test_total = 0
test_running_loss = 0.0
with torch.no_grad():
    for inputs in test_loader:
        outputs = model(inputs.view(-1, 784))
        labels = torch.tensor([0] * outputs.size(0))  # Replace with actual labels
        _, predicted = torch.max(outputs.data, 1)
        test_total += labels.size(0)
        test_correct += (predicted == labels).sum().item()
        test_loss = criterion(outputs, labels)
        test_running_loss += test_loss.item()
test_accuracy = test_correct / test_total
print(f"Test Accuracy: {test_accuracy:.4f}, Test Loss: {test_running_loss/len(test_loader):.4f}")
