formaldatefinder
================

## Setup

Instructions:

1.  Ensure you have Python 3.4 installed. This can be checked at the command
    line:

        $ python3 --version
        Python 3.4.0

    If not, you can download it at the [Python
    website](https://www.python.org/downloads/).

2.  Clone this repository with Git (download available at the [Git
    website](http://git-scm.com/downloads)). The clone command should look
    like:

        git clone https://github.com/malea/formaldatefinder.git

    This will create a folder called `formaldatefinder`.

3.  Create a Python [virtual
    environment](https://docs.python.org/3/library/venv.html) in the project
    folder.

        python3 -mvenv .

    The environment can be activated using the following command:

        source bin/activate

4.  With the virtual environment active, run the following command to install
    the required packages.

        pip install -r requirements.txt
