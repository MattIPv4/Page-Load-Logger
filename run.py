import socket
from warnings import warn

import requests


class Tester:

    def __init__(self):
        """
        Creates the tester class
        """
        self.__time = None
        self.__int_ip = None
        self.__ext_ip = None
        self.__target = None

    def set_target(self, target: str) -> "Tester":
        """
        Sets the target URL that will be tested, resets time
        :param target: Target URL
        :return: self
        """
        self.__target = target
        self.__time = None
        return self

    def test_target(self) -> "Tester":
        """
        Tests the load time of the target URL
        :return: self
        """
        if self.__target is None:
            warn("No target is defined, test_target did not run")
            return self

        self.__time = requests.get(self.__target).elapsed.total_seconds()
        return self

    def get_internal_ip(self) -> "Tester":
        """
        Fetches the internal IP of the current device
        :return: self
        """
        self.__int_ip = socket.gethostbyname(socket.gethostname())
        return self

    def get_external_ip(self) -> "Tester":
        """
        Fetches the external IP address of the current network
        :return: self
        """
        self.__ext_ip = requests.get("https://api.ipify.org/").text
        return self

    def log_results(self) -> "Tester":
        """
        Logs the results of the most recently run test
        :return: self
        """
        if self.__time is None:
            warn("No time is recorded, run test_target before log_results")
            return self
        if self.__int_ip is None:
            warn("Internal IP is not known, run get_internal_ip before log_results")
            return self
        if self.__ext_ip is None:
            warn("External IP is not known, run get_external_ip before log_results")
            return self
        print(self.__target, self.__time, self.__int_ip, self.__ext_ip)


if __name__ == "__main__":
    tester = Tester()
    tester.get_internal_ip().get_external_ip()
    tester.set_target("https://google.com").test_target().log_results()
    tester.set_target("https://google.co.uk").test_target().log_results()
