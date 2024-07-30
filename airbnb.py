from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

opts = Options()

#configuracion de user agent:
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts

)
driver.get("https://www.airbnb.com.pe/")

sleep(3)

titulos = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
for titulo in titulos:
    print(titulo.text)
