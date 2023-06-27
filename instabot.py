from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def follow_people(username, password, count):
    driver = webdriver.Chrome("path/to/chromedriver")  
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    time.sleep(4)


    save_info_btn = driver.find_element(By.XPATH, "//button[text()='Not Now']")
    save_info_btn.click()
    time.sleep(2)

    
    user_to_follow = "username_of_the_user" 
    driver.get(f"https://www.instagram.com/{user_to_follow}/followers/")
    time.sleep(2)

    
    follow_btns = driver.find_elements(By.XPATH, "//button[text()='Follow']")
    for btn in follow_btns[:count]:
        btn.click()
        time.sleep(1)

    
    driver.quit()


follow_people('your_username', 'your_password', 100)

