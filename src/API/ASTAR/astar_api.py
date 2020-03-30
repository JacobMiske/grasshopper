"""
ASTAR API class
"""
#!/usr/bin/python3
import time
import csv
import json
from itertools import repeat
from builtins import str
from selenium import webdriver
from api_visualize.api_visualize import astar_api_visualize

# Load the config
with open("config.json") as file:
    ATOMIC_NUMBER = json.load(file).get("astar_request").get("Attributes").get("AtomicNumber")


class ASTAR_API():
    """
    Controls the NIST ASTAR database website.
    """
    def __init__(self, options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
        """
        Creates a new instance of the NIST ASTAR src.

        Starts the service and then creates new instance of NIST ASTAR src.

        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - options - this takes an instance of ChromeOptions
         - service_args - List of args to pass to the driver service
         - desired_capabilities - Dictionary object with non-browser specific
           capabilities only, such as "proxy" or "loggingPref".
         - service_log_path - Where to log information from the driver.
         - chrome_options - Deprecated argument for options
         - keep_alive - Whether to configure NIST ASTAR src to use HTTP keep-alive.
        """
        self.options = options
        self.service_args = service_args
        self.desired_capabilities = desired_capabilities
        self.service_log_path = service_log_path
        self.chrome_options = chrome_options
        self.keep_alive = keep_alive
        self.driver = webdriver.Chrome()
        self.driver.get("https://physics.nist.gov/PhysRefData/Star/Text/ASTAR.html")

    def get_user_options(self):
        """
        A list of boolean values related to
        user options in data scraping
        :return:
        """
        # TODO: Input results of user readable questions

        options = [0, 0, 0]
        return options

    def set_data_options(self):
        """
        Clicks on different return values before data downloaded
        :return: 0
        """
        click_e_stopping = self.driver.find_element_by_xpath(
            "/html/body/form/p/table/thead/tr[2]/th[1]/input")
        click_e_stopping.click()
        click_n_stopping = self.driver.find_element_by_xpath(
            "/html/body/form/p/table/thead/tr[2]/th[2]/input")
        click_n_stopping.click()
        click_t_stopping = self.driver.find_element_by_xpath(
            "/html/body/form/p/table/thead/tr[2]/th[3]/input")
        click_t_stopping.click()
        click_range_CSDA = self.driver.find_element_by_xpath(
            "/html/body/form/p/table/thead/tr[2]/th[4]/input")
        click_range_CSDA.click()
        click_range_projected = self.driver.find_element_by_xpath(
            "/html/body/form/p/table/thead/tr[2]/th[5]/input")
        click_range_projected.click()
        click_range_detour = self.driver.find_element_by_xpath(
            "/html/body/form/p/table/thead/tr[2]/th[6]/input")
        click_range_detour.click()
        return 0

    def save_data_to_csv(self, web_tsv_scrape):
        """
        Takes astar data and saves as a .csv file
        :return:
        """
        with web_tsv_scrape as tsvin, open("data.csv", "w", newline='') as csvout:
            tsvin = csv.reader(tsvin, delimiter='\t')
            csvout = csv.writer(csvout)

            for row in tsvin:
                count = int(row[4])
                if count > 0:
                    csvout.writerows(repeat(row[2:4], count))
        return 0

    def get_astar_html(self, options, options_bool=False, save_html=True):
        """
        Use selenium's webdriver to search the astar website
        and query the database.
        :return:
        """
        # Click on the material, TODO: WebElement does not click
        # element_button = \
        # self.driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[1]/td/div/select")[0]
        # element_button.click()
        # Click submit button
        submit_button = self.driver.find_elements_by_xpath("/html/body/form/div/table/tbody/tr[3]/td/input[1]")[0]
        submit_button.click()
        # Remove graph
        # submit_button = driver.find_elements_by_xpath("/html/body/form/p[2]/table/tbody/tr[2]/td[1]/p[1]/input")[0]
        # submit_button.click()
        self.set_data_options()

        # Click tab deliminator submit button
        submit_button = self.driver.find_elements_by_xpath("/html/body/form/p/input[3]")[0]
        submit_button.click()
        # Click download data submit button
        submit_button = self.driver.find_elements_by_xpath("/html/body/form/p/input[5]")[0]
        submit_button.click()
        # Print out html
        if save_html:
            html = self.driver.page_source
        # Wait then close
        time.sleep(3)
        self.driver.quit()
        return html if save_html else 0

    def get_astar_data(self, astar_html_data, save_file=True):
        """
        Takes HTML with data, convert to readable python object.
        Can pass to save_data_to_csv() method for save file.
        :return:
        """
        res = astar_html_data.split('\t')
        # res = line_res.split('\t')
        result = [float(i.strip()) for i in res[21:-1]]
        print(result)
        astar_data = result
        return astar_data

    def save_data_to_csv(self, astar_html_data):
        """
        Saving method for getting an CSV out
        :param astar_html_data:
        :return:
        """
        res = astar_html_data.split("\t")
        astar_data = [i.strip() for i in res[21:-1]]
        # Get the filename to create
        filename = "../Results/Data/astar_api_result_{}.csv".format(time.time())
        with open(filename, "w") as filename:
            wr = csv.writer(filename, quoting=csv.QUOTE_ALL)
            wr.writerow(astar_data)
        return 0

    def get_astar_api_plots(self, astar_data):
        """

        :param astar_data:
        :return:
        """
        astar_api_visualizer = astar_api_visualize()
        astar_api_visualizer.plot_data(list_v=astar_data)
        # get_metrics = astar_api_visualizer.get_metrics_on_list(list_v=astar_data)


if __name__ == '__main__':
    # Use the module
    astar_operator = ASTAR_API()
    # Get options on request
    options_user = astar_operator.get_user_options()
    # Run the data scraper
    html = astar_operator.get_astar_html(options=options_user, save_html=True)
    data = astar_operator.get_astar_data(save_file=True, astar_html_data=html)
    astar_operator.save_data_to_csv(astar_html_data=html)
    astar_operator.get_astar_api_plots(astar_data=data)

