import json
import random

def generate_data(num_lines):
    data = {
        "services": {},
        "stations": ["Belgrano", "Palermo"],
        "cost_per_unit": {"Belgrano": 1.0, "Palermo": 1.0},
        "rs_info": {"capacity": 100, "max_rs": 25}
    }
    x=100
    y=120
    for i in range(1, num_lines//2 + 1):
        time_1 = random.randint(x, y)  # Random time for first stop
        time_2 = time_1 + random.randint(50, 80)  # Time for second stop, increasing

        service1 = {
            "stops": [
                {"time": time_1, "station": "Belgrano", "type": "D"},
                {"time": time_2, "station": "Palermo", "type": "A"}
                
                
            ],
            "demand": [500]
        }
        

        data["services"][str(i)] = service1
        x=x+20
        y=y+20

    x=100
    y=120
    for i in range(num_lines//2 + 1, num_lines+1):
        time_1 = random.randint(x, y)  # Random time for first stop
        time_2 = time_1 + random.randint(50, 80)  # Time for second stop, increasing
        
        service2 = {
            "stops": [
                {"time": time_1, "station": "Palermo", "type": "D"},
                {"time": time_2, "station": "Belgrano", "type": "A"}
                
                
            ],
            "demand": [500]
        }


        data["services"][str(i)] = service2
        x=x+20
        y=y+20

    return data

# Generar datos con 10 líneas
generated_data = generate_data(100)
filename = './services1000.json'

with open(filename, 'w') as json_file:
    json.dump(generated_data, json_file, indent=4)

