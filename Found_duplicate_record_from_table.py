"""Found duplicate records from the table there are multiple page and print that records"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize the browser
driver = webdriver.Chrome(options=options)

# URL of the webpage
url = "https://customizeyourfood.com/admin"
driver.get(url)

# Login
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("acecard.club@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Admin@123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

# Navigate to Transaction Histories
driver.get("https://customizeyourfood.com/admin/transaction-histories")
time.sleep(5)

# XPath definitions
next_page_button_xpath = "(//a[@href='#'])[11]"  # Update with your actual next button XPath
table_xpath = "//table[@id='TransactionHistoryDataTable']/tbody/tr"

# Dictionary to track User Detail and Receipt combinations
transaction_records = {}
matching_records = []
non_matching_records = []

# Function to process the table on the current page
def process_table():
    rows = driver.find_elements(By.XPATH, table_xpath)
    for row in rows:
        try:
            # Extract relevant data
            user_detail = row.find_element(By.XPATH, ".//td[3]").text.strip()
            receipt = row.find_element(By.XPATH, ".//td[4]").text.strip()
            transaction_type = row.find_element(By.XPATH, ".//td[12]").text.strip()  # Credit or Debit

            # Combine User Detail and Receipt as a key
            key = (user_detail, receipt)

            # Check if this combination exists
            if key in transaction_records:
                # Compare transaction types
                first_type = transaction_records[key]
                if first_type == transaction_type:
                    matching_records.append((key, first_type, transaction_type))
                else:
                    non_matching_records.append((key, first_type, transaction_type))
            else:
                # Add to the dictionary
                transaction_records[key] = transaction_type

        except Exception as e:
            print(f"Error processing row: {e}")

# Process all pages
total_pages = 40  # Define the total number of pages
page = 1
while page <= total_pages:
    print(f"Processing page {page}...")
    process_table()
    try:
        # Click the next page button
        next_button = driver.find_element(By.XPATH, next_page_button_xpath)
        next_button.click()
        time.sleep(2)  # Wait for the next page to load
        page += 1
    except Exception as e:
        print(f"Error navigating to the next page: {e}")
        break

# Print results at the end
if matching_records:
    print(f"\nMatching Records - {len(matching_records)} found:\n")
    for i, (key, first_type, second_type) in enumerate(matching_records, start=1):
        print(f"Matching Record {i}:")
        print(f"  User Detail    : {key[0]}")
        print(f"  Receipt        : {key[1]}")
        print(f"  First Record   : Transaction Type: {first_type}")
        print(f"  Second Record  : Transaction Type: {second_type}")
        print("-" * 40)

if non_matching_records:
    print(f"\nNon-Matching Records - {len(non_matching_records)} found:\n")
    for i, (key, first_type, second_type) in enumerate(non_matching_records, start=1):
        print(f"Non-Matching Record {i}:")
        print(f"  User Detail    : {key[0]}")
        print(f"  Receipt        : {key[1]}")
        print(f"  First Record   : Transaction Type: {first_type}")
        print(f"  Second Record  : Transaction Type: {second_type}")
        print("-" * 40)

if not matching_records and not non_matching_records:
    print("\nNo records found.")
else:
    print("\nEnd of processing.")

# Close the WebDriver
driver.quit()
