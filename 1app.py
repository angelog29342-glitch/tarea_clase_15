import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

st.title('Dashboard interactivo de notas')
st.header('!Buenas tardes, profesora¡')
st.text(' El propósito de la aplicacion es explorar los resultados de un curso combinando filtros. Promedio: 50% de cada evaluación. Aprobación del ejercicio: promedio >= 4')
st.image('logo.png.png')
if st.button('Haga clic aquí'):
  st.write('!PRESIONASTE EL BOTÓN¡')
maya = st.text_input('Escriba aquí')
st.write('Escribió:', maya)
st.sidebar.header('Datos y filtros:')
st.sidebar.text('Buenas tardes, esta seccion es lo mismo que la de la derecha pero mas pequeña.')
file = st.side.file_uploader('Cargue el archivo aquí', type=['csv'])
if file is None:
  st.info('Suba el archivo al costado para comenzar')
  st.stop()
df=pd.read_csv(file, encoding='utf-8-sig')
df[promedio]=(df['nota_1']+df['nota_2'])/2
géneros=st.sidebar.multiselect('Géneros',['Hombre','Mujer'], default=['Hombre','Mujer'])
opciones_seccion = ['Todas'] + sorted(df['seccion'].unique())
seccion=st.sidebar.selectbox('Sección', opciones_seccion())
st.sidebar.image('logo.png.png')
if st.sidebar.button('No hagas clic aquí'):
  st.sidebar.write('!VIRUS¡')
aztec = st.sidebar.text_input('Escriba denuevo')
st.sidebar.write('Escribió:', aztec)
