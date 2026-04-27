# Actividad Evaluable UD 6 – Lectura y escritura de información

## Aplicación Refugio de Animales

Aplicación en Python para gestionar los animales de un refugio usando patrón MVC y acceso a base de datos MYSQL.
La aplicación debe permitir consultas, inserciones, modificaciones, borrado y exportación a CSV.

## Script de Base de Datos

```'sql
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS refugio_animales;
USE refugio_animales;

-- Crear la tabla de animales
CREATE TABLE IF NOT EXISTS animales (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
especie VARCHAR(30) NOT NULL,
edad INT,
adoptado BOOLEAN
);

-- Insertar algunos registros
INSERT INTO animales (nombre, especie, edad, adoptado) VALUES
('Alvin', 'Perro', 3, FALSE),
('Dexter', 'Gato', 2, FALSE),
('Coco', 'Conejo', 1, FALSE),
('Rocky', 'Perro', 5, TRUE),
('Nala', 'Gato', 4, FALSE);
```

## Estructura de Carpetas

Entregable6
├── main.py                 # Programa principal de ejecución
├── config.py               # Contiene la configuracion para la conexion a BBDD Mysql
├── conexion.py             # Clase para la conexion con BBDD Mysql
├── Models/
│ ├── Animal.py             # Clase enum para tipos de combustible de centrales termicas
│ └── AnimalModel.py        # Clase enum para tipos de material fisil de centrales nucleares
├── Views/
│ └── AnimalView.py         # Clase enum para tipos de combustible de centrales termicas
├── Controllers/
│ └── AnimalController.py   # Clase abstracta central
└── Utilities/
  └── Utilities.py          # Utilidades para validacion

## Funcionalidades

- Listar todos los animales
- Buscar animales por especie
- Agregar un nuevo animal
- Adoptar un animal
- Eliminar un animal
- Guardar animales en un archivo CSV

## Tecnologías

- Python 3.14.4
- Programación Orientada a Objetos
- Manejo de excepciones
- Acceso a base de datos MYSQL
- Exportació a archivo .CSV
- Uso de emojis: https://emojikeyboard.top/es/