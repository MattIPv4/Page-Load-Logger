<!-- Source: https://github.com/MattIPv4/template/blob/master/README.md -->

<!-- Title -->
<h1 align="center" id="Page-Load-Logger">
    Page Load Logger
</h1>

<!-- Tag line -->
<h3 align="center">A single Python script to log page load speeds to an SQLite database</h3>

<!-- Badges -->
<p align="center">
    <img src="https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg?style=flat-square" alt="Style"/>
    <a href="http://patreon.mattcowley.co.uk/" target="_blank">
        <img src="https://img.shields.io/badge/patreon-IPv4-blue.svg?style=flat-square" alt="Patreon"/>
    </a>
    <a href="http://slack.mattcowley.co.uk/" target="_blank">
        <img src="https://img.shields.io/badge/slack-MattIPv4-blue.svg?style=flat-square" alt="Slack"/>
    </a>
</p>

----

<!-- Content -->
## Getting Started

### Python Environment

This script is written to work with Python 3.6 & 3.7.
For Windows & macOS, you can download Python from [the official website](https://www.python.org/downloads/).
Installing Python on Linux is more complicated, please see [the Hitchhiker's Guide to Python](https://docs.python-guide.org/starting/install3/linux/) for more information.

It makes use of the requests library which will need to be installed through pip.
This can be done by running `python -m pip install requests` in command line/terminal.
You may need to use `python3` (or similar) instead of `python` in some installations.

### Configuration File

With the Python environment setup, the configuration file needs to be edited to test your desired site or sites.
Within the config.ini file you will find two "variables" that can be set.
Example values for both of these are provided within the config.ini file, as well as comments explaining each variable's purpose.

The first, `[Tester] sites`, is a comma separated list of all the sites that the script should test the loading speed for.
> Eg. `sites = https://google.co.uk, https://bbc.co.uk`

The second value, `[Database] file`, is the file name (and location/path) of the database file that the results will be saved to.
> Eg. `file = results.db`

### Running the Script

With the Python environment prepared and the configuration file edited, the script should be ready to run.
To do this, simply run `python run.py` in your command line/terminal.
As with the pip command, `python` may need to be substituted with `python3` or similar to access your python installation.

## Accessing the Results Data

Once you have run the script, the results will be saved to the database file that your defined in the configuration file.
This file is a [flat-file SQLite database](https://www.sqlite.org/).
You can view the data contained through a tool such as the [DB Browser for SQLite](https://sqlitebrowser.org/).

<!-- Contributing -->
## Contributing

Contributions are always welcome to this project!\
Take a look at any existing issues on this repository for starting places to help contribute towards, or simply create your own new contribution to the project.

Please make sure to follow the existing standards within the project such as code styles, naming conventions and commenting/documentation.

When you are ready, simply create a pull request for your contribution and I will review it whenever I can!

### Donating

You can also help me and the project out by contributing through a donation on PayPal or by supporting me monthly on my Patreon page.
<p>
    <a href="http://patreon.mattcowley.co.uk/" target="_blank">
        <img src="https://img.shields.io/badge/patreon-IPv4-blue.svg?logo=patreon&logoWidth=30&logoColor=F96854&style=popout-square" alt="Patreon"/>
    </a>
    <a href="http://paypal.mattcowley.co.uk/" target="_blank">
        <img src="https://img.shields.io/badge/paypal-Matt%20(IPv4)%20Cowley-blue.svg?logo=paypal&logoWidth=30&logoColor=00457C&style=popout-square" alt="PayPal"/>
    </a>
</p>

<!-- Discussion & Support -->
## Discussion, Support and Issues

Need support with this project, have found an issue or want to chat with others about contributing to the project?
> Please check the project's issues page first for support & bugs!

Not found what you need here?
* If you have an issue, please create a GitHub issue here to report the situation, include as much detail as you can!
* _or,_ You can join our Slack workspace to discuss any issue, to get support for the project or to chat with contributors and myself:
<a href="http://slack.mattcowley.co.uk/" target="_blank">
    <img src="https://img.shields.io/badge/slack-MattIPv4-blue.svg?logo=slack&logoWidth=30&logoColor=blue&style=popout-square" alt="Slack" height="60">
</a>
