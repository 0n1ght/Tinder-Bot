from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep as wait
from sys import argv, exit


if len(argv) != 4:
     print("Tu run the script, use this pattern: python3 <way_of_login> <login> <password>\nwhere \"way_of_login\" can be google/facebook/phone")
     exit(0)

# run internet browser
driver = webdriver.Chrome() # you can also use Firefox()
driver.get("https://tinder.com/")
wait(5)

# 3 ways of login

def login_via_gmail():

    login_bt = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]")
    login_bt.click()
    wait(4)

    google_login_window = driver.window_handles[1]
    driver.switch_to.window(google_login_window)

    email_input = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    email_input.send_keys(argv[2])
    wait(1)

    email_confirm = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span")
    email_confirm.click()
    wait(3)
    
    passwd_input = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    passwd_input.send_keys(argv[3])
    wait(1)

    passwd_confirm = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span")
    passwd_confirm .click()
    wait(3)

    confirm_bt = driver.find_element(By.XPATH, value="/html/body/div/div[1]/div/div/main/div[3]/div[1]")
    confirm_bt.click()


def login_via_facebook():

    login_bt = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
    login_bt.click()
    wait(4)
    
    facebook_login_window = driver.window_handles[1]
    driver.switch_to.window(facebook_login_window)
    accept_cookies = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]")
    accept_cookies.click()
    wait(4)
    
    login_fb_input = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/form/div/div[1]/div/input")
    login_fb_input.send_keys(argv[2])
    wait(4)
    pass_fb_input = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/form/div/div[2]/div/input")
    pass_fb_input.send_keys(argv[3])
    wait(4)
    login_fb_bt = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/form/div/div[3]/label[2]/input")
    login_fb_bt.click()
    wait(8)
    
    continue_fb_bt = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div[1]/div")
    continue_fb_bt.click()


def login_via_phone_num():
    pass # currently there is antibot


# login
login_bt = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div")
login_bt.click()
wait(4)

match(argv[1]):
    case "facebook":
        login_via_facebook()
    case "phone":
            login_via_phone_num()
    case _:
        login_via_gmail()

wait(8)
driver.switch_to.window(driver.window_handles[0])

# welcome on Tinder
# skip pop-ups
allow_location_tinder = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]")
allow_location_tinder.click()
wait(4)
nonotify_location_tinder = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]")
nonotify_location_tinder.click()
wait(8)

# scroll right
content = (driver.find_element(By.CSS_SELECTOR, value="body"))
while True:
    wait(2)
    content.send_keys(Keys.ARROW_RIGHT)