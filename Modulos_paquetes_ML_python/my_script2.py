import torch
import torch.nn as nn
import torch.optim as optim

# Creamos datos de ejemplo
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]]) # Entrada
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]]) # salida esperada

# Creamos el modelo
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel() 

# imprimir el modelo sin ser entrenado
print("Modelo sin entrenar:")
with torch.no_grad():
    predicted = model(X)
    print(predicted.numpy())

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Entrenamos el modelo
for epoch in range (100):
    model.train()

    outputs = model(X)
    loss = criterion(outputs, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f"Epoch [{epoch+1}/100], Loos: {loss.item():.4f}")

# Evaluamos el modelo
model.eval()
with torch.no_grad():
    predicted = model(X)
    print("Predicciones:")
    print(predicted.numpy())
