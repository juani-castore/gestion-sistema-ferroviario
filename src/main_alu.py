import json
import networkx as nx
#from tp2.instances.prueba import *
from grafo import *
from graficador import *


def main():
	archivos: list[str] = [] 
	archivos.append("./instances/toy_instance.json")
	archivos.append("./instances/retiro-tigre-semana.json")
	archivos.append("./instances/juani_instance.json")
	archivos.append("./instances/dataset.json")
	archivos.append("./instances/otra_instance.json")
	archivos.append("./instances/ejercicio2_b.json")
	archivos.append("./instances/ejercicio2.json")
	archivos.append("./instances/experimentacion_c.json")
	archivos.append("./instances/experimentacion_c2.json")
	archivos.append("./instances/experimentacion_c3.json")
	archivos.append("./instances/experimentacion_c4.json")
	archivos.append("./instances/services100.json")

	# Seleccionamos el archivo a leer
	print("Los archivos disponibles son: ")
	for i in range(len(archivos)):
		print(str(i) + " - " + archivos[i])
	i = -1 
	while i < 0 or i >= len(archivos):
		i = int(input("Ingrese el número del archivo que desea leer: "))
	file = archivos[i]
	with open(file) as json_file:
		data = json.load(json_file)
	
	
	proporcionDemandaEfectiva = 1
	retraso = 0 
	g1=crearGrafo(data, proporcionDemandaEfectiva,retraso)

	# Dejamos comentado el graficador porque sirve solo para instancias pequeñas
	# Asignar un nombre unico al archivo de salida
	graficador(g1, "grafoRetiroTigre.png")

	flow_dict = nx.min_cost_flow(g1)
	costo = nx.min_cost_flow_cost(g1)
	print("El costo mínimo del flujo máximo, que al mismo tiempo representa la cantidad de vagones que vamos  a utilizar, es: " + str(costo))
	print("Ahora imprimiremos el diccionario con el flujo: ")
	print(flow_dict)


	print("\n-------------------------------------------------------------------------------------------------------------------\n")

	print("Pasando al ejercicio 5 del escenario adicional")
	g1, nodo_ultimo, nodo_intermedio =crearGrafoEj4(data, 3)
	flow_dict = nx.min_cost_flow(g1)
	costo = nx.min_cost_flow_cost(g1)
	print("La cantidad de vagones que hay que reubicar son: " + str(flow_dict[nodo_ultimo][nodo_intermedio]))
	print("El nuevo costo total mínimo del máximo flujo, que ahora NO representa los vagones que necesitaremos, es: " + str(costo))
	print("La cantidad de vagones que vamos a utilizar es: " + str(costo - flow_dict[nodo_ultimo][nodo_intermedio]) )
	print("Ahora imprimiremos el diccionario con el flujo: ")
	print(flow_dict)


	'''
	Esto lo usamos para la experimentación.

	while(r<11):
		g1=crearGrafo(data, proporcionDemandaEfectiva,retraso)
		flow_dict = nx.min_cost_flow(g1)
		costo = nx.min_cost_flow_cost(g1)
		print(str(r),costo)
		r=r+1
	#print(flow_dict)
 
	#Corroborar que el balance sea 0
	suma = 0
	for node in g1.nodes():
		suma = suma + g1.nodes[node]['demand']
	#print(suma)
	'''


if __name__ == "__main__":
	main()