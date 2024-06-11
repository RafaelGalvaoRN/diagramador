import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st



# Função para criar o diagrama de vínculos

# Função para criar o diagrama de vínculos com cores e emojis personalizados
def criar_diagrama_de_vinculos(nodos, arestas):
    G = nx.Graph()

    for nodo, color in nodos:
        G.add_node(nodo, color=color)

    for aresta in arestas:
        G.add_edge(*aresta)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.8, iterations=100)

    # Obter as cores dos nodos
    node_colors = [G.nodes[nodo]['color'] for nodo in G.nodes()]

    # Desenhar nodos e arestas
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)

    # Desenhar rótulos com nomes manualmente
    ax = plt.gca()
    for nodo, (x, y) in pos.items():
        ax.text(x, y, nodo, fontsize=12, ha='center', va='center', fontfamily='sans-serif', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

    plt.title("Diagrama de Vínculos")
    st.pyplot(plt)


