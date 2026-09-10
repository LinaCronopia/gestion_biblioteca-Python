# Sistema de gestión de biblioteca

Proyecto final de práctica desarrollado durante mi formación inicial en programación con Python. El objetivo fue aplicar conceptos básicos de programación orientada a objetos mediante un sistema de consola para gestionar usuarios, libros y préstamos de una biblioteca.

## Funcionalidades

- Registrar usuarios.
- Registrar libros de prosa o poesía.
- Registrar préstamos de uno o más libros.
- Mostrar la información de los usuarios.
- Mostrar la información y las características de los libros.

## Conceptos aplicados

- Clases y objetos.
- Herencia.
- Encapsulamiento de datos y comportamientos.
- Composición entre objetos.
- Listas y estructuras de control.
- Interfaz interactiva mediante consola.

## Estructura

```text
gestion_biblioteca-Python/
├── clases/
│   ├── __init__.py
│   ├── inventario.py
│   ├── libro.py
│   ├── prestamo.py
│   └── usuario.py
├── .gitignore
├── README.md
└── main.py
```

## Ejecución

Se requiere Python 3 y no es necesario instalar dependencias externas.

```bash
python main.py
```

El programa muestra un menú desde el cual se pueden registrar usuarios y libros, realizar préstamos y consultar la información cargada durante la ejecución.

## Alcance

Este repositorio conserva un proyecto correspondiente a una etapa inicial de aprendizaje. Los datos se almacenan temporalmente en memoria y se pierden al cerrar el programa. Una posible ampliación sería incorporar persistencia de datos y controles adicionales sobre el inventario.
