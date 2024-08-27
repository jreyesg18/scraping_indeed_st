import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Título de la app en Streamlit
st.title('Scraping de Ofertas de Trabajo en Indeed')

# Solicitar al usuario que seleccione el navegador
navegador = st.selectbox("Seleccione el navegador que desea utilizar:", ["Chrome", "Firefox"])

# Campos de entrada en Streamlit para la URL y las palabras clave
Pagina_Url = st.text_input("Ingrese URL de la página de empleos:", "https://cl.indeed.com/")
Palabra_clave = st.text_input("Ingrese palabras clave separadas por comas (ej: Analista,Desarrollador):")

# Convertir las palabras clave en una lista
Palabra_clave = [keyword.strip() for keyword in Palabra_clave.split(',')]

# Botón para iniciar el scraping
if st.button('Iniciar Scraping'):
    driver = None

    # Condicional para seleccionar el driver basado en el navegador
    if navegador == "Chrome":
        driver = webdriver.Chrome()
    elif navegador == "Firefox":
        driver = webdriver.Firefox()

    driver.get(Pagina_Url)

    while True:
        # Intentar encontrar y cerrar el popup si aparece
        try:
            close_button = driver.find_element(By.CSS_SELECTOR, "div[aria-modal='true'] button[aria-label='cerrar']")
            close_button.click()
            time.sleep(1)  # Espera un momento para asegurarse de que el popup se haya cerrado
        except:
            pass  # Si el popup no aparece, continua con el scraping

        # Encuentra todos los elementos que coinciden con la clase especificada
        ofertas = driver.find_elements(By.CLASS_NAME, "css-zu9cdh.eu4oa1w0")

        # Itera sobre cada oferta y extrae el texto
        for oferta in ofertas:
            job_title_element = oferta.find_element(By.CSS_SELECTOR, "h2.jobTitle a")
            job_title = job_title_element.text
            job_link = job_title_element.get_attribute("href")

            if any(keyword.upper() in job_title.upper() for keyword in Palabra_clave):
                st.write(f"**Job Title:** {job_title}")
                st.write(f"[Link]({job_link})\n")

        # Intentar encontrar el botón de "Next Page"
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='pagination-page-next']")
            next_button.click()
            time.sleep(3)  # Esperar unos segundos para que la página cargue
        except:
            st.write("No more pages")
            break

    driver.quit()

