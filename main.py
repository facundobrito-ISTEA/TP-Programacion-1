"""Extractor de titulares: punto de entrada.

Programa de consola que pide una URL, descarga la página, muestra los
primeros titulares numerados y, si el usuario quiere, los guarda en un
archivo de texto. La lógica está en extractor.py.
"""

from extractor import descargar_html, extraer_titulares, guardar_titulares

# Constantes (en MAYÚSCULAS, como pide PEP 8)
URL_POR_DEFECTO: str = "https://www.bbc.com/mundo"
CANTIDAD_TITULARES: int = 10
ARCHIVO_SALIDA: str = "titulares.txt"


def pedir_url() -> str:
    """Pide la URL al usuario.

    Si el usuario no escribe nada, usa la URL por defecto. Si escribe
    una dirección sin "://" (por ejemplo "sitio.com"), le agrega
    "https://" al principio.

    Retorna:
        str: la URL ingresada (sin espacios en los bordes) o la
        URL por defecto.
    """
    texto = input(f"URL del sitio (Enter para usar {URL_POR_DEFECTO}): ")
    texto = texto.strip()

    if texto == "":
        return URL_POR_DEFECTO

    if "://" not in texto:
        texto = "https://" + texto

    return texto


def mostrar_titulares(titulares: list[str], total: int) -> None:
    """Muestra por pantalla los titulares recibidos, numerados.

    Parámetros:
        titulares (list[str]): titulares a mostrar.
        total (int): cantidad total de titulares encontrados en la
            página (puede ser mayor a los que se muestran).

    Retorna:
        None
    """
    print()
    print(f"Se muestran {len(titulares)} de {total} titulares:")
    print()

    numero = 1
    for titular in titulares:
        print(f"{numero}. {titular}")
        numero += 1


def preguntar_si_guardar() -> bool:
    """Pregunta al usuario si quiere guardar los titulares en un archivo.

    Repite la pregunta hasta recibir una respuesta válida (s o n).

    Retorna:
        bool: True si la respuesta es sí, False si es no.
    """
    while True:
        respuesta = input("\n¿Querés guardar los titulares en un archivo? "
                          "(s/n): ")
        respuesta = respuesta.strip().lower()

        if respuesta == "s":
            return True
        if respuesta == "n":
            return False

        print("Respuesta no válida. Escribí 's' o 'n'.")


def main() -> None:
    """Coordina los pasos del programa."""
    print("=== Extractor de titulares ===")

    url = pedir_url()

    print(f"\nDescargando {url} ...")
    html = descargar_html(url)
    if html == "":
        print("No se pudo obtener la página. Fin del programa.")
        return

    titulares = extraer_titulares(html)
    if len(titulares) == 0:
        print("La página se descargó, pero no tiene titulares "
              "(<h2> o <h3>).")
        return

    primeros = titulares[0:CANTIDAD_TITULARES]
    mostrar_titulares(primeros, len(titulares))

    if preguntar_si_guardar():
        guardar_titulares(primeros, ARCHIVO_SALIDA)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma cancelado por el usuario.")
