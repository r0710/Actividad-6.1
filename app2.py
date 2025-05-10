# app.py

#####################
# Importamos librerias
import matplotlib.pyplot as plt
import streamlit as st 
import plotly.express as px
import pandas as pd
import io


#####################
# Definimos la instancia
@st.cache_resource

#################
# Creamos la función de carga de datos
def load_data():
    df = pd.read_csv('Socio_NNCOMPLETO.csv')
    df['Usuario'] = df['Usuario'].str.upper()
    usuarios_validos = ['VALENTIN', 'YAEL DAVID', 'YEREMI YAZMIN ', 'RAMIRO ISAI']
    df = df[df['Usuario'].isin(usuarios_validos)]
    columnas = ['Usuario', 'Administrador','botón correcto', 'tiempo de interacción', 'mini juego',
                'número de interacción', 'color presionado', 'dificultad', 'fecha',
                'Juego', 'tiempo de sesión']
    df = df[columnas]
    return df, columnas

st.set_page_config(page_title= "Wuupi Duupi", layout= "wide")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/originals/ee/58/97/ee58978ecfe73a9ad982290b0ba19a84.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.image("cropped-menta.png")

##################
# Cargo los datos obtenidos de la función 'load_data'
df, Lista = load_data()
k_gr = ['bar', 'area', 'pie']

#####################
# CREACIÓN DEL DASHBOARD

st.sidebar.title('Wuupi')  # Puedes cambiar el título si quieres
View = st.sidebar.selectbox(label='Tipo de Análisis', options=['Extracción de características',
                                            'Regresión Lineal','Regresión No Lineal', 'Regresión Logísitca', 'ANOVA'])


# CONTENIDO DE LA VISTA 1
if View == 'Extracción de características':
    Variable_Cat = st.sidebar.selectbox(label = 'Variable', options = Lista[1:])   # Quitamos 'Usuario' de la selección
    tipo_grafica = st.sidebar.selectbox(label = 'Tipo de grafica', options = k_gr[0:])   

    st.title('Extracción de características')

    # Creamos los 4 contenedores de comparación, uno por usuario
    usuarios = df['Usuario'].unique()
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Usuario: VALENTIN
    with col1:
        df_valentin = df[df['Usuario'] == 'VALENTIN']
        tabla_valentin = df_valentin[Variable_Cat].value_counts().reset_index()
        tabla_valentin.columns = ['categorias', 'frecuencia']
        st.subheader('Valentin')
        if tipo_grafica == 'bar':
            fig1, ax= plt.subplots()
            fig1 = px.bar(data_frame=tabla_valentin, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'area':
            fig1, ax= plt.subplots()
            fig1 = px.area(data_frame=tabla_valentin, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'pie':
            fig1, ax= plt.subplots()
            fig1 = px.pie(data_frame=tabla_valentin, names='categorias', values='frecuencia', title=f'Frecuencia de {Variable_Cat}')

        fig1.update_layout(height=300)
        st.plotly_chart(fig1, use_container_width=True)

        #img= io.BytesIO()
        #fig1.savefig(img, format= "png")
        #img.seek(0)

        #st.download_button(
        #    label= (f"Descargar gráfica de {Variable_Cat}"),
        #    data= img,
        #    file_name= (f"Gráfica de {Variable_Cat}.png"),
        #    mime= "image/png"
        #)

    # Usuario: YAEL DAVID
    with col2:
        df_yael = df[df['Usuario'] == 'YAEL DAVID']
        tabla_yael = df_yael[Variable_Cat].value_counts().reset_index()
        tabla_yael.columns = ['categorias', 'frecuencia']
        st.subheader('Yael David')
        if tipo_grafica == 'bar':
            fig2, ax= plt.subplots()
            fig2 = px.bar(data_frame=tabla_yael, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'area':
            fig2, ax= plt.subplots()
            fig2 = px.area(data_frame=tabla_yael, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'pie':
            fig2, ax= plt.subplots()
            fig2 = px.pie(data_frame=tabla_yael, names='categorias', values='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        fig2.update_layout(height=300)
        st.plotly_chart(fig2, use_container_width=True)

        #img2= io.BytesIO()
        #fig2.savefig(img2, format= "png")
        #img2.seek(0)

        #st.download_button(
        #    label= (f"Descargar gráfica de {Variable_Cat}"),
        #    data2= img2,
        #    file_name= (f"Gráfica de {Variable_Cat}.png"),
        #    mime= "image/png"
        #)

    # Usuario: YEREMI YAZMIN
    with col3:
        df_yeremi = df[df['Usuario'] == 'YEREMI YAZMIN ']
        tabla_yeremi = df_yeremi[Variable_Cat].value_counts().reset_index()
        tabla_yeremi.columns = ['categorias', 'frecuencia']
        st.subheader('Yeremi Yazmin')
        if tipo_grafica == 'bar':
            fig3, ax= plt.subplots()
            fig3 = px.bar(data_frame=tabla_yeremi, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'area':
            fig3, ax= plt.subplots()
            fig3 = px.area(data_frame=tabla_yeremi, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'pie':
            fig3, ax= plt.subplots()
            fig3 = px.pie(data_frame=tabla_yeremi, names='categorias', values='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        fig3.update_layout(height=300)
        st.plotly_chart(fig3, use_container_width=True)

        #img3= io.BytesIO()
        #fig3.savefig(img3, format= "png")
        #img3.seek(0)

        #st.download_button(
        #    label= (f"Descargar gráfica de {Variable_Cat}"),
        #    data3= img3,
        #    file_name= (f"Gráfica de {Variable_Cat}.png"),
        #    mime= "image/png"
        #)

    # Usuario: RAMIRO ISAI
    with col4:
        df_ramiro = df[df['Usuario'] == 'RAMIRO ISAI']
        tabla_ramiro = df_ramiro[Variable_Cat].value_counts().reset_index()
        tabla_ramiro.columns = ['categorias', 'frecuencia']
        st.subheader('Ramiro Isai')
        if tipo_grafica == 'bar':
            fig4, ax= plt.subplots()
            fig4 = px.bar(data_frame=tabla_ramiro, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'area':
            fig4, ax= plt.subplots()
            fig4 = px.area(data_frame=tabla_ramiro, x='categorias', y='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        elif tipo_grafica == 'pie':
            fig4, ax= plt.subplots()
            fig4 = px.pie(data_frame=tabla_ramiro, names='categorias', values='frecuencia', title=f'Frecuencia de {Variable_Cat}')
        fig4.update_layout(height=300)
        st.plotly_chart(fig4, use_container_width=True)

        #img4= io.BytesIO()
        #fig4.savefig(img4, format= "png")
        #img4.seek(0)

        #st.download_button(
        #    label= (f"Descargar gráfica de {Variable_Cat}"),
        #    data4= img4,
        #    file_name= (f"Gráfica de {Variable_Cat}.png"),
        #    mime= "image/png"
        #)