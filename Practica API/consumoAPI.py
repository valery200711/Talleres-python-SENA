import requests
import json

url = "https://api-colombia.com/api/v1/Department"

try:
    respuesta = requests.get(url, timeout=10)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        
        for atraccion in datos:
            id_municipio = atraccion.get("id","ID no encontrada")
            nombre = atraccion.get("name","Nombre no disponible")
            poblacion = atraccion.get("population","Poblacion no disponible")
            print(f"ID: {id_municipio} - Nombre: {nombre} - Poblacion: {poblacion}\n")
    else:
        print(f"Error en la solicitud: Codigo {respuesta.status_code}")
except requests.exceptions.RequestException as error:
    print(f"Error de conexion: {error}")