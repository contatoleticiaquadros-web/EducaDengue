import streamlit as st
import numpy as np
from PIL import Image
from modelo import prever

st.set_page_config(
    page_title="EducaDengue",
    page_icon="🦟",
    layout="wide"
)

st.title("EducaDengue 🦟")
st.caption(
    "Projeto Educacional de Combate à Dengue"
)

st.divider()

arquivo = st.file_uploader(
    "Envie uma imagem para análise",
    type=["jpg", "jpeg", "png"]
)

if arquivo is not None:

    imagem = Image.open(arquivo).convert("RGB")
    imagem_np = np.array(imagem)

    classe, confianca = prever(imagem_np)

    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.subheader("Imagem enviada")
        st.image(imagem)

    with col2:

        st.subheader("Resultado da IA")

        percentual = int(confianca * 100)

        if "Alto" in classe:

            st.error("🔴 ALTO RISCO")

            mensagem = """
Condições favoráveis para a proliferação do mosquito Aedes aegypti.

Recomenda-se inspeção imediata do local e eliminação de recipientes com água parada.
"""

        elif "Médio" in classe:

            st.warning("🟡 MÉDIO RISCO")

            mensagem = """
Foram identificadas características que merecem atenção.

É recomendada uma vistoria preventiva para eliminar possíveis riscos.
"""

        else:

            st.success("🟢 BAIXO RISCO")

            mensagem = """
Não foram identificados indícios relevantes de foco de dengue na imagem analisada.

Mantenha inspeções periódicas para prevenção.
"""

        st.progress(confianca)

        st.metric(
            label="Confiança da IA",
            value=f"{percentual}%"
        )

        st.markdown(mensagem)

    st.divider()

    with st.expander("🔬 Detalhes da classificação"):

        st.write(f"Classe identificada: {classe}")
        st.write(f"Confiança: {percentual}%")

st.divider()

st.caption(
    "Saúde começa com consciência | EducaDengue"
)
