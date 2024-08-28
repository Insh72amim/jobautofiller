import warnings
from urllib3.exceptions import InsecureRequestWarning

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os

JobUrl = "https://careers.adobe.com/us/en/job/ADOBUSR146370EXTERNALENUS/Software-Development-Engineer?utm_medium=phenom-feeds&source=LinkedIn&utm_source=linkedin"

MYDETAILS = {
    "JobUrl": JobUrl,
    "name": "Syed Amim",
    "email": "amim.insherah@gmail.com",
    "phone": "8228894267",
    "country": "India",
    "city": "Hyderabad",
    "state": "Telangana",
    "zip": "500084",
    "address": "Kondapur",
    "linkedin": "https://www.linkedin.com/in/syed-amim",
    "github": "https://github.com/Insh72amim",
    "website": "https://syedamim.netlify.app/",
    "resumePath": "/Users/syedamim/Desktop/Syed_Amim_Resume.pdf",
    "machine": {
        "name": "MacBook Pro",
        "driver_path": "/usr/local/bin/chromedriver",
        "chrome_binary_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    },
}

warnings.filterwarnings("ignore", category=InsecureRequestWarning)

# Path to your ChromeDriver executable
driver_path = MYDETAILS["machine"]["driver_path"]  # Ensure this path is correct

# Path to the Chrome binary
chrome_binary_path = MYDETAILS["machine"][
    "chrome_binary_path"
]  # Update this path if necessary

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# Set up the WebDriver service
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the webpage
url = MYDETAILS["JobUrl"]

# Open the webpage
driver.get(url)

# Implicit Wait
driver.implicitly_wait(5)  # Wait for up to 10 seconds for elements to be available


def accept_cookies():
    try:
        accept_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'btn') and contains(@class, 'primary-button')]//ppc-content[contains(text(), 'Allow')]",
                )
            )
        )
        accept_cookies_button.click()
        print("Cookies accepted")
    except Exception as e:
        print(f"No cookies button found or unable to click: {e}")


def add_form_field_value(field_id, field_value):
    try:
        field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        if field:
            field.send_keys(field_value)
            print(f"Field {field_id} set to {field_value}")
    except Exception as e:
        print(f"Error setting value for field {field_id}: {e}")


def select_checkbox_by_id(checkbox_id):
    try:
        checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, checkbox_id))
        )
        if not checkbox.is_selected():
            checkbox.click()
            print(f"Checkbox {checkbox_id} selected")
    except Exception as e:
        print(f"Error selecting checkbox {checkbox_id}: {e}")


def click_button_by_id(button_id):
    try:
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        button.click()
        print(f"Button {button_id} clicked")
    except Exception as e:
        print(f"Error clicking button {button_id}: {e}")


def click_button_by_text(class_name):
    try:
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, class_name))
        )
        if button:
            button.click()
            print(f"Button with class name {class_name} clicked")
        button_class = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        if button_class:
            button_class.click()
            print(f"Button with class name {class_name} clicked")
    except Exception as e:
        print(f"Error clicking button {class_name}: {e}")


def close_overlay():
    try:
        overlay_close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'close-overlay') or contains(@class, 'overlay-close')]",
                )
            )
        )
        overlay_close_button.click()
        print("Overlay closed")
    except Exception as e:
        print(f"No overlay close button found or unable to click: {e}")


def handle_js_alert():
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Alert accepted")
    except Exception as e:
        print(f"No alert found or unable to accept: {e}")


def select_dropdown_by_id(dropdown_id, value):
    try:
        dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, dropdown_id))
        )
        if dropdown:
            select = Select(dropdown)
            select.select_by_visible_text(value)
            print(f"Dropdown {dropdown_id} selected value {value}")
    except Exception as e:
        print(f"Error selecting dropdown {dropdown_id}: {e}")


try:
    # Accept all cookies if the button or modal is present
    accept_cookies()

    # Handle any potential overlays
    close_overlay()

    # Wait for the "Upload Resume" button and ensure it's clickable
    upload_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='upload-resume-btn btn primary-button']")
        )
    )

    # Scroll to the "Upload Resume" button to ensure it's in view
    driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)

    # Click the "Upload Resume" button using JavaScript if necessary
    driver.execute_script("arguments[0].click();", upload_button)

    # Wait for the file input element to be visible and interactable
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )

    # Ensure the file path is absolute
    absolute_resume_file_path = os.path.abspath(MYDETAILS["resumePath"])

    # Input the file path to the file input element
    file_input.send_keys(absolute_resume_file_path)

    print("Resume uploaded successfully")

    # Handle the JavaScript alert
    handle_js_alert()

    # Page 1
    add_form_field_value("cntryFields.addressLine1", MYDETAILS["address"])
    add_form_field_value("cntryFields.city", MYDETAILS["city"])
    add_form_field_value("cntryFields.postalCode", MYDETAILS["zip"])
    add_form_field_value("cntryFields.region", MYDETAILS["state"])
    add_form_field_value("deviceType", "Mobile")
    select_dropdown_by_id("source", "Social Media")
    time.sleep(2)
    select_dropdown_by_id("applicantSource", "LinkedIn")
    # add_form_field_value("applicationSource", "LinkedIn")
    select_checkbox_by_id("candidateSelfIdentifyAsPriorWorker.false")
    select_checkbox_by_id("emailAgreement")
    click_button_by_id("next")

    # Page 2
    add_form_field_value("experienceData[0].location", MYDETAILS["city"])
    select_dropdown_by_id("educationData[0].degree", "Bachelors")
    # add_form_field_value("educationData[0].fromTo.startDate", "07/2018")
    # add_form_field_value("educationData[0].fromTo.endDate", "05/2022")
    add_form_field_value(
        "socialMediaAccountDataV2[0].socialNetworkAccountURL", MYDETAILS["linkedin"]
    )
    click_button_by_id("array-button-add-websites")
    add_form_field_value("websites[0].website", MYDETAILS["website"])
    click_button_by_id("array-button-add-websites")
    add_form_field_value("websites[1].website", MYDETAILS["github"])
    click_button_by_id("next")

    # Page 3
    select_dropdown_by_id("jsqData.R2_Primary_Questionnaire_External_India.a", "Yes")
    select_checkbox_by_id("jsqData.R2_Primary_Questionnaire_External_India.b_4")
    select_dropdown_by_id("jsqData.R2_Primary_Questionnaire_External_India.c", "Yes")
    select_dropdown_by_id("jsqData.R2_Primary_Questionnaire_External_India.d", "Yes")
    select_dropdown_by_id("jsqData.R2_Primary_Questionnaire_External_India.e", "Yes")
    click_button_by_id("next")

    # Page 4
    select_checkbox_by_id("termConditions_non_us.agreementCheck")
    click_button_by_id("next")

    # Page 5
    click_button_by_text("btn primary-button btn-submit")
    click_button_by_id("submit")
    time.sleep(10)

finally:
    # Time-based wait
    time.sleep(
        20
    )  # Wait for 20 seconds to observe the result before closing the browser

    # Close the browser
    driver.quit()
