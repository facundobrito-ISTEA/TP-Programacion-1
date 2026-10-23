# Extractor de titulares

Programa de consola en Python que descarga una página web, extrae sus
titulares (etiquetas `<h2>` y `<h3>`), muestra los primeros 10 numerados y,
si el usuario quiere, los guarda en un archivo de texto.

Trabajo grupal del Ejercicio Avanzado 3 de Programación 1 (Unidad 11).

## Qué hace

1. Pide la URL de un sitio de noticias. Si se aprieta Enter, usa una por
   defecto; si se escribe sin `://` (por ejemplo `sitio.com`), le agrega
   `https://` al principio.
2. Descarga el HTML de la página con `requests`.
3. Extrae los titulares con `beautifulsoup4`.
4. Muestra por pantalla los primeros 10, numerados.
5. Pregunta si se quieren guardar en `titulares.txt`.

## Manejo de errores

El programa maneja errores con `try / except` y avisa por pantalla sin
cortarse:

- URL inválida
- Sin conexión o sitio inexistente
- Timeout (el sitio tarda más de 10 segundos)
- Error del servidor (404, 500, etc.)
- Página sin titulares
- Problemas al guardar el archivo

## Librerías usadas

- `requests`: descarga el HTML de la página.
- `beautifulsoup4`: analiza el HTML y extrae los titulares.

## Requisitos

- Python 3.9 o superior
- Las librerías de terceros anteriores (se instalan con pip, ver abajo)

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
TP-Programacion-1/
├── .venv/               (entorno virtual, no se sube a Git)
├── .gitignore
├── README.md
├── requirements.txt     (dependencias congeladas)
├── main.py              (punto de entrada: interacción con el usuario)
└── extractor.py         (módulo propio: descarga, extracción y guardado)
```

## Integrantes

- Facundo Brito
- Guido Julian Andino
- Franco Luciano Arias
- Pedro Bardeci
- Sergio Antonio Álvarez
