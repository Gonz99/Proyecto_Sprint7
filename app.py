import pandas as pd
import plotly_express as px 
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")
st.header("Aplicacion sobre vehiculos usados")
hist_button = st.button("Construir Histograma")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig_1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_1, use_container_width=True)

buil_histogram = st.checkbox("Construir grafico de dispersión")
if buil_histogram:
    st.write("Construir grafico de dispersión para las columnas de odometro y precio")
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig_2, use_container_width=True)