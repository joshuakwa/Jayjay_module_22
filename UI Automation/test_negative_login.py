import time

from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_negative_login():
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
    driver.find_element(By.ID, "password").send_keys("asdasd")
    driver.find_element(By.ID, "login-button").click()
    error_msg = driver.find_element(By.XPATH, "//h3").text
    assert_that(error_msg).is_equal_to("Epic sadface: Username and password do not match any user in this service")

    time.sleep(2)
    driver.quit()
