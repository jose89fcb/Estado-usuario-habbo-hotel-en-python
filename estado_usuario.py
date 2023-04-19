import requests


keko = input("Escribe tú keko: ")

respuesta = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
data = respuesta.json()



estado = data["online"]

translations = {
    "False": "Desconectad@",
    "True": "En línea"
}

estado = translations[str(estado)]
print(f'Estado:{estado}')