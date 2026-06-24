import streamlit as st
import numpy as np
from modelo import prever
from PIL import Image

st.title("🦟 EducaDengue - Classificação de Imagens")

uploaded_file = st.file_uploader("Envie uma imagem", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    imagem = Image.open(uploaded_file)
    st.image(imagem, caption="Imagem enviada", use_column_width=True)
    img_array = np.array(imagem)
    classe, confianca = prever(img_array)
    st.write(f"**Classe:** {classe}")
    st.write(f"**Confiança:** {confianca:.2f}")
