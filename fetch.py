from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

driver = webdriver.Chrome()

# Base URL
base_url = "https://results.eci.gov.in/PcResultGenJune2024/statewiseS"

# Initialize an empty DataFrame to store all the data
all_data = pd.DataFrame()

# Loop through each state (assuming 1 to 24) and each page (assuming max 4 pages per state)
for state_num in range(1, 25):
    for page_num in range(1, 5):
        # Construct the URL for the specific state and page
        state_str = f"{state_num:02}"  # Zero-padded state number
        url = f"{base_url}{state_str}{page_num}.htm"
        
        # Open the URL
        driver.get(url)
        time.sleep(2)  # Allow time for the page to load
        
        try:
            # Locate the table
            table = driver.find_element(By.CLASS_NAME, "table-responsive")
            
            # Read the HTML table into a DataFrame
            df = pd.read_html(table.get_attribute('outerHTML'))[0]
            
            # Add the state and page information
            df['State'] = state_num
            df['Page'] = page_num
            
            # Append the data to the main DataFrame
            all_data = pd.concat([all_data, df], ignore_index=True)
        except Exception as e:
            print(f"Failed to process {url}: {e}")

# Close the WebDriver
driver.quit()

# Drop unnecessary columns or duplicates if needed
all_data.drop_duplicates(inplace=True)

# Save the combined DataFrame to a CSV file
all_data.to_csv('../data/win_margins_2024.csv', index=False)
