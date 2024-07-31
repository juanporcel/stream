import streamlit as st
import inicio
import sobre_nosotros
import data_analytics
import contactanos



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
a = st.sidebar.radio('Menú:', ["Inicio", "Sobre Nosotros", "Tableros Power BI", "Contáctanos"])



# Condicionales para cambiar el contenido según la selección del menú
if a == "Inicio":
    inicio.mostrar_inicio()
elif a == "Sobre Nosotros":
    sobre_nosotros.mostrar_sobre_nosotros()
elif a == "Tableros Power BI":
    data_analytics.mostrar_data()
elif a == "Contáctanos":
    contactanos.mostrar_contactanos()


