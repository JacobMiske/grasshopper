#!/usr/bin/python3
import time
from builtins import str
from selenium import webdriver

ATOMIC_NUMBER = 2


class pstar_api():
    """
    Controls the NIST pstar database website.

    This API handles automated use of the following website.
    https://physics.nist.gov/PhysRefData/pstar/html/pstar1.html
    """
    def __init__(self, options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
        """
        Creates a new instance of the NIST pstar API.

        Starts the service and then creates new instance of NIST pstar API.

        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - options - this takes an instance of ChromeOptions
         - service_args - List of args to pass to the driver service
         - desired_capabilities - Dictionary object with non-browser specific
           capabilities only, such as "proxy" or "loggingPref".
         - service_log_path - Where to log information from the driver.
         - chrome_options - Deprecated argument for options
         - keep_alive - Whether to configure NIST API to use HTTP keep-alive.
        """
        self.options = options
        self.service_args = service_args
        self.desired_capabilities = desired_capabilities
        self.service_log_path = service_log_path
        self.chrome_options = chrome_options
        self.keep_alive = keep_alive

    def get_user_options(self):
        """
        A list of boolean values related to
        user options in data scraping
        :return:
        """
        options = [1,0,0]
        return options

    def get_pstar_results(self, options, options_bool=False, print_out=False):
        """
        Use selenium's webdriver to search the pstar website
        and query the database.
        :return:
        """
        # Open Chrome window
        driver = webdriver.Chrome()
        driver.get('https://physics.nist.gov/PhysRefData/pstar/html/pstar1.html')
        # Click submit button
        submit_button = driver.find_elements_by_xpath("//input[@value='Submit Information']")[0]
        submit_button.click()
        # Type atomic number
        text_area = driver.find_elements_by_xpath("/html/body/form/p[2]/table/tbody/tr[1]/td[1]/p/input[1]")[0]
        text_area.send_keys(str(ATOMIC_NUMBER))
        # Click submit button
        submit_button = driver.find_elements_by_xpath("//input[@value='Submit Information']")[0]
        submit_button.click()
        # Remove graph
        # submit_button = driver.find_elements_by_xpath("/html/body/form/p[2]/table/tbody/tr[2]/td[1]/p[1]/input")[0]
        # submit_button.click()
        # Click tab deliminator submit button
        submit_button = driver.find_elements_by_xpath("//input[@value='tab']")[0]
        submit_button.click()
        # Click download submit button
        submit_button = driver.find_elements_by_xpath("/html/body/form[2]/p/input[5]")[0]
        submit_button.click()
        # Print out html
        if print_out:
            html = driver.page_source
            print(html)
        # Wait then close
        time.sleep(3)
        driver.quit()
        return html if print_out else 0


if __name__ == '__main__':
    pstar_operator = pstar_api()
    # Get options on request
    options_user = pstar_operator.get_user_options()
    # Run the data scraper
    html = pstar_operator.get_pstar_results(options=options_user, print_out=True)
