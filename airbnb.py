from time import sleep  # Importa la función sleep para pausas

from selenium import webdriver  # Importa Selenium para control del navegador
from selenium.webdriver.common.by import By  # Importa By para localización de elementos
from selenium.webdriver.chrome.options import Options  # Importa Options para configurar Chrome
from selenium.webdriver.chrome.service import Service  # Importa Service para manejar el servicio de Chrome

from webdriver_manager.chrome import ChromeDriverManager  # Importa ChromeDriverManager para manejar el driver de Chrome

opts = Options()  # Crea una instancia de opciones de Chrome

# Configuración de user agent:
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")  # Añade un user agent específico

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),  # Instala y usa el driver de Chrome
    options=opts  # Aplica las opciones configuradas
)

driver.get("https://www.airbnb.com.pe/")  # Abre la página web de Airbnb

sleep(3)  # Espera 3 segundos para asegurar que la página cargue

titulos = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')  # Encuentra los elementos de título de los listados
for titulo in titulos:  # Itera sobre los títulos encontrados
    print(titulo.text)  # Imprime el texto de cada título

driver.quit()  # Cierra el navegador
