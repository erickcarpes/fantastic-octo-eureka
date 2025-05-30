from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

from Test.login import test_login

def time_at_work(dateIn, timeIn, noteIn, dateOut, timeOut, noteOut):
    driver = webdriver.Chrome()
    test_login(driver, "Admin", "admin123")

    driver.find_element(By.CSS_SELECTOR, "button.oxd-icon-button.oxd-icon-button--solid-main.orangehrm-attendance-card-action").click()
    input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="yyyy-dd-mm"]')))
    input_field.clear()
    input_field.send_keys(dateIn)

    input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="hh:mm"]')))
    input_field.clear()
    input_field.send_keys(timeIn)

    input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Type here"]')))
    input_field.clear()
    input_field.send_keys(noteIn)

    driver.find_element(By.CSS_SELECTOR, 'button.oxd-button.oxd-button--medium oxd-button--secondary.orangehrm-left-space').click()

    input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="yyyy-dd-mm"]')))
    input_field.clear()
    input_field.send_keys(dateOut)

    input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="hh:mm"]')))
    input_field.clear()
    input_field.send_keys(timeOut)

    input_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Type here"]')))
    input_field.clear()
    input_field.send_keys(noteOut)

    driver.find_element(By.CSS_SELECTOR, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space').click()
    time.sleep(20)
    driver.implicitly_wait(20)
    return driver

if __name__ == "__main__":
    try:
        driver = time_at_work("2023-10-01", "08:00", "Start of work", "2023-10-01", "17:00", "End of work")
        print("Time at work test passed.")
    except TimeoutException:
        print("Time at work test failed: Timeout while waiting for elements.")
    except NoSuchElementException as e:
        print(f"Time at work test failed: Element not found - {e}")
    finally:
        driver.quit()