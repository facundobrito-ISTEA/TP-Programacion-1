# Extractor de titulares

Programa de consola en Python que descarga una página web, extrae sus
titulares (etiquetas `<h2>` y `<h3>`), muestra los primeros 10 numerados y,
si el usuario quiere, los guarda en un archivo de texto.

Proyecto del Ejercicio Avanzado 3 de Programación 1 (Unidad 11).

## Qué hace

1. Pide la URL de un sitio de noticias (si se aprieta Enter usa una por
   defecto).
2. Descarga el HTML de la página con `requests`.
3. Extrae los titulares con `beautifulsoup4`.
4. Muestra por pantalla los primeros 10, numerados.
5. Pregunta si se quieren guardar en `titulares.txt`.

El programa maneja errores con `try / except`: URL inválida, sin conexión,
timeout, error del servidor, página sin titulares y problemas al guardar el
archivo.

## Requisitos

- Python 3.9 o superior
- Librerías de terceros (se instalan con pip):
  - `requests`
  - `beautifulsoup4`

## Instalación

Desde la carpeta del proyecto:

1. Crear el entorno virtual:

   ```
   python -m venv .venv
   ```

2. Activarlo:

   - Windows: `.venv\Scripts\activate`
   - Linux / Mac: `source .venv/bin/activate`

   Si PowerShell bloquea el script, ejecutar una vez:
   `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

3. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

## Uso

Con el entorno virtual activado:

```
python main.py
```

Ejemplo de ejecución:

```
=== Extractor de titulares ===
URL del sitio (Enter para usar https://www.bbc.com/mundo):

Descargando https://www.bbc.com/mundo ...

Se muestran 10 de 25 titulares:

1. Primer titular
2. Segundo titular
...

¿Querés guardar los titulares en un archivo? (s/n): s
Titulares guardados en 'titulares.txt'.
```

Para salir del entorno virtual: `deactivate`.

## Estructura del proyecto

```
extractor_titulares/
├── .venv/               (entorno virtual, no se sube a Git)
├── .gitignore
├── README.md
├── requirements.txt     (dependencias congeladas)
├── main.py              (punto de entrada: interacción con el usuario)
└── extractor.py         (módulo propio: descarga, extracción y guardado)
```

## Integrantes

- Facundo Brito
