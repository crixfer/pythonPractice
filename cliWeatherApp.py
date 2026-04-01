#CLI Weather App

# importar sys
import sys
# importar requests
import requests

API_KEY = "f6c87e2f2fe8fe3bdce43a5e202f780f"

# si no hay argumento en sys.argv:
if len(sys.argv) < 2:
#     mostrar "Debes pasar una ciudad"
    print("You should add a city!")
#     salir con sys.exit()
    sys.exit()

# ciudad = sys.argv[1]
city = sys.argv[1]

# hacer request a API del clima con la ciudad
url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")

response = requests.get(url)

# si la respuesta falla:
if response.status_code != 200:
#     mostrar error
    print("Request error!")
#     salir
    sys.exit()

data = response.json()

# extraer:
#     temperatura
temp = data["main"]["temp"]
#     descripción del clima
description = data["weather"][0]["description"]

# mostrar resultados en consola
print("Temperature: ", temp)
print("Weather: ", description.capitalize())