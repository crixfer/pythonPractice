# Currency Converter 💵

import sys
import requests

print("Add the currency: Amount, origin and destination.")

try:
    amount = int(input("What is the amount: "))
except ValueError:
    print("Please enter a valid number.")
    sys.exit()

origin = input("Add the origin of the currency. eg: DOP, USD: ").upper()
destination = input("Add the destination to be changed to: ").upper()

if amount <= 0 or not origin or not destination:
    print("You are missing required information to proceed.")
    sys.exit()

url = f"https://api.frankfurter.app/latest?from={origin}&to={destination}"
response = requests.get(url)

if response.status_code != 200:
    print("Error fetching data")
    sys.exit()

data = response.json()

if "rates" not in data:
    print("API error:", data)
    sys.exit()

if destination not in data["rates"]:
    print("Invalid currency code.")
    sys.exit()

rate = data["rates"][destination]
result = amount * rate

print(f"{amount} {origin} = {result:.2f} {destination}")
print(data)