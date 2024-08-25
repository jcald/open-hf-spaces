#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import platform
import requests

# Reemplaza 'tu_api_key_aqui' con tu token de API real
API_TOKEN = 'tu_api_key_aqui'
API_URL = 'https://multimodalart-flux-lora-the-explorer.hf.space/api/predict/'

def print_python_version():
    print(platform.python_version())
    print("--------------------------------\n")

def run_update_selection():
    width = int(input("Ingrese el ancho (width): ") or 1024)
    height = int(input("Ingrese la altura (height): ") or 1024)
    
    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={
            'fn_index': 0,  # Ajusta este índice según la función específica de 'update_selection'
            'data': [width, height],
        }
    )
    
    result = response.json()
    print(result)

def run_lora():
    lora_name = input("Ingrese el nombre de la LoRA: ")
    prompt = input("Ingrese el prompt: ") or "Hello!!"
    cfg_scale = float(input("Ingrese el cfg_scale: ") or 3.5)
    steps = int(input("Ingrese el número de steps: ") or 28)
    randomize_seed = input("¿Randomize seed? (True/False): ") or "True"
    randomize_seed = randomize_seed.lower() in ["true", "t", "1"]
    seed = int(input("Ingrese el seed: ") or 2433143866)
    width = int(input("Ingrese el ancho (width): ") or 1024)
    height = int(input("Ingrese la altura (height): ") or 1024)
    lora_scale = float(input("Ingrese el lora_scale: ") or 0.95)

    headers = {
        'Authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={
            'fn_index': 1,  # Ajusta este índice según la función específica de 'run_lora'
            'data': [lora_name, prompt, cfg_scale, steps, randomize_seed, seed, width, height, lora_scale],
        }
    )

    result = response.json()
    print(result)

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

