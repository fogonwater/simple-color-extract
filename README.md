# simple-color-extract

# Installing

Assumes Python3 with pip and virtualenv

Install the requirements with pip:

```
pip3 install -r requirements.txt --ignore-installed
```

Note the ignore-installed flag -- colorgram has on occasion not installed properly to a virtualenv without it for me.

# Running the app

Control and view extracted data in a Flask served application.

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The app looks for image files in the `static`directory. It will analyse every image it finds, every time someone visits the home page.

Visit root local host to extract colours for all images and provide an HTML summary.

e.g. http://127.0.0.1:5000/

Visit /api for a data view.

e.g. http://127.0.0.1:5000/api