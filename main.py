import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import emoji
from utilidades import criar_diagrama_de_vinculos, emojis_atual, emojis_antigo


font_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Color+Emoji&display=swap');

body {
    font-family: 'Noto Color Emoji', sans-serif;
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(font_css, unsafe_allow_html=True)



st.title("APP Gráfico 🌎")

if 'nodos' not in st.session_state:
    st.session_state['nodos'] = []

if 'arestas' not in st.session_state:
    st.session_state['arestas'] = []



col1, col2, col3 = st.columns(3)

with col1:
    nodos_input = st.text_input("Insira um elemento")

with col2:
    emoji_input = st.selectbox("Escolha um emoji", list(emojis_atual.values()))

with col3:
    color = st.color_picker("Escolha uma cor para o elemento", "#00f900")

if st.button("Adicionar Elemento"):
    st.success("Elemento adicionada")
    if nodos_input:
        st.session_state['nodos'].append((f"{nodos_input} {emoji_input}", color))

st.write("Elementos atuais:")

# Caixa para exibir os nodos adicionados, um abaixo do outro
for nodo, color in st.session_state['nodos']:
    st.write(f"- {nodo}")

# Adicionar arestas entre os nodos
st.write("Adicionar ligação / Vínculo entre Elementos:")
nodo1 = st.selectbox("Escolha o primeiro elemento", [n[0] for n in st.session_state['nodos']], key='nodo1')
nodo2 = st.selectbox("Escolha o segundo elemento", [n[0] for n in st.session_state['nodos']], key='nodo2')

if st.button("Adicionar Vínculo / Ligação"):
    if nodo1 != nodo2:
        st.session_state['arestas'].append((nodo1, nodo2))
        st.success(f"Ligação adicionada: {nodo1} - {nodo2}")
    else:
        st.error("Os elementos escolhidas devem ser diferentes")

st.write("Ligações / Vínculos atuais:")
for aresta in st.session_state['arestas']:
    st.write(f"{aresta[0]} - {aresta[1]}")

# Botão para gerar o gráfico
if st.button("Gerar Gráfico"):
    st.title("LEGENDA")
    for aresta in st.session_state['arestas']:
        st.write(f"{aresta[0]} --> {aresta[1]}")

    criar_diagrama_de_vinculos(st.session_state['nodos'], st.session_state['arestas'])

# Botão para limpar a lista de nodos e arestas, se necessário
if st.button("Limpar Elementos e Vínculos"):
    st.session_state['nodos'] = []
    st.session_state['arestas'] = []
    st.experimental_rerun()
