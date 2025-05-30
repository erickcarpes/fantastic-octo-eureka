from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from Test.login import test_login

def time_at_work(dateIn, noteIn, dateOut, noteOut):
    driver = test_login("Admin", "admin123")

    driver.find_element(By.CSS_SELECTOR, "button.oxd-icon-button.oxd-icon-button--solid-main.orangehrm-attendance-card-action").click()

    input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="yyyy-dd-mm"]')))
    input_field.clear()
    input_field.send_keys(dateIn)
    print("Date in:")

    textarea_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Type here"]')))
    textarea_field.clear()
    textarea_field.send_keys(noteIn)
    print("Note in:")

    driver.find_element(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space').click()
    print("Time in recorded successfully.")

    input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="yyyy-dd-mm"]')))
    input_field.clear()
    input_field.send_keys(dateOut)
    print("Date out:")

    driver.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-clock.oxd-time-input--clock").click()
    print("Clock icon clicked.")

    for _ in range(5):
        driver.find_element(By.CSS_SELECTOR, 'i.oxd-icon.bi-chevron-down.oxd-icon-button__icon.oxd-time-hour-input-down').click()
    print("Hour decremented 5 times.")

    driver.find_element(By.CSS_SELECTOR, 'div.oxd-time-period-label').click()
    print("Time period PM clicked.")

    textarea_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Type here"]')))
    textarea_field.clear()
    textarea_field.send_keys(noteOut)
    print("Note out:")

    driver.find_element(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space').click()
    print("Time out recorded successfully.")

    time.sleep(20)
    return driver

if __name__ == "__main__":
    driver = None
    try:
        driver = time_at_work("2023-10-01", "Start of work", "2023-10-01", "End of work")
        print("Time at work test passed.")
    except TimeoutException:
        print("Time at work test failed: Timeout while waiting for elements.")
    except NoSuchElementException as e:
        print(f"Time at work test failed: Element not found - {e}")
    finally:
        driver.quit()