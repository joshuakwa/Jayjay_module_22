import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_remove_from_cart():
    o = Options()
    o.add_argument("--headless")
    o.add_argument("--start-maximized")
    o.add_argument("--no-sandbox")
    o.add_argument("--ignore-certificate-errors")
    o.add_argument("--disable-gpu")
    o.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=o)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").is_displayed()
    driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").is_displayed()

    time.sleep(3)
    driver.quit()
