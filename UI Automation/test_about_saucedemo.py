import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from assertpy import assert_that


def test_about_saucedemo():
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
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "about_sidebar_link").click()
    current_link = driver.current_url
    assert_that(current_link).is_equal_to("https://saucelabs.com/")

    time.sleep(3)
    driver.quit()
