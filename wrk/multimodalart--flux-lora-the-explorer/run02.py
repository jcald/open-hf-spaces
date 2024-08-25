#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import platform
from gradio_client import Client

def print_python_version():
    print(platform.python_version())
    print("--------------------------------\n")

def run_update_selection(client):
    width = int(input("Ingrese el ancho (width): ") or 1024)
    height = int(input("Ingrese la altura (height): ") or 1024)
    
    result = client.predict(
        width=width,
        height=height,
        api_name="/update_selection"
    )
    print(result)

def run_lora(client):
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
    
    # Intenta pasar la selección de LoRA como parte de la llamada a `run_lora`
    result = client.predict(
        lora_name=lora_name,
        prompt=prompt,
        cfg_scale=cfg_scale,
        steps=steps,
        randomize_seed=randomize_seed,
        seed=seed,
        width=width,
        height=height,
        lora_scale=lora_scale,
        api_name="/run_lora"
    )
    print(result)

def main():
    print_python_version()
    client = Client("multimodalart/flux-lora-the-explorer")
    
    while True:
        print("Seleccione una opción:")
        print("1. Ejecutar 'update_selection'")
        print("2. Ejecutar 'run_lora'")
        print("3. Salir")
        
        choice = input("Ingrese su elección: ")
        
        if choice == '1':
            run_update_selection(client)
        elif choice == '2':
            run_lora(client)
        elif choice == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

