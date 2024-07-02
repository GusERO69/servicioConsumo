from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import pymysql

# Conectar a la base de datos MySQL
try:
    conn = pymysql.connect(
        host='34.151.233.27',
        user='CEG4',
        password="'sFk)z/lm1l7nD2;",
        database='Grupo4'
    )
    print("Conectado a la base de datos MySQL")
except pymysql.MySQLError as e:
    print(f"Error al conectar a la base de datos: {e}")

cursor = conn.cursor()
query = "SELECT voltage, current, power, timestamp FROM Lectura"
cursor.execute(query)

results = cursor.fetchall()

conn.close()

df = pd.DataFrame(results, columns=['voltage', 'current', 'power', 'timestamp'])

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day

X = df[['day', 'month', 'year', 'voltage', 'current']]
y = df['power']

print('datos X', len(X))
print('datos Y', len(y))


# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Hacer predicciones con el conjunto de datos de entrenamiento
y_pred = model.predict(X)

# Predicción con nuevos datos
new_data = pd.DataFrame([[3, 7, 2024, 0.4991232, 22.29012]], columns=['day', 'month', 'year', 'voltage', 'current'])
prediction = model.predict(new_data)
print(f"Predicción para [3, 7, 2024, 0.4991232, 22.29012]: {prediction}")
