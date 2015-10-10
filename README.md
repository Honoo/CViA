# CViA
Curriculum Vitae Analyzer

# Setup

## System Dependencies
* [xpdf](www.foolabs.com/xpdf/download.html)

## Vendor libraries
* `git submodule init`
* `git submodule update`
* `./setup`

## Database
* Install http://dev.mysql.com/downloads/connector/python/
* Follow CVIA/CVIA/settings.py to setup MySQL database and user

## Django Setting
* Add the following into your enviroment: DJANGO_SETTINGS_MODULE=CViA.settings
* Windows: In the django folder (/CViA) run `set DJANGO_SETTINGS_MODULE=CViA.settings`

