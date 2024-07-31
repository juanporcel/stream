import streamlit as st
import streamlit.components.v1 as components

def mostrar_data():     

    # Título de la página
    st.title("Visualización de Power BI")

    # Código del iframe
    iframe_code = """
    <iframe title="facturacion" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiNDA5ODllNmEtODgyMy00MmJhLTk1OTctYTc2M2IzYTk2NjY4IiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
    """

    # Mostrar el iframe en la aplicación
    components.html(iframe_code, height=400)

