# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16FMT8ihRp9N0Y2x14s_hyIa65EMudaeB
"""

pip install streamlit

import streamlit as st

# titulo de la aplicacion

st.title("Mi primera aplicacion con Streamlit")

# Configuracion del side bar

with st.sidebar:
  st.header ("opciones")
  option = st.selectbox ("Selecciona una opcion:",["opcion 1", "opcion 2"])

# Mostrar el contenido basado en la opcion seleccionada

if option == "opcion 1":
  st.write("Has seleccionado la opcion 1")
else:
  st.write("Has seleccionado la opcion 2")

# grafico

st.write ("Aqui puedes ver un grafico de ejemplo")
st.line_chart([1,2,3,4,5])