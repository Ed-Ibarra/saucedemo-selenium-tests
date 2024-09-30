import random, logging, pytest

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def login(user, password):
    """
    Log in into the site
    
    Parameters:
    user: User's name
    password: User's password
    
    Return:
    None
    """
    try:
        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

    except:
        logging.error(f"Something went wrong with the user '{user}'")
        
    else:
        logging.info(f"'{user}' has been log in successfully")
        

def select_filter(dropdown):
    """
    Select randomly a filter to be tested
    
    Parameters:
    dropdown: Option list object
    
    Return:
    None
    """
    options = [option.text for option in dropdown.options]
    choice = random.randint(0, len(options) - 1)
    
    dropdown.select_by_index(choice)
    logging.info(f"Filter tested: '{options[choice]}'")


if __name__ == '__main__':
    
    # Logs & Pytest reports
    logging.basicConfig(filename='results/logs/product_filters.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    pytest.main(["--html=results/reports/product_filters.html",
                 "--json-report",
                 "--json-report-file=results/reports/product_filters.json"])
    
    # Start of Code
    try:
        logging.info("Starting 'product_filters' test")
        
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        user = "standard_user"
        password = "secret_sauce"
        login(user, password)

        dropdown = Select(driver.find_element(By.CLASS_NAME, ("product_sort_container")))
        select_filter(dropdown)

        driver.quit
        
        logging.info("Finishing 'product_filters' test")

    except Exception as e:
        logging.error(f"'product_filters' test failed: {str(e)}")
        raise