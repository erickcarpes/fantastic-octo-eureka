from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from login import test_login
import time

def new_post(content):
    driver = test_login("Admin", "admin123")

    WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//span[text()='Buzz']/ancestor::a"))
    ).click()

    textarea_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.oxd-buzz-post-input'))
    )
    textarea_field.clear()
    textarea_field.send_keys(content)

    driver.find_element(By.CSS_SELECTOR, '.oxd-button.oxd-button--medium.oxd-button--main').click()

    time.sleep(10)
    return driver

if __name__ == "__main__":
    driver = None
    try:
        driver = new_post("This is a new post for testing.")
        print("New Post test passed.")
    except TimeoutException:
        print("New Post test failed: Timeout while waiting for elements.")
    except NoSuchElementException as e:
        print(f"New Post test failed: Element not found - {e}")
    finally:
        if driver:
            driver.quit()