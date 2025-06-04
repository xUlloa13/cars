
import pandas as pd
import plotly.express as px
import streamlit as st

# --- Título de la aplicación ---
st.header('Análisis de Datos de Anuncios de Venta de Coches')

# --- Cargar los datos ---
# Asegúrate de que 'vehicles_us.csv' esté en el mismo directorio que app.py
car_data = pd.read_csv('vehicles_us.csv')

# --- Opción 1: Usar Botones para generar los gráficos ---

# Botón para construir un histograma
hist_button = st.button('Construir Histograma de Odómetro')

if hist_button: # Si el botón es clickeado
    # Escribe un mensaje
    st.write('Creando un histograma para la distribución de Odómetro')

    # Crear el histograma
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución de Odómetro")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir Gráfico de Dispersión (Odómetro vs. Precio)')

if scatter_button: # Si el botón es clickeado
    # Escribe un mensaje
    st.write('Creando un gráfico de dispersión de Odómetro vs. Precio')

    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
    