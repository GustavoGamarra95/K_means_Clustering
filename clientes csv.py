import pandas as pd
import numpy as np

# Definir las listas de opciones
frecuencia_de_compra = ['Alta', 'Media', 'Baja']
tipo_de_producto = ['Electrónica', 'Ropa', 'Hogar', 'Alimentos']
ubicacion_geografica = ['Norte', 'Sur', 'Este', 'Oeste']
edad = ['18-24', '25-34', '35-44', '45-54', '55+']

# Configuración de la semilla para reproducibilidad
np.random.seed(42)
num_registros = 30000  # Ajustar el número de registros

# Generar datos
data = {
    'Frecuencia_de_compra': np.random.choice(frecuencia_de_compra, num_registros),
    'Tipo_de_producto': np.random.choice(tipo_de_producto, num_registros),
    'Ubicacion_geografica': np.random.choice(ubicacion_geografica, num_registros),
    'Edad': np.random.choice(edad, num_registros),
    'Año': np.random.choice([2015, 2016, 2017, 2018], num_registros)  # Columna de años
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('clientes.csv', index=False)

print("Archivo clientes.csv generado con éxito.")
