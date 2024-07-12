from grafo import *
import numpy as np
import matplotlib.pyplot as plt


def experimento(maxServices):
    instance = {"services": {
    "1": {"stops": [{"time": 100, "station": "Retiro", "type": "D"}, {"time": 110, "station": "Tigre", "type": "A"}], "demand": [500]}, 
    "2": {"stops": [{"time": 120, "station": "Tigre", "type": "D"}, {"time": 130, "station": "Retiro", "type": "A"}], "demand": [500]}, }, 
    "stations": ["Tigre", "Retiro"], "cost_per_unit": {"Tigre": 1.0, "Retiro": 1.0}, "rs_info": {"capacity": 100, "max_rs": 25}}
    i = 1
    time = 140
    stations = ["Tigre", "Retiro"]
    data: list[tuple[int, int]] = []
    while i < maxServices:
        g = crearGrafo(instance, 1, 0)
        costo = nx.min_cost_flow_cost(g)
        data.append((costo, i+1)) ## los datos se guardan como (costo, cantServicios)
        instance["services"][str(i+2)] = {"stops": [{"time": time, "station": stations[i%2], "type": "D"}, {"time": time+10, "station": stations[(i+1)%2], "type": "A"}], "demand": [500]}
        i += 1
        time += 20
    return data

def graficarData(data):
    x = np.array([i[1] for i in data])
    y = np.array([i[0] for i in data])
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, marker='o', color='blue')  # Usamos scatter para puntos discretos
    plt.xlabel('Cantidad de servicios')
    plt.ylabel('Costo de proveer todos los servicios')
    plt.title('Costo en funcion de la cantidad de servicios')
    plt.grid(True)
    plt.show()

## si el nro de servicios es muy grande, tarda mucho en ejecutar
data = experimento(100)
print(data)
graficarData(data)




