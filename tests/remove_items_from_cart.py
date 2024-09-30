import logging, pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def add_items(items_list):
    """
    Receive a list of each item available and 1 by 1 add it to the cart
    
    Parameters:
    items_list
    
    Return:
    None
    """
    try:
        for item_button in items_list:
            item_button.click()
    except:
        logging.error("There was a problem adding an item")
    else:
        logging.info("All products were SUCCESSFULLY added to the cart")


def remove_items(items_list):
    """
    Receive a list of each item available and 1 by 1 remove it from the cart
    
    Parameters:
    items_list
    
    Return:
    None
    """
    try:
        for item_button in items_list:
            item_button.click()
    except:
        logging.error("There was a problem")
    else:
        logging.info("All products were SUCCESSFULLY removed from the cart")

    
if __name__ == '__main__':
    
    # Logs & Pytest reports
    logging.basicConfig(filename='results/logs/remove_items_from_cart.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    pytest.main(["--html=results/reports/remove_items_from_cart.html",
                 "--json-report",
                 "--json-report-file=results/reports/remove_items_from_cart.json"])
    
    # Start of Code
    try:
        logging.info("Starting 'remove_items_from_cart' test")
        
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        user = "standard_user"
        password = "secret_sauce"

        driver.find_element(By.ID, "user-name").send_keys(user)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        items_list = driver.find_elements(By.CLASS_NAME, "btn_inventory")
        add_items(items_list)

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        items_list = driver.find_elements(By.CLASS_NAME, "cart_button")
        remove_items(items_list)

        driver.quit
        
        logging.info("Finishing 'remove_items_from_cart' test")
        
    except Exception as e:
        logging.error(f"'remove_items_from_cart' test failed: {str(e)}")
        raise