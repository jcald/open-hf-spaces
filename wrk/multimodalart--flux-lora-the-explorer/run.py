#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import platform
import requests
import time

# Reemplaza 'tu_api_key_aqui' con tu token de API real
API_TOKEN = 'tu_api_key_aqui'
BASE_URL = 'https://multimodalart-flux-lora-the-explorer.hf.space/call/run_lora'

def print_python_version():
    print(platform.python_version())
    print("--------------------------------\n")

def run_update_selection():
    width = int(input("Ingrese el ancho (width): ") or 1024)
    height = int(input("Ingrese la altura (height): ") or 1024)
    
    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = requests.post(
        'https://multimodalart-flux-lora-the-explorer.hf.space/call/update_selection',
        headers=headers,
        json={
            'data': [width, height],
        }
    )
    
    result = response.json()
    print(result)

def run_lora():
    prompt = input("Ingrese el prompt: ") or "Hello!!"
    cfg_scale = float(input("Ingrese el cfg_scale: ") or 1.0)
    steps = int(input("Ingrese el número de steps: ") or 1)
    randomize_seed = input("¿Randomize seed? (True/False): ") or "True"
    randomize_seed = randomize_seed.lower() in ["true", "t", "1"]
    seed = int(input("Ingrese el seed: ") or 0)
    width = int(input("Ingrese el ancho (width): ") or 256)
    height = int(input("Ingrese la altura (height): ") or 256)
    lora_scale = float(input("Ingrese el lora_scale: ") or 0.0)

    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Solicitud POST inicial
    response = requests.post(
        BASE_URL,
        headers=headers,
        json={
            'data': [prompt, cfg_scale, steps, randomize_seed, seed, width, height, lora_scale],
        }
    )
    
    if response.status_code == 200:
        event_id = response.json().get('id')
        if event_id:
            print(f"Solicitud realizada. Event ID: {event_id}")
            # Espera un poco antes de realizar la siguiente solicitud
            time.sleep(555555)
            # Solicitud GET para obtener el resultado
            result_response = requests.get(f'{BASE_URL}/{event_id}', headers=headers)
            result = result_response.json()
            print(result)
        else:
            print("No se recibió un ID de evento.")
    else:
        print(f"Error en la solicitud inicial: {response.text}")

def main():
    print_python_version()
    
    while True:
        print("Seleccione una opción:")
        print("1. Ejecutar 'update_selection'")
        print("2. Ejecutar 'run_lora'")
        print("3. Salir")
        
        choice = input("Ingrese su elección: ")
        
        if choice == '1':
            run_update_selection()
        elif choice == '2':
            run_lora()
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

