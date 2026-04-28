"""
Archivo de configuración para la conexión a la base de datos MySQL.
Contiene los parámetros necesarios para establecer la conexión con el refugio de animales.
"""

# ============================================
# CONFIGURACIÓN DE LA BASE DE DATOS
# ============================================

# Host del servidor MySQL
# - "localhost" para servidor local
# - IP o dominio para servidor remoto
DB_HOST = "localhost"

# Puerto de conexión de MySQL
# - 3306 es el puerto por defecto de MySQL
# - Cambiar si se usa un puerto diferente
DB_PORT = 3306

# Usuario de la base de datos
# - "root" es el usuario administrador por defecto
# - Recomendación: crear un usuario específico para la aplicación
DB_USER = "root"

# Contraseña del usuario de la base de datos
# - En producción, usar variables de entorno para mayor seguridad
DB_PASSWORD = "root"

# Nombre de la base de datos
# - Debe coincidir con el nombre creado en MySQL
DB_NAME = "refugio_animales"

# ============================================
# CONFIGURACIÓN OPCIONAL ADICIONAL
# ============================================

# Si se desea agregar más configuración en el futuro:
# - CHARSET = "utf8mb4"  # Codificación de caracteres
# - CONNECTION_TIMEOUT = 10  # Timeout en segundos
# - POOL_SIZE = 5  # Tamaño del pool de conexiones

# ============================================
# NOTAS DE SEGURIDAD
# ============================================
# ⚠️ IMPORTANTE:
# 1. No subir este archivo a repositorios públicos (agregar a .gitignore)
# 2. En producción, usar variables de entorno para contraseñas
# 3. Crear un usuario específico para la app (no root)
# 
# Ejemplo de creación de usuario dedicado en MySQL:
# CREATE USER 'app_refugio'@'localhost' IDENTIFIED BY 'contraseña_segura';
# GRANT SELECT, INSERT, UPDATE, DELETE ON refugio_animales.* TO 'app_refugio'@'localhost';
# FLUSH PRIVILEGES;
