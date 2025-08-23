# # importamos numpy, pandas
import numpy as np
import pandas as pd
# verificamos la version de numpy
print(np.__version__)

# Crear vector nativo de python
vector = [10, 20, 30, 40, 50]

#acceso a los datos
print(vector)
print(vector[0])  # imprime el primer elemento del vector
print(vector[-1]) # imprime el ultimo elemento del vector
print(len(vector)) # imprime la longitud del vector


# ===================================
# NUMPY
# ===================================

# creamos vectores numpy
vector_numpy = np.array([1, 2, 3, 4, 5])
print(vector_numpy)

vector_consecutivo = np.arange(0, 10)
print(vector_consecutivo)

vector_consecutivo_paso2 = np.arange(0, 10, 2)
print(vector_consecutivo_paso2)

vector_aleatorio = np.random.rand(5)
print(vector_aleatorio)

vector_aleatorio_enteros = np.random.randint(1, 10, 8)
print(vector_aleatorio_enteros)

# Propiedades de los vectores numpy
print('Propiedades de los vectores numpy')
print(vector_aleatorio.dtype)   #tpos de datos
print(vector_aleatorio.size)    #numero de elementos
print(vector_aleatorio.shape)   #dimensiones


# Operaciones vectorizadas
print('Operaciones vectorizadas')

v = np.array([10, 20, 30, 40])
lista_nativa = [10, 20, 30, 40]
lista_multi = [ x * 2 for x in lista_nativa]
print(lista_multi)


print(v)
print(v + 10)       # Suma escalar
print(v * 2)        # Multiplicacion escalar
print(v ** 2)       # Potencia escalar

print(np.sqrt(v))   # Raiz cuadrada
print(np.mean(v))   # Promedio
print(np.sum(v))    # Suma
print(np.max(v))    # Maximo
print(np.min(v))    # Minimo


# ===================================
# PANDAS
# ===================================
# Crear un DataFrame
data = {
    "Nombre": ["Ana", "Karina", "Camila", "Juan"],
    "Edad": [30, 24, 5, 20],
    "Ciudad": ["Bogota", "Medellin", "Cali", "Medellin"]
}
df =pd.DataFrame(data)
print(df)

# ACCESOS DE DATOS
# Acceso a los datos de una columna
print(df["Nombre"])

# Acceso a los datos de varias columnas
print(df[["Nombre", "Edad"]])

# Acceso a los datos de una fila
print(df.loc[3])

# OPERACIONES BASICAS EN PANDAS
# Agregar nueva columna
df["Salario"] = [2000, 5000, 0, 2200]
print(df)

#Calcular estadisticas
print(df["Edad"].mean())    # promedio
print(df["Salario"].max())  # Maximo
print(df["Salario"].min())  # Minimo
print(df["Salario"].sum())  # Suma


# FILTRADO DE DATOS
# filtro de personas mayores de 20
print(df[df["Edad"] > 20]) 

# Filtro por ciudad
print(df[df["Ciudad"] == "Medellin"]) 


# IMPORTAR / EXPORTAR DATOS 
df.to_csv("personas.csv", index=False) #exportamos

df2 = pd.read_csv("personas.csv")
print(df2)

# CREAR UN DATAFRAME VACIO
df_vacio = pd.DataFrame()
print(df_vacio)

# Convertir a numpy array
array_numpy = df2.to_numpy()
print(array_numpy)


