import tensorflow as tf
import requests
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

r = requests.get('http://127.0.0.1:8000/')

# Datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # XOR problem

#Datos test
# t = np.array([[0,1], [0,0], [1,0], [1,1]])
t = np.array(r.json())

# Crear el modelo
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=1000, verbose=3)

# Predicción
predictions = model.predict(t)
print(predictions)
umbral = 0.3
for i in predictions:
    for j in i:
        if(j<0.3) : 
            print ("0")
        else :
            print("1")
