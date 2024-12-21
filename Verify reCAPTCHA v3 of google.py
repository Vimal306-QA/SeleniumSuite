from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# Configure browser options
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Enable headless mode
# options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
options.add_argument("--start-maximized")

# Initialize the browser
driver = webdriver.Chrome(options=options)

for _ in range(20):
    driver.get("https://2captcha.com/demo/recaptcha-v3")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    time.sleep(2)
    # msg = driver.find_element(By.XPATH, "//p[@class='_successMessage_mbkq7_1']").text
    # print(msg)
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//button[normalize-space()='Reset']").click()



# try:
#     # Open Google
#     driver.get("https://2captcha.com/demo/recaptcha-v3")
#     time.sleep(2)  # Initial delay for loading
#
#     # Perform aggressive searches in a loop
#     for i in range(100):  # Increase to 100 searches
#         print(f"Performing search {i + 1}...")
#
#         # Locate the search box
#         button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
#         button.click()
#         msg = driver.find_element(By.CSS_SELECTOR,"._successMessage_mbkq7_1").text
#         print(msg)
#         driver.find_element(By.XPATH,"//button[normalize-space()='Reset']").click()
#
#         # Minimal delay between searches to mimic high-frequency activity
#         time.sleep(2)
#
#         # Check for CAPTCHA or verification page
#         if "sorry" in driver.current_url or "captcha" in driver.page_source.lower():
#             print("CAPTCHA triggered!")
#
#             # Save a screenshot and page source for debugging
#             os.makedirs("logs", exist_ok=True)
#             driver.save_screenshot(f"logs/captcha_triggered_{i + 1}.png")
#             with open(f"logs/captcha_page_{i + 1}.html", "w", encoding="utf-8") as f:
#                 f.write(driver.page_source)
#             break
#         else:
#             print("Search successful.")
#
# finally:
#     # Close the browser
#     driver.quit()
#
# print("Test completed.")
