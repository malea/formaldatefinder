formaldatefinder
================

## Easy setup -- Vagrant

1.  Download and install [Vagrant](http://www.vagrantup.com/).

2.  Open a command prompt in the directory for this project. Run the following
    command to set up the virtual machine:

        vagrant up

3.  You can now start the server by running:

        vagrant ssh -c "cd /vagrant && foreman start"

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

## Contributing

1.  [Fork this repository.](https://github.com/malea/formaldatefinder/fork)

2.  Clone your version of the repository.

        git clone https://github.com/YOURUSERNAME/formaldatefinder

3.  Set the upstream to the original repository.

        git remote add upstream https://github.com/malea/formaldatefinder.git

    This allows you to update your master branch with the following command:

        git pull upstream master:master

4.  Develop in a separate feature branch. Create a new branch with:

        git checkout master
        git checkout -b NEWBRANCH

    Push your changes using:

        git push origin NEWBRANCH:NEWBRANCH

5.  Submit your changes for review as a
    [Pull Request](https://github.com/malea/formaldatefinder/compare).
