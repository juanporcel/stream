import streamlit as st
import inicio
import sobre_nosotros
import data_analytics
import contactanos

#st.title("¡Bienvenidos!")

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


