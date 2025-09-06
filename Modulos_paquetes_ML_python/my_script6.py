import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = sns.load_dataset('iris')

# Grafico de dispersion
sns.scatterplot(
    x = 'sepal_length',
    y = 'petal_length',
    data = data,
    palette= "Set2"
)

# Personalizo con matplotlib
plt.title("Grafico de dispersion de iris")
plt.xlabel("Longitud del sepalo")
plt.ylabel("Longitud del petalo")

plt.show()

# MAPA DE CALOR
data = np.random.rand(5, 5)

sns.heatmap(data, annot=True, cmap="YlGnBu")

plt.title("Mapa de calor")
plt.xlabel("Columnas")
plt.ylabel("Filas")
plt.show()
