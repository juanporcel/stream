import streamlit as st
import inicio
import sobre_nosotros
import data_analytics
import contactanos

# Configurar un favicon personalizado
favicon = "https://web.dev/static/articles/building/an-adaptive-favicon/image/large-easy-distinguish-cc5a0d56fe6fc_960.png?hl=es-419"  # URL o ruta local del archivo favicon

# Inyectar HTML en el encabezado de la página
st.markdown(f"""
    <link rel="icon" href="{favicon}" type="image/x-icon">
    <link rel="shortcut icon" href="{favicon}" type="image/x-icon">
    """, unsafe_allow_html=True)



#Borrar boton de github y 3 puntos de opciones
st.markdown("""
    <style>
    [data-testid="baseButton-header"] {
        display: none !important; 
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown("""
    <style>
    .eyeqlp53 {
        display: none !important; 
    }
    </style>
    """, unsafe_allow_html=True)



# Menú en la barra lateral
a = st.sidebar.radio('Menú:', ["Inicio", "Sobre Nosotros", "Data Analytics", "Contáctanos"])



# Condicionales para cambiar el contenido según la selección del menú
if a == "Inicio":
    inicio.mostrar_inicio()
elif a == "Sobre Nosotros":
    sobre_nosotros.mostrar_sobre_nosotros()
elif a == "Data Analytics":
    data_analytics.mostrar_data()
elif a == "Contáctanos":
    contactanos.mostrar_contactanos()


