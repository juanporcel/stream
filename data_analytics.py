import streamlit as st
import pandas as pd
import numpy as np

def mostrar_data():
    st.title("Data Analytics")
    st.write("Aquí puedes ver los análisis de datos más recientes.")
    data = pd.DataFrame(
        np.random.randn(100, 3),
        columns=['a', 'b', 'c']
    )
    st.area_chart(data)
