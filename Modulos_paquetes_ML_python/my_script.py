# Importamos librerias de sklearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargamos el dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividiendo el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)

#Entrenando el modelo con fit
model.fit(X_train, y_train)

# Predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactidud del modelo: {accuracy:.2f}")

# Largo, ancho, lardo_petalo y ancho_petalo
nueva_flow = [[5.0, 3.6, 1.4, 0.2]]
prediccion = model.predict(nueva_flow)
print(f"La prediccion es: {iris.target_names[prediccion][0]}")



