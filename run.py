import socket
import sqlite3
from typing import Any
from warnings import warn

import requests


class Database:

    def __init__(self):
        """
        Creates a connection to the database
        """
        self.__conn = sqlite3.connect("results.db")
        self.__create_table()

    def __cursor(self) -> sqlite3.Cursor:
        """
        Generates a cursor for the database connection
        :return: Database cursor
        """
        return self.__conn.cursor()

    def __save(self):
        """
        Commits any recent changes to the database
        """
        self.__conn.commit()

    def __execute(self, sql: str, data: Any = ()) -> sqlite3.Cursor:
        """
        Executes an sql statement on the database with provided data
        :param sql: The sql statement to execute
        :param data: Any data to inject alongside the statement (defaults to empty tuple)
        :return: Active database cursor
        """
        cursor = self.__cursor()
        cursor.execute(sql, data)
        self.__save()
        return cursor

    def __create_table(self):
        self.__execute('''CREATE TABLE IF NOT EXISTS results
        (test_id INTEGER PRIMARY KEY,
        datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
        target_url TEXT,
        time_seconds REAL,
        internal_ip TEXT,
        external_ip TEXT)''')

    def log(self, target_url: str, time_seconds: float, internal_ip: str, external_ip: str):
        """
        Logs a test result to the database
        :param target_url: The target URL of the test
        :param time_seconds: The time, in seconds, taken to load the target
        :param internal_ip: The internal IP of the device testing
        :param external_ip: The external IP of the network testing
        """
        self.__execute('''INSERT INTO results (target_url, time_seconds, internal_ip, external_ip) VALUES (?,?,?,?)''',
                       (target_url, time_seconds, internal_ip, external_ip))


class Tester:

    def __init__(self):
        """
        Creates the tester class
        """
        self.__db = Database()
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
        self.__db.log(self.__target, self.__time, self.__int_ip, self.__ext_ip)


if __name__ == "__main__":
    tester = Tester()
    tester.get_internal_ip().get_external_ip()
    tester.set_target("https://google.com").test_target().log_results()
    tester.set_target("https://google.co.uk").test_target().log_results()
