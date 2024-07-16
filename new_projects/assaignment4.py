import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from PIL import Image
from torch.utils.data import DataLoader, TensorDataset
import os

# Define paths to datasets
training_path = "/home/akhila-bejagam/Pictures/training"
validation_path = "/home/akhila-bejagam/Pictures/validation"
testing_path = "/home/akhila-bejagam/Pictures/testing"

# Define transforms for preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Paths to datasets
datasets = [
    {'name': 'train', 'path': training_path},
    {'name': 'validation', 'path': validation_path},
    {'name': 'test', 'path': testing_path}
]

# Initialize datasets and dataloaders
data_loaders = {}
for dataset in datasets:
    images = [f for f in os.listdir(dataset['path']) if f.endswith('.jpg') or f.endswith('.png')]
    data = []
    labels = []
    for img_name in images:
        img_path = os.path.join(dataset['path'], img_name)
        image = Image.open(img_path)
        image = transform(image)
        data.append(image)
        labels.append(torch.tensor(0))  # Assuming all labels are 0 for simplicity

    # Convert lists to tensors
    data_tensor = torch.stack(data)
    labels_tensor = torch.tensor(labels)

    # Create TensorDataset and DataLoader
    data_loaders[dataset['name']] = DataLoader(TensorDataset(data_tensor, labels_tensor), batch_size=64, shuffle=dataset['name'] == 'train')

# Neural network model
net = nn.Sequential(
    nn.Linear(224 * 224 * 3, 128),
    nn.ReLU(),
    nn.Dropout(p=0.5),
    nn.Linear(128, 64),
    nn.ReLU(),
    nn.Linear(64, 10)
)

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()

# Regularization techniques
regularization_techniques = ['L1', 'L2', 'Dropout']

for technique in regularization_techniques:
    print(f"Training with {technique} regularization...")
    
    # Reset model parameters and optimizer
    for module in net.modules():
        if isinstance(module, nn.Linear):
            nn.init.xavier_uniform_(module.weight)
            nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Dropout):
            module.p = 0.5
            
    optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

    # Train the network
    num_epochs = 10 # Increase number of epochs
    for epoch in range(num_epochs):
        running_loss = 0.0
        net.train()  # Set the model to train mode
        for dataset_name in ['train']:
            for i, (inputs, labels) in enumerate(data_loaders[dataset_name], 0):
                optimizer.zero_grad()
                inputs = inputs.view(-1, 224 * 224 * 3)
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                
                # Apply regularization for L1 and L2
                if technique == 'L1' or technique == 'L2':
                    l1_lambda = 0.00001  # Adjust regularization strength
                    l2_lambda = 0.0001   # Adjust regularization strength
                    l1_reg = torch.tensor(0., requires_grad=False)
                    l2_reg = torch.tensor(0., requires_grad=False)
                    for param in net.parameters():
                        l1_reg += torch.norm(param, 1)
                        l2_reg += torch.norm(param, 2)
                    loss += l1_lambda * l1_reg + l2_lambda * l2_reg
                
                loss.backward()
                optimizer.step()
                running_loss += loss.item()

        # Calculate training accuracy
        net.eval()  # Set the model to evaluation mode
        correct = 0
        total = 0
        with torch.no_grad():
            for inputs, labels in data_loaders['train']:
                inputs = inputs.view(-1, 224 * 224 * 3)
                outputs = net(inputs)
                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
            train_accuracy = 100 * correct / total

            # Calculate validation accuracy
            correct = 0
            total = 0
            for inputs, labels in data_loaders['validation']:
                inputs = inputs.view(-1, 224 * 224 * 3)
                outputs = net(inputs)
                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
            validation_accuracy = 100 * correct / total

            print(f'Epoch {epoch+1}, Loss: {running_loss / len(data_loaders["train"])}, Train Accuracy: {train_accuracy}%, Validation Accuracy: {validation_accuracy}%')

    # Evaluate on test set
    correct = 0
    total = 0
    net.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        for inputs, labels in data_loaders['test']:
            inputs = inputs.view(-1, 224 * 224 * 3)
            outputs = net(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        test_accuracy = 100 * correct / total
    print(f'Test Accuracy with {technique} regularization: {test_accuracy}%')