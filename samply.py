from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Path to your ChromeDriver executable
driver_path = '/usr/local/bin/chromedriver'  # Ensure this path is correct

# Path to the Chrome binary
chrome_binary_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'  # Update this path if necessary

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# Set up the WebDriver service
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the webpage
url = 'https://careers.adobe.com/us/en/apply?jobSeqNo=ADOBUSR146367EXTERNALENUS&utm_medium=phenom-feeds&source=LinkedIn&utm_source=linkedin&step=1'

# Open the webpage
driver.get(url)

# Implicit Wait
driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to be available

try:
    # Accept all cookies if the button or modal is present
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'primary-button')]//ppc-content[contains(text(), 'Allow')]"))
        )
        accept_cookies_button.click()
        print("Cookies accepted")
    except Exception as e:
        print(f"No cookies button found or unable to click: {e}")

    # Wait for the "Upload Resume" button and ensure it's clickable
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='upload-resume-btn btn primary-button']"))
    )

    # Handle any potential overlays
    # try:
    #     overlay = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, 'overlaybg'))
    #     )
    #     if overlay.is_displayed():
    #         print("Overlay detected. Waiting for it to disappear.")
    #         WebDriverWait(driver, 20).until(
    #             EC.invisibility_of_element_located((By.CLASS_NAME, 'overlaybg'))
    #         )
    # except:
    #     print("No overlay detected or overlay has disappeared.")

    # Scroll to the "Upload Resume" button to ensure it's in view
    upload_button = driver.find_element(By.XPATH, "//button[@class='upload-resume-btn btn primary-button']")
    driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)

    # Click the "Upload Resume" button using JavaScript if necessary
    driver.execute_script("arguments[0].click();", upload_button)

    # Wait for the file input element to be visible and interactable
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )

    # Path to your resume file
    resume_file_path = '/Users/syedamim/Desktop/Syed_Amim_Resume.pdf'  # Replace with the path to your resume file
    # Ensure the file path is absolute
    absolute_resume_file_path = os.path.abspath(resume_file_path)
    
    # Input the file path to the file input element
    file_input.send_keys(absolute_resume_file_path)

    print("Resume uploaded successfully")

    # Handle the JavaScript alert
    try:
        WebDriverWait(driver, 10).until(
            EC.alert_is_present()
        )
        alert = driver.switch_to.alert
        alert.accept()
        print("Alert accepted")
    except Exception as e:
        print(f"No alert found or unable to accept: {e}")

    # Add the value "Kondapur" to the address field
    address_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cntryFields.addressLine1"))
    )
    address_field.send_keys("Kondapur")
    
    city_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cntryFields.city"))
    )
    city_field.send_keys("Hyderabad")
    
    postal_code = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cntryFields.postalCode"))
    )
    postal_code.send_keys("500084")
    
    select_state = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "cntryFields.region"))
    )
    select_state.send_keys("Telangana")
    
    select_deviceType = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "deviceType"))
    )
    select_deviceType.send_keys("Mobile")

    # Handle the checkbox to indicate prior worker status
    prev_worker_checkbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "candidateSelfIdentifyAsPriorWorker.false"))
    )
    if not prev_worker_checkbox.is_selected():
        prev_worker_checkbox.click()
        print("Prior worker checkbox selected")

    # Handle the checkbox for email agreement
    email_agreement_checkbox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "emailAgreement"))
    )
    if not email_agreement_checkbox.is_selected():
        email_agreement_checkbox.click()
        print("Email agreement checkbox selected")
    
    next_1 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "next"))
    )
    next_1.click()
    time.sleep(10)


finally:
    # Time-based wait
    time.sleep(20)  # Wait for 20 seconds to observe the result before closing the browser

    # Close the browser
    driver.quit()
