#!/usr/bin/env python3
"""Demo: Python scraper and automation bot for Upwork-like listings."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_demo_scraper() -> None:
    """Scrapes job titles from a mock job listing page and prints them."""

    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chromium-browser"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #driver = webdriver.Chrome(options=chrome_options)

    try:
        # Example: scrape from a job listing website (replace with target URL)
        driver.get("https://remoteok.com/remote-dev-jobs")
        time.sleep(2)  # Wait for page to load

        job_cards = driver.find_elements(By.CSS_SELECTOR, "td.position h2")
        print("Jobs Found:")
        for job in job_cards[:5]:  # Limit to first 5
            print(" -", job.text.strip())
    finally:
        driver.quit()

if __name__ == "__main__":
    run_demo_scraper()
