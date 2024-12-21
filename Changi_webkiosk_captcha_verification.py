import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Define Chrome options and desired capabilities
chrome_options = Options()
caps = DesiredCapabilities.CHROME
caps["goog:loggingPrefs"] = {"performance": "ALL"}

# Merge capabilities into Chrome options
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

# Set up ChromeDriver
driver_path = "C:\\Users\\Hipster\\Documents\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# Open the website

for _ in range(1):
    driver.get("https://web-development-vcea.voncierge.tech/")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
    time.sleep(2)

logs = driver.get_log("performance")
for log in logs:
    message = json.loads(log["message"])  # Convert log message to JSON
    network_log = message["message"]
    if network_log["method"].startswith("Network."):
        print(json.dumps(network_log, indent=2))

driver.quit()
