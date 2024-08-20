# main.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep as wait
from gui import create_gui

def login_via_gmail(driver, login, passwd):
    driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]").click()
    wait(4)

    driver.switch_to.window(driver.window_handles[1])

    driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(login)
    wait(1)

    driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span").click()
    wait(3)
    
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(passwd)
    wait(1)

    driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span").click()
    wait(3)

    driver.find_element(By.XPATH, value="/html/body/div/div[1]/div/div/main/div[3]/div[1]").click()

def login_via_facebook(driver, login, passwd):
    driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button").click()
    wait(4)
    
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]").click()
    wait(4)
    
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/form/div/div[1]/div/input").send_keys(login)
    wait(4)
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/form/div/div[2]/div/input").send_keys(passwd)
    wait(4)
    driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/form/div/div[3]/label[2]/input").click()
    wait(8)
    
    driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div").click()

def login_via_phone_num(driver, login, passwd):
    pass  # Still figuring out how to handle this

def main():
    platform, login, passwd, submitted = create_gui()

    if not submitted:
        exit(1)

    driver = webdriver.Chrome()  # You can also use Firefox()
    driver.get("https://tinder.com/")
    wait(5)

    # Sign in
    driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div").click()
    wait(4)

    match platform.lower():
        case "google":
            login_via_gmail(driver, login, passwd)
        case "facebook":
            login_via_facebook(driver, login, passwd)
        case "phone":
            login_via_phone_num(driver, login, passwd)
        case _:
            print("Error with chosen platform.")

    wait(8)
    driver.switch_to.window(driver.window_handles[0])

    # Welcome on Tinder
    driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]").click()
    wait(4)
    driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]").click()
    wait(8)

    # Scroll right
    content = driver.find_element(By.CSS_SELECTOR, value="body")
    while True:
        wait(2)
        content.send_keys(Keys.ARROW_RIGHT)

if __name__ == "__main__":
    main()
