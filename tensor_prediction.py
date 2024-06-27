import tensorflow as tf
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Dense
import numpy as np


# Datos de ejemplo
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
y = np.array([-0.025, -0.020, -0.015, -0.010, -0.005, 0.000, 0.005, 0.010, 0.015, 0.020, 0.025])

# Crear el modelo
model = Sequential()
model.add(Dense(11, input_dim=3, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=1000, verbose=1)

t = np.array([[15, 0.000375, 0.108120]])

# Predicción
predictions = model.predict(t)
print(predictions)
