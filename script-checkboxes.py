from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()

chrome_driver.get("https://the-internet.herokuapp.com/checkboxes")

input_element = chrome_driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')

input_element.click()

sleep(6)