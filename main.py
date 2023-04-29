from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
import time

chrome_options = ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-blink-features=AutomationControlled")

service = Service(r"Path to your chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Set an implicit wait for 10 seconds to avoid fixed sleep times
# driver.implicitly_wait(10)

# Find the cookie element on the page
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

# Click the cookie repeatedly for 5 minutes
current_time = time.time()
while time.time() - current_time < 300:
    # Click the cookie once every 5 seconds
    inner_current_time = time.time()
    while time.time() - inner_current_time < 0.5:
        cookie.click()
    
    # Find the largest enabled store item and purchase it
    store = driver.find_element("id","store")
    store_item = store.find_elements('xpath', "*")
    largest_enabled_store_item = None
    for item in store_item:
        if item.get_attribute("class") == "grayed":
            if largest_enabled_store_item is not None:     
                largest_enabled_store_item.click()               
            break
        else:
            largest_enabled_store_item = item 
    
# Print the cookies per second
cookies_per_second = driver.find_element("id", "cps")
print(cookies_per_second.text)

# Wait indefinitely to keep the browser window open
while True:
    pass

# Close the browser window
driver.quit()