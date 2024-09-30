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
        
        
def buy_cart():
    """
    Buy every item on the cart
    
    Parameters:
    None
    
    Return:
    None
    """
    driver.find_element(By.ID, "checkout").click()
    
    driver.find_element(By.ID, "first-name").send_keys("test name")
    driver.find_element(By.ID, "last-name").send_keys("test lastname")
    driver.find_element(By.ID, "postal-code").send_keys("00000")
    
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    
    message = driver.find_element(By.ID, "checkout_complete_container").text

    assert "Thank you for your order" in message
    logging.info("Purchase COMPLETED")


if __name__ == '__main__':
    # Logs & Pytest reports
    logging.basicConfig(filename='results/logs/make_a_purchase.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    pytest.main(["--html=results/reports/make_a_purchase.html",
                 "--json-report",
                 "--json-report-file=results/reports/make_a_purchase.json"])
    
    # Start of Code
    try:
        logging.info("Starting 'make_a_purchase' test")
        
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

        buy_cart()

        driver.quit
        
        logging.info("Finishing 'make_a_purchase' test")

        
    except Exception as e:
        logging.error(f"'make_a_purchase' test failed: {str(e)}")
        raise