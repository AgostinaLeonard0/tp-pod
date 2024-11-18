# -*- coding: utf-8 -*-
"""Copia de POD - 03/Pandas/Individual - Agostina Leonard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cQatWnhUWgPc0GzJTzpeKDcL4SfW3CZQ

* *texto en cursiva*   **Año:** [2024]
*   **Alumno/a:** [Agostina Leonard]
*   **Legajo:** [43663468]

# Pandas
A continuación, cada celda va a pedir algo distinto. Por favor, realizarlo con la menor cantidad de lineas posibles y con NumPy.

Importar `pandas` con el alias `pd` e imprimir la versión instalada.
"""

import pandas as pd; print(pd.__version__)

"""Crear la siguiente tabla como un dataframe de Pandas donde cada linea represente un diccionario.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

import pandas as pd; df = pd.DataFrame([{"Index": 9, "nombre": "Brown, James", "edad": 43, "dni": 30123444}, {"Index": 3, "nombre": "Hamkel, Louis V.", "edad": 29, "dni": 44555666}, {"Index": 7, "nombre": "Baptista, Carlos", "edad": 28, "dni": 43120111}]); print(df)

"""Crear la siguiente tabla como un dataframe de Pandas donde todas las lineas esten dentro de un solo diccionario.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

import pandas as pd; df = pd.DataFrame({"Index": [9, 3, 7], "nombre": ["Brown, James", "Hamkel, Louis V.", "Baptista, Carlos"], "edad": [43, 29, 28], "dni": [30123444, 44555666, 43120111]}); print(df)

"""Crear la siguiente tabla como un dataframe de Pandas donde se usen unicamente listas.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

import pandas as pd; df = pd.DataFrame([[9, "Brown, James", 43, 30123444], [3, "Hamkel, Louis V.", 29, 44555666], [7, "Baptista, Carlos", 28, 43120111]], columns=["Index", "nombre", "edad", "dni"]); print(df)

"""Crear la siguiente tabla como un dataframe de Pandas donde se usen unicamente `Series`.

| _Index_ | **nombre**       | **edad** | **dni**  |
|---------|------------------|----------|----------|
| 9       | Brown, James     | 43       | 30123444 |
| 3       | Hamkel, Louis V. | 29       | 44555666 |
| 7       | Baptista, Carlos | 28       | 43120111 |
"""

import pandas as pd; df = pd.DataFrame({"Index": pd.Series([9, 3, 7]), "nombre": pd.Series(["Brown, James", "Hamkel, Louis V.", "Baptista, Carlos"]), "edad": pd.Series([43, 29, 28]), "dni": pd.Series([30123444, 44555666, 43120111])}); print(df)

"""Reutilice cualquiera de los dataframe hechos anteriormente pero agregue la columna `fecha` con el tipo de dato relacionado a fechas.

| _Index_ | **nombre**       | **edad** | **dni**  | **fecha**  |
|---------|------------------|----------|----------|------------|
| 9       | Brown, James     | 43       | 30123444 | 12/08/1981 |
| 3       | Hamkel, Louis V. | 29       | 44555666 | 10/04/1995 |
| 7       | Baptista, Carlos | 28       | 43120111 | 28/05/1996 |
"""

df["fecha"] = pd.to_datetime(["12/08/1981", "10/04/1995", "28/05/1996"], dayfirst=True); print(df)

"""Ejecute la siguiente celda. Se va a descargar un archivo llamado `u.user`."""

!wget https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user

"""Lea el archivo con pandas y muestre las primeras 5 filas."""

!wget https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user
import pandas as pd; df = pd.read_csv("u.user", sep="|"); print(df.head())

"""Utilice la columna `user_id` como indice y saque dicha columna del dataframe


"""

df.set_index("user_id", inplace=True); print(df)

"""¿Cuantas categorias de trabajos hay?"""

num_categorias_trabajos = df['occupation'].nunique()
print(num_categorias_trabajos)

""" Reporte el porcentaje de personas que tiene cada ocupación."""

porcentaje_ocupaciones = df['occupation'].value_counts(normalize=True) * 100
print(porcentaje_ocupaciones)

"""Reporte el promedio de edad de los estudiantes usando indexeo booleano."""

promedio_edad_estudiantes = df[df['occupation'] == 'student']['age'].mean()
print(promedio_edad_estudiantes)

"""Mostrar, con una sola linea y sin importar `matplotlib`, un histograma de las edades de las personas que son administradores."""

df[df['occupation'] == 'administrator']['age'].hist()

"""Reemplace, sin usar `for`, en la columna `gender` `F` por `female` y `M` por `male`."""

df['gender'] = df['gender'].replace({'F': 'female', 'M': 'male'})

"""# Yahoo! Finance

Vamos a analizar acciones. La siguiente linea accede a Yahoo Finance y devuelve un DataFrame con los valores de la acción cada dia desde el 1980.
"""

import yfinance as yf
dataframe = yf.download('AAPL', start="1980-01-01", end="2030-01-01")

"""¿Cual es el registro mas viejo? Imprimirlo."""

print(dataframe.iloc[[0]])

"""Cree la columna `Average` tal que

$$Average =  \frac{High-Low}{2}$$

y muestre con un histograma dicha columna.
"""

dataframe['Average'] = (dataframe['High'] + dataframe['Low']) / 2
dataframe['Average'].hist()

"""Con `matplotlib`, muestre como `Average` fue evolucionando *al final de cada año*."""

import matplotlib.pyplot as plt

yearly_average = dataframe['Average'].resample('A').last()
plt.plot(yearly_average.index, yearly_average.values, marker='o')
plt.title('Evolución de Average al final de cada año')
plt.xlabel('Año')
plt.ylabel('Average')
plt.grid()
plt.show()

"""Muestre con un gráfico de barras, como el volumen fue cambiando *año a año*."""

yearly_volume = dataframe['Volume'].resample('A').sum()
yearly_volume.plot(kind='bar', figsize=(10, 6))
plt.title('Cambio del Volumen Año a Año')
plt.xlabel('Año')
plt.ylabel('Volumen Total')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""# Cancelaciones y Delays de vuelos del 2015

Creese una cuenta en Kaggle e importe los archivos del dataset del siguiente link: https://www.kaggle.com/datasets/usdot/flight-delays. Cree los dataframes `airlines`, `airports`, y `flights` apartir de esos archivos.
"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d usdot/flight-delays
!unzip flight-delays.zip -d flight_delays

import pandas as pd

# Cargar los archivos en DataFrames
airlines = pd.read_csv('flight_delays/airlines.csv')
airports = pd.read_csv('flight_delays/airports.csv')
flights = pd.read_csv('flight_delays/flights.csv')

# Mostrar las primeras filas de cada DataFrame
print(airlines.head())
print(airports.head())
print(flights.head())

"""Combine (*join*) las tablas `airlines`, `airports`, y `flights` en una sola tabla."""

import pandas as pd

airlines = pd.read_csv('flight_delays/airlines.csv')
airports = pd.read_csv('flight_delays/airports.csv')
flights = pd.read_csv('flight_delays/flights.csv')


airports_origin = airports.rename(columns={
    'IATA_CODE': 'ORIGIN_AIRPORT',
    'AIRPORT': 'ORIGIN_AIRPORT_NAME',
    'CITY': 'ORIGIN_CITY',
    'STATE': 'ORIGIN_STATE',
    'COUNTRY': 'ORIGIN_COUNTRY',
    'LATITUDE': 'ORIGIN_LATITUDE',
    'LONGITUDE': 'ORIGIN_LONGITUDE'
})

airports_destination = airports.rename(columns={
    'IATA_CODE': 'DESTINATION_AIRPORT',
    'AIRPORT': 'DESTINATION_AIRPORT_NAME',
    'CITY': 'DESTINATION_CITY',
    'STATE': 'DESTINATION_STATE',
    'COUNTRY': 'DESTINATION_COUNTRY',
    'LATITUDE': 'DESTINATION_LATITUDE',
    'LONGITUDE': 'DESTINATION_LONGITUDE'
})

combined = flights.merge(airlines, left_on='AIRLINE', right_on='IATA_CODE', how='left')
combined = combined.merge(airports_origin, on='ORIGIN_AIRPORT', how='left')
combined = combined.merge(airports_destination, on='DESTINATION_AIRPORT', how='left')
print(combined.head())

"""¿Cuantos vuelos fueron al aeropuerto JFK?"""

num_vuelos_jfk = flights[flights['DESTINATION_AIRPORT'] == 'JFK'].shape[0]
print(num_vuelos_jfk)

"""[texto del enlace](https://)¿Cuantos vuelos hizo la aerolinea AA?"""

num_vuelos_aa = flights[flights['AIRLINE'] == 'AA'].shape[0]
print(num_vuelos_aa)

"""¿Que aerolineas (las primeras 5) tuvo la menor cantidad de vuelos con atrasos? Imprimirlas."""

menor_atrasos = flights[flights['DEPARTURE_DELAY'] > 0].groupby('AIRLINE').size().nsmallest(5)
print(menor_atrasos)

"""¿Que aerolineas (las primeras 5) tuvo la mayor cantidad de vuelos con atrasos? Imprimirlas."""

mayor_atrasos = flights[flights['DEPARTURE_DELAY'] > 0].groupby('AIRLINE').size().nlargest(5)
print(mayor_atrasos)

"""[texto del enlace](https://)Haga un resumen de las razones por la cual los vuelos se atrasan."""

razones_atrasos = flights[['AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']].sum()
print(razones_atrasos)

"""Compruebe si hay columnas con celdas vacias."""

celdas_vacias = flights.isnull().sum()
print(celdas_vacias[celdas_vacias > 0])

"""Haga una imputación de datos COMPLETA del dataframe. Pueden escojer cualquier estrategia y no necesariamente todas las columnas deben seguir la misma estrategia."""

flights['CANCELLATION_REASON'].fillna("Unknown", inplace=True)
flights[['AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY', 'DEPARTURE_DELAY', 'ARRIVAL_DELAY', 'TAXI_OUT', 'TAXI_IN', 'AIR_TIME', 'ELAPSED_TIME']].fillna(0, inplace=True)
flights['TAIL_NUMBER'].fillna("Unknown", inplace=True)
flights['DEPARTURE_TIME'].fillna(flights['DEPARTURE_TIME'].mean(), inplace=True)
flights['ARRIVAL_TIME'].fillna(flights['ARRIVAL_TIME'].mean(), inplace=True)
flights['SCHEDULED_TIME'].fillna(flights['SCHEDULED_TIME'].median(), inplace=True)
print(flights.isnull().sum())