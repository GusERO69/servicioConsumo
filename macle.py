from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Generar datos de entrenamiento falsos
X = np.array([
    [-10, -0.001250, -0.020000],
    [-8, -0.001000, -0.018000],
    [-6, -0.000750, -0.015000],
    [-4, -0.000500, -0.012000],
    [-2, -0.000250, -0.009000],
    [0, 0.000000, -0.006000],
    [2, 0.000250, -0.003000],
    [4, 0.000500, 0.000000],
    [6, 0.000750, 0.003000],
    [8, 0.001000, 0.006000],
    [10, 0.001250, 0.009000]
])
# Datos de consumo correspondientes (Power)
y = np.array([-0.025, -0.020, -0.015, -0.010, -0.005, 0.000, 0.005, 0.010, 0.015, 0.020, 0.025])

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X, y)

# Hacer predicciones con el conjunto de datos de entrenamiento
y_pred = model.predict(X)

# Calcular MAE y MSE
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

# Calcular el margen de error en porcentaje
mae_percentage = (mae / np.mean(np.abs(y))) * 100

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"MAE Percentage: {mae_percentage}%")

# Predicción con nuevos datos
# Nuevos datos para predicción [ADC Value, Voltage, Current]
new_data = [[15, 0.000375, 0.108120]]
prediction = model.predict(new_data)
print(f"Predicción para [15, 0.000375, 0.108120]: {prediction}")
