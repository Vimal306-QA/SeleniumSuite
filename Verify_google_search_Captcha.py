from selenium import webdriver
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

try:
    # Open Google
    driver.get("https://www.google.com")
    time.sleep(2)  # Initial delay for loading

    # Perform aggressive searches in a loop
    for i in range(100):  # Increase to 100 searches
        print(f"Performing search {i + 1}...")

        # Locate the search box
        search_box = driver.find_element("name", "q")
        search_box.clear()
        search_box.send_keys("same search query")  # Repeated query to simulate bot behavior
        search_box.send_keys(Keys.RETURN)

        # Minimal delay between searches to mimic high-frequency activity
        time.sleep(2)

        # Check for CAPTCHA or verification page
        if "sorry" in driver.current_url or "captcha" in driver.page_source.lower():
            print("CAPTCHA triggered!")

            # Save a screenshot and page source for debugging
            os.makedirs("logs", exist_ok=True)
            driver.save_screenshot(f"logs/captcha_triggered_{i + 1}.png")
            with open(f"logs/captcha_page_{i + 1}.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            break
        else:
            print("Search successful.")

finally:
    # Close the browser
    driver.quit()

print("Test completed.")
