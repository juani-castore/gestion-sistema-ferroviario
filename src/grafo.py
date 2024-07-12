import json
import networkx as nx
import math
from typing import Hashable
import matplotlib.pyplot as plt

def circulacion(g1):
    for node in g1.nodes():
        edges_in = g1.in_edges(node)
        edges_out = g1.out_edges(node)
        lower_in=0
        lower_out=0
        for edge in edges_in:
            lower_in= lower_in+ g1[edge[0]][edge[1]]['lower_bound_directed']

        for edge in edges_out:
            #print(g1[edge[1]][edge[0]]['lower_bound_directed'])
            lower_out= lower_out+ g1[edge[0]][edge[1]]['lower_bound_directed']
        
        #print(g1.nodes[node]['demand'])
        g1.nodes[node]['demand'] = lower_out-lower_in 
        #print(g1.nodes[node]['demand'])
        #print(lower_in,lower_out,lower_in-lower_out, g1.nodes[node]['demand']) 
    
    
    for edge in g1.edges():
        capacidad = g1.edges[edge]['capacity'] - g1.edges[edge]['lower_bound_directed']
        #print(g1.edges[edge]['capacity'])
        g1.edges[edge]['capacity']= capacidad
        g1.edges[edge]['lower_bound_directed']=0
        #print(g1.edges[edge]['capacity'])
    
    return g1


def crearGrafo(data, x,r):
    '''
    El parametro x lo agregamos porque resulta util en la expermientacion.  representa la proporción en que se incrementará la demanda de cada servicio
    Ejemplo: x=1, no se ve incrementada. x=1.1, aumenta en un 10% la demanda en cada servicio
    
    El parametro r lo agregamos porque resulta util en la expermientacion.  representa la cantidad de minutos retrasados el servicio de llegada. 
    Ejemplo: r=0, no se ve retrasado el horario original. r=2,se ve retrasado en 2 minutos
    '''
    G = nx.DiGraph()
    lista_izq=set()
    lista_der=set()
    
    
    for service in data["services"]:
        ### los nodos tienen como nombre  (horario,estacion, tipo de servicio)
        nodoD = (data["services"][service]["stops"][0]["time"],data["services"][service]["stops"][0]["station"], data["services"][service]["stops"][0]['type'])
        nodoA = (data["services"][service]["stops"][1]["time"]+r,data["services"][service]["stops"][1]["station"], data["services"][service]["stops"][1]['type'])
        G.add_node(nodoD,  demand=0)
        G.add_node(nodoA,  demand=0)
        
        #Agregamos los arcos de tren
        G.add_edge(nodoD,nodoA, lower_bound_directed= math.ceil((((data["services"][service]["demand"][0] *x) / (data["rs_info"]['capacity'])  ))) , capacity=data["rs_info"]["max_rs"], weight=0)
        #Guardamos las aristas de traspaso
        if( data["stations"][1] == nodoD[1]):
            lista_izq.add(nodoD)
            lista_der.add(nodoA)
        else:
            lista_izq.add(nodoA)
            lista_der.add(nodoD)

    #Agregamos los arcos de los de traspaso
    lista_izq=list(lista_izq)
    lista_der=list(lista_der)
    lista_izq = sorted(lista_izq, key=lambda x: x[0])
    lista_der = sorted(lista_der, key=lambda x: x[0])  
    
    for i in range(len(lista_der)-1):
        G.add_edge(lista_der[i], lista_der[i+1],lower_bound_directed=0 , capacity= float('inf'), weight=0 )
        G.add_edge(lista_izq[i], lista_izq[i+1],lower_bound_directed=0 , capacity= float('inf'), weight=0 )         
    
    #Agregamos los arcos de los de trasnoche
    G.add_edge(lista_izq[len(lista_izq)-1], lista_izq[0], lower_bound_directed=0, capacity= float('inf'), weight=1)
    G.add_edge(lista_der[len(lista_der)-1], lista_der[0], lower_bound_directed=0, capacity= float('inf'), weight=1 )
    
    #print( lista_izq)
    #print(lista_der)
    G=circulacion(G)
    	
    return G



def crearGrafoEj4(data, u):
    '''
    Vamos a suponer que la terminal que se está arreglando es Retiro y que la cantidad de vagones máxima que puede tener viene dada por u.
    '''
    G = nx.DiGraph()
    lista_izq=set()
    lista_der=set()
    
    
    for service in data["services"]:
        ### los nodos tienen como nombre  (horario,estacion, tipo de servicio)
        nodoD = (data["services"][service]["stops"][0]["time"],data["services"][service]["stops"][0]["station"], data["services"][service]["stops"][0]['type'])
        nodoA = (data["services"][service]["stops"][1]["time"],data["services"][service]["stops"][1]["station"], data["services"][service]["stops"][1]['type'])
        G.add_node(nodoD,  demand=0)
        G.add_node(nodoA,  demand=0)
        
        #Agregamos los arcos de tren
        G.add_edge(nodoD,nodoA, lower_bound_directed= math.ceil((((data["services"][service]["demand"][0]) / (data["rs_info"]['capacity'])  ))) , capacity=data["rs_info"]["max_rs"], weight=0)
        #Guardamos las aristas de traspaso
        if( data["stations"][1] == nodoD[1]):
            lista_izq.add(nodoD)
            lista_der.add(nodoA)
        else:
            lista_izq.add(nodoA)
            lista_der.add(nodoD)

    #Agregamos los arcos de los de traspaso
    lista_izq=list(lista_izq)
    lista_der=list(lista_der)
    lista_izq = sorted(lista_izq, key=lambda x: x[0])
    lista_der = sorted(lista_der, key=lambda x: x[0])  
    
    for i in range(len(lista_der)-1):
        G.add_edge(lista_der[i], lista_der[i+1],lower_bound_directed=0 , capacity= float('inf'), weight=0 )
        G.add_edge(lista_izq[i], lista_izq[i+1],lower_bound_directed=0 , capacity= float('inf'), weight=0 )    

    # Agregamos un nodo fantasma que representa la estación intermedia para luego agregar el eje que nos mostrara cuantos vagones irán a esta estación intermedia
    nodo_fantasma = (-1,"Estación Intermedia")
    G.add_node(nodo_fantasma)
    G.add_edge(lista_izq[len(lista_izq)-1], nodo_fantasma, lower_bound_directed=0, capacity= float('inf'), weight=2)
    G.add_edge(nodo_fantasma, lista_izq[0], lower_bound_directed=0, capacity= float('inf'), weight=0)
    

    #Agregamos los arcos de los de trasnoche
    G.add_edge(lista_izq[len(lista_izq)-1], lista_izq[0], lower_bound_directed=0, capacity= u, weight=1)
    G.add_edge(lista_der[len(lista_der)-1], lista_der[0], lower_bound_directed=0, capacity= float('inf'), weight=1)
    
    #print( lista_izq)
    #print(lista_der)
    G=circulacion(G)
    	
    return G, lista_izq[len(lista_izq)-1], nodo_fantasma

    

    

        
    

    
        
        
        
            
        

    
    
    
