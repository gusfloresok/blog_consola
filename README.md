# Blog por consola

Sistema de blog por consola hecho en Python. Permite ver todos los posts, buscar por título, filtrar por tag y validar la estructura de los posts.

## Cómo ejecutarlo

Desde la carpeta `blog_consola/`, ejecutar:

```
python main.py
```

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Qué hace cada archivo

- `main.py`: archivo principal que se ejecuta. Importa las funciones del paquete `blog` y maneja el flujo del menú.
- `blog/__init__.py`: permite que Python reconozca la carpeta `blog` como un paquete.
- `blog/datos.py`: contiene los datos del blog (autor, estados, etiquetas y posts).
- `blog/menu.py`: muestra el menú y retorna la opción elegida por el usuario.
- `blog/operaciones.py`: funciones para listar posts, buscar por título y filtrar por tag.
- `blog/validaciones.py`: función para validar que cada post tenga la estructura correcta.
