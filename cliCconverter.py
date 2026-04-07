# CLI Currency Converter

# importar sys
import sys
# importar requests
import requests


# esperar argumentos:
#     monto
#     moneda_origen
#     moneda_destino
if len(sys.argv) != 4:
    print("After: cliCconverter.py <amount> <from_currency> <to_currency> and press ENTER")
    print("Example: cliCconverter.py 1000 USD DOP")
    sys.exit()


# asignar argumentos
try:
    amount = float(sys.argv[1])
except ValueError:
    print("The amount should be a valid number.")
    sys.exit()

from_c = sys.argv[2].upper()
to_c = sys.argv[3].upper()

# hacer request a API de tasas de cambio
url = f"https://api.frankfurter.app/latest?from={from_c}&to={to_c}"
response = requests.get(url)

# si falla:
if response.status_code != 200:
    print("There was an error with the API data.")
#     salir
    sys.exit()

data = response.json()

if "rates" not in data or to_c not in data["rates"]:
    print("Invalid currency code or API error.")
    sys.exit()

# obtener tasa de conversión desde la api
rate = data["rates"][to_c]
# resultado = monto * tasa
result = amount * rate
# mostrar resultado
print(f"{amount} {from_c} = {result:.2f} {to_c}")