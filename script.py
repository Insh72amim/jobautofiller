from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless mode

# Set up WebDriver
service = Service(executable_path="/Users/syedamim/Downloads/chromedriver-mac-arm64/chromedriver")  # Update path
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the webpage
    driver.get(
        "https://careers.adobe.com/us/en/apply?jobSeqNo=ADOBUSR146367EXTERNALENUS&utm_medium=phenom-feeds&source=LinkedIn&utm_source=linkedin&step=1"
    )  # Update with your URL

    # Wait for the button to be clickable
    wait = WebDriverWait(driver, 10)
    button = wait.until(
        EC.element_to_be_clickable((By.ID, "next"))
    )  # Update with button's ID

    # Click the button
    button.click()
    print("Button clicked!")

    # Optionally, wait for a response or perform further actions
    time.sleep(5)  # Wait for 5 seconds for demonstration

finally:
    driver.quit()
