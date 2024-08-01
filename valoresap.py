import streamlit as st
import streamlit.components.v1 as components

def mostrar_cuadro_valores():

    # Código del iframe con estilos CSS para adaptabilidad
    iframe_code_valores = """
    <div style="display: flex; justify-content: center;">
        <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSlH7Y6NTXvhkpH9BMoY3Q2mvdijJ0_sDmmOFzNiQip0iwd4xyPd46TGZvvgufw17xelQ6iobLJ5ySK/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false"></iframe>
    </div>
    """
    components.html(iframe_code_valores, height=300)
    