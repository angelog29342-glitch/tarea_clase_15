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
file = st.sidebar.file_uploader('Cargue el archivo aquí', type=['csv'])
if file is None:
  st.info('Suba el archivo al costado para comenzar')
  st.stop()
df=pd.read_csv(file, encoding='utf-8-sig')
df['promedio'=(df['nota_1']+df['nota_2'])/2
géneros=st.sidebar.multiselect('Géneros',['Hombre','Mujer'], default=['Hombre','Mujer'])
opciones_seccion = ['Todas'] + sorted(df['seccion'].unique())
seccion=st.sidebar.selectbox('Sección', opciones_seccion())
st.sidebar.image('logo.png.png')
prom_min, prom_max = st.sidebar.slider('Rango del promedio', 1.0, 7.0, (1.0, 7.0), format='%.2f')
asist_min=st.sidebar.number_input('Asistencia mínima (%)', min_value=0, max_value=100, value=0)
st.sidebar.caption('Los filtros se combinan, quitar ambos géneros deja la sección vacía.')

filtros=(df['género'].isin(géneros)) & df['promedio'].between(prom_min, prom_max) & (df['asistencia']>=asist_min)
if seccion != 'Todas':
         filtro=filtro & (df['sección'] == seccion)

# df_sel=df[filtro]

st.markdown(f'**Filtros activos:** {', '.join(géneros)}, Sección: {seccion}' f'Promedio: {prom_min} a {prom_max}, Asistencia mínima: {asist_min}%')
if len(df_sel) == 0:
    st.warning("No hay estudiantes que cumplan los filtros. Cambia la selección.")
    st.stop()
  
promedio_general = df_sel["promedio"].mean()
aprobacion = (df_sel["promedio"] >= 4).mean() * 100
c1, c2, c3 = st.columns(3)
c1.metric("Estudiantes seleccionados", len(df_sel))
c2.metric("Promedio general", coma(promedio_general))
c3.metric("Aprobación", coma(aprobacion) + " %")

izq, der = st.columns([1.1, 1])
with izq:
    tipo = st.radio("Gráfico", ["Notas por estudiante", "Promedio por sección"], horizontal=True)
with der:
    mostrar_tabla = st.checkbox("Mostrar tabla", value=True)

col_grafico, col_tabla = st.columns([1.1, 1])
with col_grafico:
    st.subheader("Visualización de notas") 
    fig, ax = plt.subplots(figsize=(8, 4.5))

    if tipo == "Notas por estudiante":
        ax.bar(df_sel["estudiante"], df_sel["promedio"])
        ax.set_title("Promedio por estudiante")
        ax.set_xlabel("Estudiante")
    else:
        por_seccion = df_sel.groupby("seccion")["promedio"].mean()
        ax.bar(por_seccion.index, por_seccion.values)
        ax.set_title("Promedio por sección")
        ax.set_xlabel("Sección")

    ax.axhline(4, color="red", linestyle="--", label="Aprobación: 4,0")
    ax.set_ylabel("Promedio de notas")
    ax.set_ylim(0, 7)
    ax.tick_params(axis="x", rotation=45)
    ax.legend()

    st.pyplot(fig)
with col_tabla:
    if mostrar_tabla:
        st.subheader("Estudiantes seleccionados")
        tabla = df_sel[["id", "estudiante", "sexo", "seccion", "promedio", "asistencia"]]
        tabla = tabla.rename( columns={
                "id": "ID", "estudiante": "Estudiante", "género": "Género", "seccion": "Sección", "promedio": "Promedio", "asistencia": "Asistencia (%)",})
        st.dataframe(tabla, hide_index=True)
