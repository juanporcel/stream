import streamlit as st
import streamlit.components.v1 as components

def mostrar_data():
    st.title("Visualización de Power BI")
    st.write("Facturación")

    # Código del iframe con estilos CSS para adaptabilidad
    iframe_code_facturacion = """
    <div style="display: flex; justify-content: center;">
        <iframe title="facturacion" width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiNDA5ODllNmEtODgyMy00MmJhLTk1OTctYTc2M2IzYTk2NjY4IiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true" style="border:0; width: 100%; max-width: 1000px;"></iframe>
    </div>
    """
    components.html(iframe_code_facturacion, height=500)

    st.write("Transporte")
    iframe_code_transporte = """
    <div style="display: flex; justify-content: center;">
        <iframe title="transporte" width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiY2I0ZWQ1ZGQtNDBhOC00NDljLWI4NmYtZmFkY2M5MTcyYzk0IiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true" style="border:0; width: 100%; max-width: 1000px;"></iframe>
    </div>
    """
    components.html(iframe_code_transporte, height=500)

    st.write("Grilla de pacientes")
    iframe_code_grilla_pacientes = """
    <div style="display: flex; justify-content: center;">
        <iframe title="grillapacientes" width="100%" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiODE4YmUxOTMtMjg5ZS00OWM4LThiNDYtMzkxYzM2MGY5YWYyIiwidCI6ImRiODM5ZTQ4LWE0YzYtNDU5ZC1iOWMwLTZmNzI5M2RiOGYzYiIsImMiOjR9" frameborder="0" allowFullScreen="true" style="border:0; width: 100%; max-width: 1000px;"></iframe>
    </div>
    """
    components.html(iframe_code_grilla_pacientes, height=500)

# Llamada a la función para mostrar los datos
mostrar_data()



