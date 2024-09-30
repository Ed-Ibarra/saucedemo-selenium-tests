import time, logging, pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_users():
    """
    Returns a list of all users available
    
    Parameters:
    None
    
    Return:
    list - All users
    """
    login_credentials_div = driver.find_element(By.ID, "login_credentials")
    
    # Get the whole text inside the div with the ID "login_credentials"
    full_text = login_credentials_div.get_attribute('innerText')

    # Exclude the text from the H4 tag and save the usernames in a list
    h4_text = login_credentials_div.find_element(By.TAG_NAME, "h4").text
    usernames = full_text.replace(h4_text, "").strip().split("\n")
    
    return usernames

def get_password():
    """
    Return the only password
    
    Parameters:
    None
    
    Return:
    string - Password
    """
    login_password_div = driver.find_element(By.CLASS_NAME, "login_password")
    
    # Get the whole text inside the div with the CLASSNAME "login_password"
    full_text = login_password_div.get_attribute('innerText')

    # Exclude the text from the H4 tag and save the usernames in a list
    h4_text = login_password_div.find_element(By.TAG_NAME, "h4").text
    password = full_text.replace(h4_text, "").strip()
    
    return password


if __name__ == '__main__':
    # Logs & Pytest reports
    logging.basicConfig(filename='results/logs/all_users.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    pytest.main(["--html=results/reports/all_users.html",
                 "--json-report",
                 "--json-report-file=results/reports/all_users.json"])
    
    # Start of Code
    try:
        logging.info("Starting 'all_users' test")
        
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        users = get_users()
        password = get_password()
        
        # List of users that could not log in
        issue_users = []

        for user in users:
            try:
                driver.find_element(By.ID, "user-name").send_keys(user)
                driver.find_element(By.ID, "password").send_keys(password)
                driver.find_element(By.ID, "login-button").click()
                
                driver.find_element(By.ID, "react-burger-menu-btn").click()
                
                time.sleep(1)
                
                driver.find_element(By.ID, "logout_sidebar_link").click()

            except:
                logging.error(f"Something went wrong with the user: {user}")
                issue_users.append(user)
                driver.get("https://www.saucedemo.com/")
        
        logging.info(f"PASS to login: {", ".join([user 
                                                for user in users 
                                                    if user not in issue_users]
                                                )}")

        logging.info(f"FAIL to login: {", ".join(issue_users)}")

        driver.quit
        
        logging.info("Finishing 'all_users' test")
        
    except Exception as e:
        logging.error(f"'all_users' test failed: {str(e)}")
        raise