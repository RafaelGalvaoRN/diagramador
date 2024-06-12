import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.font_manager import FontProperties
import platform



# Função para criar o diagrama de vínculos com cores e emojis personalizados
# def criar_diagrama_de_vinculos(nodos, arestas):
#     G = nx.Graph()
#
#     for nodo, color in nodos:
#         G.add_node(nodo, color=color)
#
#     for aresta in arestas:
#         G.add_edge(*aresta)
#
#     plt.figure(figsize=(12, 8))
#     pos = nx.spring_layout(G, k=0.8, iterations=100)
#
#     # Obter as cores dos nodos
#     node_colors = [G.nodes[nodo]['color'] for nodo in G.nodes()]
#
#     # Desenhar nodos e arestas
#     nx.draw_networkx_edges(G, pos)
#     nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
#
#     # Desenhar rótulos com nomes manualmente
#     ax = plt.gca()
#     for nodo, (x, y) in pos.items():
#         ax.text(x, y, nodo, fontsize=12, ha='center', va='center',
#                 fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))
#
#     plt.title("Diagrama de Vínculos")
#     st.pyplot(plt)


emojis_antigo = {
    "Casa": "⌂",
    "Trabalho": "⚒",
    "Carro": "►",
    "Dinheiro": "$",
    "Homem": "♂",
    "Mulher": "♀",
    "Planta": "⚘",
    "Telefone": "☎",
    "Email": "✉",
    "Computador": "⌨",
    "Sorriso": "☺",
    "Triste": "☹",
    "Coração": "♡",
    "Sol": "☀",
    "Avião": "✈",

}

emojis_atual = {
    "Casa": "🏠",
    "Trabalho": "💼",
    "Carro": "🚗",
    "Dinheiro": "💰",
    "Homem": "👨",
    "Mulher": "👩",
    "Planta": "🌿",
    "Telefone": "📞",
    "Email": "📧",
    "Computador": "💻",
    "Sorriso": "😊",
    "Triste": "☹️",
    "Coração": "❤️",
    "Sol": "☀️",
    "Avião": "✈️",

}

def extrair_nome_emoji(nodo):
    for nome_atual, emoji_atual in emojis_atual.items():
        if emoji_atual in nodo:
            nome = nodo.replace(emoji_atual, '').strip()
            return nome, nome_atual
    return nodo, None

def criar_diagrama_de_vinculos(nodos, arestas):
    G = nx.Graph()

    for nodo, color in nodos:
        nome, nome_emoji = extrair_nome_emoji(nodo)
        emoji_antigo = emojis_antigo.get(nome_emoji, '')
        G.add_node(f"{nome} {emoji_antigo}", color=color)

    for aresta in arestas:
        nome1, nome_emoji1 = extrair_nome_emoji(aresta[0])
        nome2, nome_emoji2 = extrair_nome_emoji(aresta[1])
        emoji_antigo1 = emojis_antigo.get(nome_emoji1, '')
        emoji_antigo2 = emojis_antigo.get(nome_emoji2, '')
        G.add_edge(f"{nome1} {emoji_antigo1}", f"{nome2} {emoji_antigo2}")

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
        ax.text(x, y, nodo, fontsize=12, ha='center', va='center', fontweight='bold',
                bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.3'))

    plt.title("Diagrama de Vínculos")
    st.pyplot(plt)
