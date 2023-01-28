from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
options = Options()
options.headless = True
url = "https://selenium-python.readthedocs.io/"
options.add_argument("--window-size=1920,1200")
DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(url)
print(driver.page_source)
driver.quit()