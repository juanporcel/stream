import streamlit as st

def mostrar_contactanos():
    st.title("¡Contactanos!!")
    st.write("Puedes contactarnos a través de...")

    # Botón de WhatsApp
    numero_telefono = "2604363708"  # Reemplaza con tu número de teléfono
    mensaje = "Hola, me gustaría más información sobre sus servicios."
    url = f"https://wa.me/{numero_telefono}?text={mensaje.replace(' ', '%20')}"
    
    # Icono de WhatsApp
    icono_html = f'''
    <a href="{url}" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="50" height="50" alt="WhatsApp">
    </a>
    '''
    
    st.markdown(icono_html, unsafe_allow_html=True)




