"""Lógica del extractor de titulares.

Contiene las funciones que descargan una página web, extraen sus
titulares y los guardan en un archivo. Si ocurre un error, las
funciones lo informan por pantalla en lugar de cortar el programa.
"""

import requests
from bs4 import BeautifulSoup

# Constantes (en MAYÚSCULAS, como pide PEP 8)
TIMEOUT_SEGUNDOS: int = 10
ENCABEZADOS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (extractor_titulares)"
}


def descargar_html(url: str) -> str:
    """Descarga el contenido HTML de una página web.

    Maneja los errores de red más comunes e informa por pantalla
    qué pasó, en lugar de cortar el programa.

    Parámetros:
        url (str): dirección de la página a descargar.

    Retorna:
        str: el HTML de la página, o una cadena vacía si hubo un error.
    """
    try:
        respuesta = requests.get(
            url, headers=ENCABEZADOS, timeout=TIMEOUT_SEGUNDOS
        )
        # Si el servidor respondió 404, 500, etc., esto lanza HTTPError
        respuesta.raise_for_status()

        # Si el servidor no declara la codificación, requests asume
        # ISO-8859-1 y se rompen las tildes y las ñ. Por eso se usa la
        # codificación que detecta el propio contenido.
        respuesta.encoding = respuesta.apparent_encoding

        return respuesta.text
    except requests.exceptions.MissingSchema:
        print("Error: la URL no es válida. Tiene que empezar con "
              "http:// o https://")
    except requests.exceptions.InvalidURL:
        print("Error: la URL no es válida. Revisá que esté bien escrita.")
    except requests.exceptions.Timeout:
        print(f"Error: el sitio tardó más de {TIMEOUT_SEGUNDOS} segundos "
              "en responder.")
    except requests.exceptions.ConnectionError:
        print("Error: no se pudo conectar. Revisá tu conexión a internet "
              "o que la dirección exista.")
    except requests.exceptions.HTTPError as error:
        print(f"Error: el servidor respondió con un problema ({error}).")
    except requests.exceptions.RequestException as error:
        print(f"Error inesperado al descargar la página: {error}")

    return ""


def extraer_titulares(html: str) -> list[str]:
    """Extrae los titulares de un texto HTML.

    Busca las etiquetas <h2> y <h3>, descarta las vacías y las
    repetidas, y conserva el orden en que aparecen en la página.

    Parámetros:
        html (str): contenido HTML de la página.

    Retorna:
        list[str]: lista de titulares (puede estar vacía si la página
        no tiene ninguno).
    """
    titulares: list[str] = []

    sopa = BeautifulSoup(html, "html.parser")
    etiquetas = sopa.find_all(["h2", "h3"])

    for etiqueta in etiquetas:
        # El " " separa el texto de las etiquetas internas con un
        # espacio. Después, split() corta por cualquier espacio o salto
        # de línea y join() une las palabras con un solo espacio.
        texto = " ".join(etiqueta.get_text(" ").split())

        if texto == "":
            continue

        if texto in titulares:
            continue

        titulares.append(texto)

    return titulares


def guardar_titulares(titulares: list[str], nombre_archivo: str) -> bool:
    """Guarda los titulares en un archivo de texto, uno por línea.

    Los numera y usa codificación UTF-8 para respetar tildes y eñes.

    Parámetros:
        titulares (list[str]): titulares a guardar.
        nombre_archivo (str): nombre del archivo de salida.

    Retorna:
        bool: True si se guardó bien, False si hubo un error al escribir.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            numero = 1
            for titular in titulares:
                archivo.write(f"{numero}. {titular}\n")
                numero += 1
    except IOError as error:
        print(f"Error: no se pudo guardar el archivo ({error}).")
        return False

    print(f"Titulares guardados en '{nombre_archivo}'.")
    return True
