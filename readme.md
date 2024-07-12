 Gestión eficiente de recursos en sistemas ferroviarios
 Trabajo para la materia diseño de algoritmos

## Integrantes
- [Juan Ignacio Castore]
- [Catalina Brusco]
- [Catalina Aufiero]


+ Motivación
En un contexto global donde el cambio climático es un desafío creciente, la eficiencia en el transporte ferroviario se vuelve crucial. Los sistemas ferroviarios, con su baja huella ambiental, son fundamentales para reducir las emisiones de gases de efecto invernadero y promover la movilidad sostenible.

+ Descripción del Problema
El problema abordado en este proyecto se centra en optimizar la circulación de material rodante en un sistema ferroviario específico, minimizando la cantidad total de vagones necesarios para satisfacer la demanda de pasajeros en servicios planificados entre dos estaciones cabeceras.

Estructura de carpetas y archivos

├── enunciado
│   ├── enunciado.pdf
│   └── paperTeorico.pdf
├── instances
│   ├── prueba.py(generador de instancias aleatorias)
├── src
│   ├── grafo.py (funciones para crear el grafo)
│   ├── main_alu.py (funciones para resolver el problema)
├── tools
│   ├── instance_converter.py
└── readme.md

+ Modelo Propuesto
El modelo se basa en la formulación de red espacio-tiempo descrita por Schrijver [1], adaptada para permitir traspasos de material rodante solo en estaciones cabecera. Se utiliza un grafo dirigido donde los vértices representan eventos (partidas y llegadas de servicios) y los arcos modelan los viajes de los servicios y los traspasos de material rodante.

+ Implementación y Algoritmos
Se implementó el modelo en Python utilizando la biblioteca NetworkX para representar y resolver el problema de circulación en la red definida. Se utiliza un algoritmo de flujo en redes para encontrar la asignación óptima de vagones que minimice la cantidad total utilizada.

+ Datos
Los datos de entrada se proporcionan en formato JSON, detallando el cronograma de servicios, la demanda de pasajeros y las capacidades de los vagones. Se incluyen múltiples instancias para permitir pruebas y experimentación con diferentes escenarios de demanda.

+ Experimentación y Resultados
Se realizaron experimentos exhaustivos utilizando diferentes instancias proporcionadas y se compararon los resultados obtenidos con métodos manuales utilizados actualmente por la empresa. Se analizó la efectividad de la solución propuesta y se discutieron posibles mejoras y ajustes.

+ referencias
[1] Alexander Schrijver. Flows in railway optimization. Nieuw Archief voor Wiskunde, 9(2):126, 2008.

