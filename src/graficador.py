import matplotlib.pyplot as plt
import networkx as nx

## Función que grafica un grafo de nx
def graficador(G, output_filename):
    plt.figure(figsize=(12, 8))

    # Algoritmo de posicionamiento de nodos
    pos = nx.spring_layout(G)

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

    # Dibujar aristas
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')

    # Agregar etiquetas de nodos
    labels = {node: f"{node[1]} ({node[0]}, {node[2]})" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)

    # Mostrar peso de las aristas (no es visible en el grafo, pero está en los datos)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title('Grafo de Circulación de Material Rodante')
    plt.axis('on')  # Asegura que los ejes sean visibles

    # Guardar el gráfico en un archivo
    plt.savefig("./graficos/"+output_filename)
    plt.close()