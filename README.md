# playground
## Introduction
This is my little playground. It contains a variety of bits of code used
for various purposes.

## Installation
You are free to clone this repository and any of its code. If you do use my code 
in your projects, I certainly would appreciate a shout-out or some credit.

### Python
Under the Python directory, there is a **requirements.txt** file. This file can be used to
install required packages for the sample code to run. _You must first have Python
and pip installed_. The following code can be run to install the required modules
from the directory where the **requirements.txt** reside.

```commandline
pip install -r ./requirements.txt
```

#### Sample Webapp
There is a small sample webapp using Python Flask and bootstrap CSS. The app is designed to
demo some functionalities of Flask for web development. It uses Flask and a simple on disk
JSON file for data storage, and pulls some variables from the config.py file.

To work with this web app, you will need to create a ``.env`` file in the application directory, 
and set a variable called 'SECRET_KEY', this is needed for Flask's flash notification function to work, as 
flash notification requires the browser to track sessions, and the Secret Key will be used in the creation 
of session cookies. The sample content of a ``.env`` file would look like the following:

```commandline
SECRET_KEY="This is my secret key!"
```

