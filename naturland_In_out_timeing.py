from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Credentials & URLs
USERNAME = "admin@hipster-inc.com"
PASSWORD = "qw21QW@!"
LOGIN_URL = "https://natureland.hipster-dev.com/login"
LISTING_URL = "https://natureland.hipster-dev.com/admin/staffs"

# Start WebDriver
driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()

# Step 1: Login
driver.get(LOGIN_URL)
time.sleep(3)

driver.find_element(By.NAME, "email").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
time.sleep(5)  # Wait for login

# Step 2: Navigate to Employee Listing Page
driver.get(LISTING_URL)
time.sleep(3)

# Step 3: Process All Pages
while True:
    print("Processing a new page...")

    # Find All "Edit" Buttons on the Current Page
    edit_buttons = driver.find_elements(By.XPATH, "//a[contains(@href, '/admin/staffs/') and contains(@href, '/edit')]")

    for index in range(len(edit_buttons)):
        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", edit_buttons[index])
        time.sleep(1)

        # Wait until the element is clickable
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, '/admin/staffs/') and contains(@href, '/edit')]")))

        # Click using JavaScript to avoid overlay issues
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)

        # # Define check-in and check-out times
        # check_in_time = "07:00"
        # check_out_time = "23:30"
        #
        # # Update times for all days
        # days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        # for day in days:
        #     try:
        #         checkin_field = driver.find_element(By.XPATH, f"//input[@name='{day}_checkin']")
        #         checkout_field = driver.find_element(By.XPATH, f"//input[@name='{day}_checkout']")
        #
        #         checkin_field.clear()
        #         checkin_field.send_keys(check_in_time)
        #         checkout_field.clear()
        #         checkout_field.send_keys(check_out_time)
        #     except:
        #         print(f"Skipping {day} field (not found).")
        #
        # # Click Save
        # driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
        # time.sleep(2)

        # Go back to the listing page
        driver.get(LISTING_URL)
        time.sleep(3)

    # Step 4: Click "Next" Button if Available
    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
    except:
        print("No more pages found. Process complete.")
        break  # Exit loop when no more pages

# Step 5: Close Browser
print("All employees updated successfully!")
driver.quit()
