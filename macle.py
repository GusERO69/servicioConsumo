from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import pymysql

# Conectar a la base de datos MySQL
try:
    conn = pymysql.connect(
        host='localhost',        # Por ejemplo, 'localhost' si es local
        user='root',     # Tu usuario de la base de datos
        password='123456', # Tu contraseña de la base de datos
        database='energy_monitor' # El nombre de tu base de datos
    )
    print("Conectado a la base de datos MySQL")
except pymysql.MySQLError as e:
    print(f"Error al conectar a la base de datos: {e}")

cursor = conn.cursor()
query = "SELECT voltage, current, power FROM home"
cursor.execute(query)

# Obtener todos los resultados
results = cursor.fetchall()

conn.close()

# Generar datos de entrenamiento falsos
# X = np.array([
#     [-4,-0.000500015,-0.015152],
#     [-4,-0.000500015,-0.015152],
#     [-6,-0.000750023,-0.022728],
#     [-6,-0.000750023,-0.022728],
#     [-3,-0.000375011,-0.011364],
#     [-5,-0.000625019,-0.01894],
#     [-6,-0.000750023,-0.022728],
#     [-5,-0.000625019,-0.01894],
#     [-4,-0.000500015,-0.015152],
#     [-5,-0.000625019,-0.01894],  
# ])
X = []
y = []

# y = np.array([
#     -0.00348495,
#     -0.00348495,
#     -0.00522743,
#     -0.00522743,
#     -0.00261372,
#     -0.00435619,
#     -0.00522743,
#     -0.00435619,
#     -0.00348495,
#     -0.00435619,
# ])
for row in results:
    X.append([row[0], row[1]])
    y.append(row[2])

print('datos X', len(X))
print('datos Y', len(y))


# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Hacer predicciones con el conjunto de datos de entrenamiento
y_pred = model.predict(X)

# Predicción con nuevos datos
# Nuevos datos para predicción [ADC Value, Voltage, Current]
new_data = [[-0.000625019,-0.01894]]
prediction = model.predict(new_data)
print(f"Predicción para [-0.000625019,-0.01894]: {prediction}")
