from bs4 import BeautifulSoup

import requests


class ESTAR_API:
    """
    API for extracting, transforming, and loading ESTAR data from NIST
    """

    def __init__(self, options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None, keep_alive=True):
        """
        Creates a new instance of the NIST ESTAR src.

        Starts the service and then creates new instance of NIST ESTAR src.

        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - options - this takes an instance of ChromeOptions
         - service_args - List of args to pass to the driver service
         - desired_capabilities - Dictionary object with non-browser specific
           capabilities only, such as "proxy" or "loggingPref".
         - service_log_path - Where to log information from the driver.
         - chrome_options - Deprecated argument for options
         - keep_alive - Whether to configure NIST src to use HTTP keep-alive.
        """
        self.options = options
        self.service_args = service_args
        self.desired_capabilities = desired_capabilities
        self.service_log_path = service_log_path
        self.chrome_options = chrome_options
        self.keep_alive = keep_alive

    def get_ESTAR_HTML(self):
        """
        Returns the ESTAR page's HTML
        """
        url = "https://physics.nist.gov/PhysRefData/Star/Text/ESTAR.html"
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data)
        print(soup)
        return data


if __name__ == '__main__':
    ESTAR_operator = ESTAR_API()
    ESTAR_HTML = ESTAR_operator.get_ESTAR_HTML()
