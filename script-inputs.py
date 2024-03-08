from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver = webdriver.Chrome()

chrome_driver.get("https://the-internet.herokuapp.com/inputs")

input_element = chrome_driver.find_element(By.TAG_NAME, 'input')

input_element.send_keys("1345" + Keys.ENTER)

sleep(6)