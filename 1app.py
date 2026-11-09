import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Dashboard interactivo de notas')
st.header('!Buenas tardes, profesora¡')
st.text('Esta aplicación sirve para...')
st.image('logo.png.png')
if st.button('Haga clic aquí'):
  st.write('!PRESIONASTE EL BOTÓN¡')
maya = st.text_input('Escriba aquí')
st.write('Escribió:', maya)
st.sidebar.header('Datos y filtros:')
st.sidebar.text('Buenas tardes, esta seccion es lo mismo que la de la derecha pero mas pequeña.')
st.sidebar.image('logo.png.png')
if st.sidebar.button('No hagas clic aquí'):
  st.sidebar.write('!VIRUS¡')
aztec = st.sidebar.text_input('Escriba denuevo')
st.sidebar.write('Escribió:', aztec)
