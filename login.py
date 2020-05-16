from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep 
from info import getInfo

def userLogin(driver):
    username = driver.find_element_by_name('username')
    user_name, pass_word = getInfo()
    username.send_keys(user_name)
    password = driver.find_element_by_name('password')
    password.send_keys(pass_word)

    login = driver.find_element_by_name('login')
    login.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "golinks"))
        )
    except:
        print("error.................")

    