import streamlit as st
import streamlit.components.v1 as components

def mostrar_data():     

    # Título de la página
    st.title("Visualización de Power BI")
    st.write("Facturación")

    # Código del iframe
    iframe_code = """
    <iframe title="facturacion" width="100" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiNDA5ODllNmEtODgyMy00MmJhLTk1OTctYTc2M2IzYTk2NjY4IiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
    """

    # Mostrar el iframe en la aplicación
    components.html(iframe_code, height=500)

    st.write("Transporte")

    # Código del iframe
    iframe_code = """
    <iframe title="transporte" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiY2I0ZWQ1ZGQtNDBhOC00NDljLWI4NmYtZmFkY2M5MTcyYzk0IiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
    """

    # Mostrar el iframe en la aplicación
    components.html(iframe_code, height=400)

    st.write("Grilla de pacientes")

    # Código del iframe
    iframe_code = """
    <iframe title="grillapacientes" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiODE4YmUxOTMtMjg5ZS00OWM4LThiNDYtMzkxYzM2MGY5YWYyIiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
    """

    # Mostrar el iframe en la aplicación
    components.html(iframe_code, height=400)



