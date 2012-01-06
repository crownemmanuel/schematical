===========
Schematical
===========

Search and rescue application.


Features
========

#. Receives location and condition via SMS.
#. Show control panel with location and status on top of building schematics.


Use cases
=========

As a user
---------

#. From your mobile phone, text "!HURT @WorldBank,MC-202".

As a respondant
---------------

#. When you open the control panel, you will be able to see a floor plan of the building with an overlay of the people that need to be rescued.


Implementation
==============

Schematical is written using Flask, A Python Web Microframework loosely based on Django[1].
For those with a PHP background, Flask would be the equivalent of CakePHP or Symphony.

[1] http://flask.pocoo.org

Installation
============
#. Install Git and Python >= 2.6

#. Install virtualenv::
    sudo easy_install virtualenv

#. Clone this repository using git::
    git clone git://github.com/crownemmanuel/schematical.git
    cd schematical

#. Create a virtualenv for this application::
    virtuanelv venv

#. Activate the virtual environment::
    source venv/bin/activate

#. Install the requirements::
    pip install -r requirements.txt

#. Run the tests::
    python tests.py

#. Run the server::
    python schematical.py

#some issue being dealt with on the versioning
And then navigate to http://localhost:5000
