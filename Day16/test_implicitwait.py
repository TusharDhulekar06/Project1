from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Test_implicit:
    def test_implicit(self):
        service=ChromeService(executable_path=ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)

        driver.get("https://www.haldirams.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

        sweet=driver.find_element(By.XPATH,"//input[@id='search']")
        sweet.send_keys("Namkeen")
        sweet.submit()