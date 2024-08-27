# Scraping de Ofertas de Trabajo en Indeed

Este proyecto es una aplicación en Streamlit que permite realizar scraping de ofertas de trabajo desde la página web de Indeed. Los resultados se filtran según las palabras clave proporcionadas por el usuario y se muestran en la interfaz de Streamlit.

## Requisitos

- Python 3.x
- Streamlit
- Selenium
- Navegadores WebDriver: Debes tener instalado el WebDriver correspondiente para el navegador que deseas utilizar (Chrome o Firefox).

## Instalación

1. **Clonar el repositorio:**


         git clone https://github.com/usuario/indeed_scraping.git
         cd indeed_scraping

2. **Crear un entorno virtual (opcional, pero recomendado):**


         python -m venv venv
      
         source venv/bin/activate  # macOS/Linux
      
         .\venv\Scripts\activate  # Windows

3. **Instalar las dependencias:**

         pip install streamlit selenium

4. **Descargar el WebDriver:**

- ChromeDriver

- GeckoDriver (Firefox)

Asegúrate de que el WebDriver esté en tu PATH o en el directorio del proyecto.

## Uso

1. **Ejecutar la aplicación:**

       streamlit run main.py
2. **Seleccionar navegador:** En la interfaz de Streamlit, selecciona el navegador que deseas utilizar (Chrome o Firefox).

3. **Ingresar URL y palabras clave:**
- Introduce la URL de la página de empleos de Indeed desde la que deseas extraer ofertas.
- Especifica las palabras clave para filtrar los trabajos (separadas por comas).
4. **Iniciar el scraping:** Haz clic en el botón "Iniciar Scraping" para comenzar el proceso.
5. **Resultados:** Los resultados de las ofertas de trabajo se mostrarán en la interfaz de Streamlit.

## Personalización

- Ajustar palabras clave: Puedes cambiar las palabras clave para buscar diferentes tipos de trabajos.
- Mejorar el scraping: Puedes modificar el código para extraer más detalles de cada oferta, como la empresa, ubicación, o salario.

## Problemas comunes

- WebDriver no encontrado: Asegúrate de que el WebDriver está instalado y accesible en tu sistema.
- Compatibilidad de Selenium: Verifica que la versión de Selenium sea compatible con la versión de tu navegador y WebDriver.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request en el repositorio de GitHub.