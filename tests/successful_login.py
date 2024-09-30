import logging, pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    
    # Logs & Pytest reports
    logging.basicConfig(filename='results/logs/successful_login.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    pytest.main(["--html=results/reports/successful_login.html",
                 "--json-report",
                 "--json-report-file=results/reports/successful_login.json"])
    
    # Start of Code
    try:
        logging.info("Starting 'successful_login' test")
        
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        user = "standard_user"
        password = "secret_sauce"

        try:
            driver.find_element(By.ID, "user-name").send_keys(user)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()
            
            driver.find_element(By.ID, "react-burger-menu-btn").click()

        except:
            logging.error(f"Something went wrong with the user '{user}'")
            
        else:
            logging.info(f"'{user}' has been login successfully")

        driver.quit
        
        logging.info("Finishing 'successful_login' test")
    
    except Exception as e:
        logging.error(f"'successful_login' test failed: {str(e)}")
        raise