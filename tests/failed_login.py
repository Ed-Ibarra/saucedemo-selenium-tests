import time, logging, pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def error_message():
    """
    Returns a boolean to verify if there is found an error message
    
    Parameters:
    None
    
    Return:
    True  - If there was an error message
    False - If there was NOT an error message
    """
    
    if driver.find_elements(By.CLASS_NAME, "error-message-container"):
        return True
    else:
        return False

if __name__ == '__main__':
    # Logs & Pytest reports
    logging.basicConfig(filename='results/logs/failed_login.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    pytest.main(["--html=results/reports/failed_login.html",
                 "--json-report",
                 "--json-report-file=results/reports/failed_login.json"])
    
    # Start of Code
    try:
        logging.info("Starting 'failed_login' test")
        
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        user = "wrong_user"
        password = "wrong_password"

        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        logging.error("Wrong credentials") if error_message() else None

        driver.quit
        
        logging.info("Finishing 'failed_login' test")
        
    except Exception as e:
        logging.error(f"'failed_login' test failed: {str(e)}")
        raise