import requests
from colorama import Back, Fore, init
init()


keko = input("Escribe tú keko: ")

respuesta = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
data = respuesta.json()



estado = data["online"]

es = {
    "False":  Fore.RED + "Desconectad@",
    "True": Fore.GREEN + "En línea"
}

estado = es[str(estado)]

print(f'Estado: {estado}')
