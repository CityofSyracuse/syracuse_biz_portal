# Syracuse Biz Portal


## Install Instructions for Developing with the Sample Project


Requires Postgres and Django be installed.  This project is developed and *only* works with Python 3.5 and Django 1.9 (and probably higher but untested).

```bash
pip install -r requirements/app.txt
```

Copy the local_settings file and update the settings to fit your machine.

```
cp local_settings.py.example local_settings.py
```

Create a database for the application by first logging into postgres (`psql`) then running:

```
CREATE DATABASE syracuse_biz_portal;
```

Test that Django is working and pointed at your database(migrations not yet created).

```
./manage.py migrate
```

Create a user to log in to and manage the application.

```
./manage.py createsuperuser
```

## For Contributors

First thank you for helping its much appreciated.  This project is currently has to major functions to host a bizport CMS with Wagtail and to offer a resource search tool using [wealthmap](https://github.com/codeforamerica/wealthmap) which is configured in the matcher app in this project.

You might end up wanting to make changes to the wealthmap application as well.  If so fork and clone the app to your desktop environment and then install from source like so.

```
pip install -e .
```

This will allow you to work on both repositories and without having to push and upgrade from this project.


### Pushing Up Changes

The best way to help us is to look through existing issues or create new issues. Once its triaged then to fork this code and make a branch.


Once you've made your proposed changes, if the tests pass(if we have tests) and the pep8 linter passes( see .pep8 file) you're ready to file a PR.


Doing this will mean your changes are highly likely to make it into the main repository.

