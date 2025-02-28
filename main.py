from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Use your actual Chrome profile path
chrome_profile_path = r"C:\Users\Asif Abrar\AppData\Local\Google\Chrome\User Data"

# Set Chrome options to use your existing profile
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")  # Load existing profile
options.add_argument("--profile-directory=Default")  # Use the correct profile name
options.add_argument("--remote-debugging-port=9222")  # Prevent crashes
options.add_argument("--disable-dev-shm-usage")  # Reduce memory usage
options.add_argument("--no-sandbox")  # Allow running without sandbox
options.add_argument("--start-maximized")  # Open Chrome maximized

# Suppress console errors
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_argument("--disable-gpu")  # Prevent GPU-related errors
options.add_argument("--disable-features=OptimizationGuideModelExecution")  # Prevent ML-based UI errors

# Initialize WebDriver with profile
driver = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(driver, 10)  # Explicit wait

    def logout_facebook():
        driver.get("https://www.facebook.com/")
        time.sleep(3)

        login_check = driver.find_elements(By.NAME, "email")

        if login_check:
            print("You are NOT logged into Facebook.")
        else:
            print("You are LOGGED INTO Facebook.")
            try:
                profile_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Your profile']")))
                profile_icon.click()
                time.sleep(2)

                logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Log Out')]")))
                logout_button.click()
                time.sleep(3)

                print("Successfully logged out from Facebook.")
            except Exception as e:
                print(f"Facebook logout error: {e}")

    def logout_google():
        driver.get("https://accounts.google.com/")
        time.sleep(3)

        profile_check = driver.find_elements(By.XPATH, "//a[contains(@href, 'SignOutOptions')]")
        
        if profile_check:
            print("You are LOGGED INTO Google.")
            driver.get("https://accounts.google.com/SignOutOptions")
            time.sleep(3)

            try:
                logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign out')]")))
                logout_button.click()
                time.sleep(3)

                print("Successfully logged out from Google.")
            except Exception as e:
                print(f"Google logout error: {e}")
        else:
            print("You are NOT logged into Google.")

    def logout_github():
        driver.get("https://github.com/")
        time.sleep(3)

        profile_button = driver.find_elements(By.XPATH, "//button[@aria-label='Open user navigation menu']")
        
        if profile_button:
            print("You are LOGGED INTO GitHub.")
            try:
                profile_button[0].click()
                time.sleep(2)

                logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'logout')]")))
                logout_button.click()
                time.sleep(3)
                
                logout_from_all_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/main/div/form/input[4]")))
                logout_from_all_account_button.click()
                time.sleep(3)

                print("Successfully logged out from GitHub.")
            except Exception as e:
                print(f"GitHub logout error: {e}")
        else:
            print("You are NOT logged into GitHub.")

    logout_facebook()
    logout_google()
    logout_github()

finally:
    driver.quit()  # Close browser
