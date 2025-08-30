# pip install matplotlib
import matplotlib.pyplot as plt
import pandas as pd
'''
GRAFICOS EN LINEA
'''
# Datos
x = [1,2,3,4,5]
y = [2,8,6,8,10]

plt.plot(x, y, label="Linea de ejemplo", color="red")
plt.title("Grafico de lineas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()


'''
GRAFICOS EN BARRAS
'''
plt.bar(x, y, label="Barra de ejemplo", color="green")
plt.title("Grafico de barras")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()


df = pd.read_csv("personas.csv")
print(df)

plt.bar(df["Nombre"], df["Salario"], label="salarios", color="orange")
plt.title("Salario del personal")
plt.xlabel("Nombres")
plt.ylabel("Salarios")
plt.legend()
plt.show()
