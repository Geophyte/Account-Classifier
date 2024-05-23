import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import sklearn.metrics as sk_metrics
from typing import Dict, Any


class BinaryClassifier(nn.Module):
    def __init__(self, input_dim: int) -> None:
        super(BinaryClassifier, self).__init__()
        self.layer_1 = nn.Linear(input_dim, 32)
        self.layer_2 = nn.Linear(32, 64)
        self.layer_3 = nn.Linear(64, 32)
        self.output = nn.Linear(32, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        x = self.relu(self.layer_3(x))
        x = self.sigmoid(self.output(x))
        return x


class Trainer:
    def __init__(self, model: nn.Module, criterion: nn.Module, optimizer: optim.Optimizer) -> None:
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer

    def train(self, train_loader: DataLoader, num_epochs: int) -> None:
        for epoch in range(num_epochs):
            self.model.train()
            for data, target in train_loader:
                self.optimizer.zero_grad()
                output = self.model(data)
                loss = self.criterion(output, target)
                loss.backward()
                self.optimizer.step()
            print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')


class Evaluator:
    def __init__(self, model: nn.Module) -> None:
        self.model = model

    def evaluate(self, X: torch.Tensor, y: torch.Tensor) -> Dict[str, Any]:
        self.model.eval()
        with torch.no_grad():
            y_pred = self.model(X).numpy()
            y_true = y.numpy()
            y_pred_label = (y_pred > 0.5).astype(int)

        y_true = y_true.flatten()
        y_pred = y_pred.flatten()
        y_pred_label = y_pred_label.flatten()

        metrics = {
            'accuracy': sk_metrics.accuracy_score(y_true, y_pred_label),
            'roc_auc': sk_metrics.roc_auc_score(y_true, y_pred),
            'precision': sk_metrics.precision_score(y_true, y_pred_label),
            'recall': sk_metrics.recall_score(y_true, y_pred_label),
            'f1': sk_metrics.f1_score(y_true, y_pred_label),
            'confusion_matrix': sk_metrics.confusion_matrix(y_true, y_pred_label)
        }

        return metrics


def create_data_loader(X: torch.Tensor, y: torch.Tensor, batch_size: int) -> DataLoader:
    dataset = TensorDataset(X, y)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return data_loader
