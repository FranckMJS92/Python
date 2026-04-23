# Actividad Evaluable UD 5 – Programación Orientada a Objetos

## Aplicación de Gestión de Producción Eléctrica

Aplicación en Python para gestionar la producción eléctrica generada por centrales térmicas y nucleares.

## Estructura de Carpetas

Entregable5
├── main.py                     # Programa principal de ejecución
├── Classes/
│   ├── Central.py              # Clase abstracta central
│   ├── CentralTermica.py       # Clase para Central termica
│   ├── CentralNuclear.py       # Clase para Central nuclear
│   └── ParqueGeneracion.py     # Clase para colección de centrales
├── Enums/
│   ├── Combustible.py          # Clase enum para tipos de combustible de centrales termicas
│   └── MaterialFisil.py        # Clase enum para tipos de material fisil de centrales nucleares
└── Utilities/
    └── Utilities.py            # Utilidades para validacion


## Funcionalidades

- Añadir nuevas centrales (térmicas o nucleares)
- Mostrar todas las centrales
- Obtener producción eléctrica total
- Obtener producción solo de centrales térmicas
- Obtener producción solo de centrales nucleares
- Buscar producción por nombre de central
- Contar centrales térmicas por tipo de combustible
- Mostrar central con mayor producción

## Tecnologías

- Python 3.14.4
- Programación Orientada a Objetos
- Herencia y abstracción
- Enumerados (Enum)
- Manejo de excepciones
- Uso de emojis: https://emojikeyboard.top/es/