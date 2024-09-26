import networkx as nx
import matplotlib.pyplot as plt
import random

# Tworzenie grafu nieskierowanego z losowymi wagami
graf = [[1,4,5,6],[0,4,2],[1,3],[4,2,9],[0,1,5,3],[0,4,6,7],[0,5,7],[6,5,9,8],[7,9],[3,7,8]]
def dodaj_losowe_wagi(lista_sasiedztwa):
    for i in range(len(lista_sasiedztwa)):
        for j in range(len(lista_sasiedztwa[i])):
            lista_sasiedztwa[i][j] = (lista_sasiedztwa[i][j], random.randint(1, 10))
    return lista_sasiedztwa
graf = dodaj_losowe_wagi(graf)
# Rysowanie grafu
def rysuj_graf(graf):
    G = nx.Graph()
    for i, krawedzie in enumerate(graf):
        for krawedz in krawedzie:
            G.add_edge(i, krawedz[0], weight=krawedz[1])

    pos = nx.spring_layout(G)  # układ wierzchołków
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Graf z wagami")
    plt.show()

# Rysowanie grafu z wagami
print("Graf 1 z losowymi wagami:")
rysuj_graf(graf)