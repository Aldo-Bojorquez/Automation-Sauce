# Automatización de la página demo "Sauce Demo"

Este proyecto automatiza la interacción con la página demo de Sauce Labs llamada "Sauce Demo" usando Playwright. La automatización cubre el flujo principal del sitio, incluyendo inicio de sesión, navegación por el catálogo de productos, selección de artículos, gestión del carrito y finalización de la compra.

## ¿Qué automatiza?

- Inicio de sesión con credenciales válidas.
- Validación del acceso al catálogo de productos.
- Agregado de productos al carrito.
- Navegación dentro del carrito.
- Finalización del proceso de compra.
- Verificación del estado final de la compra.

## Tecnologías utilizadas

- Python
- Pytest
- Playwright (Python)
- Visual Studio Code

## Requisitos para ejecutar el proyecto

Antes de correr la automatización, asegúrate de tener instalado lo siguiente en tu computadora:

### Python

Descarga e instala Python desde la página oficial:

- https://www.python.org/downloads/

Verifica la instalación con:

```bash
python --version
```

### 2. Visual Studio Code (recomendado)

Puedes usar cualquier editor de código, pero VS Code es muy útil para trabajar con el proyecto.

- https://code.visualstudio.com/

### 3. Dependencias del proyecto

Dentro de la carpeta del proyecto, instala las dependencias con:

```bash
pip install -r requirements.txt
```

Si el proyecto utiliza Playwright, también debes instalar los navegadores:

```bash
pip install pytest-playwright
```

### 4. Compatibilidad del sistema

El proyecto puede ejecutarse en:

- Windows
- macOS
- Linux

Siempre que tengan instalados Python y las dependencias del proyecto.

## Cómo ejecutar el proyecto

1. Abrir una terminal en la raíz del proyecto.
2. Instalar las dependencias:

```bash
pip install
```

3. Ejecutar la automatización:

```bash
pytest //para ejecución de todos test
pytest test/"Carpeta para test" //para ejecutar los test de carpetas en especifico
```

O en caso de contar con un script específico:

```bash
pytest test/"Carpeta para test"/"Nombre de archivo"
```

## Credenciales de prueba recomendadas

La página demo de Sauce Demo usa estas credenciales por defecto:

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

## Observaciones

- La automatización sirve para validar flujos críticos de compra en un e-commerce demo.
- Se recomienda ejecutar las pruebas en un entorno estable y con conexión a internet.
- Si hay errores con Playwright (Python), revisa que los navegadores estén instalados correctamente.

## Conclusión

La automatización de "Sauce Demo" permite probar de manera rápida y confiable el flujo de compra de una tienda de ejemplo. Con requisitos básicos como Playwright (Python), cualquier computadora con estas herramientas puede ejecutar el proyecto y verificar el comportamiento del sitio.
