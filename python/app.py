#! /usr/bin/env python

from flask import Flask, request, render_template, flash, redirect, url_for
from config import NAME, DESC, SECRET_KEY, DB_FILE_FULL_PATH
from os import path
import json
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


def write_data(data):
    """
    Takes a list of dictionary file and converts it to JSON for output to defined file path from the config file
    :param data: A list of dictionary object
    :return: True if successful, False if failed
    """
    # Attempt to open the file in full overwrite mode and output the converted JSON to file.
    try:
        with open(DB_FILE_FULL_PATH, "w") as file:
            file.write(json.dumps(data, indent=4))
        file.close()
        return True
    # If exception, show on web server, and return False.
    except Exception as e:
        print(f'Error encountered: {str(e)}')
        app.logger.error(f'Error encountered: {str(e)}')
        return False


def load_data(location=DB_FILE_FULL_PATH):
    """
    Attempt to read file defined in the location varaible and load the file into JSON.
    :param location: The path and filename of the file.
    :return:
    """
    # Check to see if the file exists, if so, then try to open the file and convert it to Dictionary and return data.
    if path.exists(location):
        try:
            with open(location, 'r') as file:
                raw_data = file.read()
            file.close()
            data = json.loads(raw_data)
            return data
        # If there is an error, then output error on server, and return None
        except Exception as e:
            print(f'Error encountered: {str(e)}')
            app.logger.error(f'Error encountered: {str(e)}')
            return None
    # If file doesn't exist, return none.
    else:
        print(f'The file at "{str(location)} does not yet exist"')
        app.logger.warning(f'The file at "{str(location)} does not yet exist"')
        return None


@app.route('/', methods=['GET'])
def index():
    """
    Load the data from the on-server JSON file and display it using the index.html template.
    :return: Displayed index.html template.
    """
    data = load_data()
    if data is None:
        data = [{'id': 0,
                 'name': 'So empty...',
                 'desc': 'Nothing is here yet',
                 'time': str(datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z'))}]
    return render_template('index.html', data=data)


@app.route('/demo', methods=['GET', 'POST'])
def demo():
    """
    Interact with the demo.html file. Accepts HTTP GET and POST.
    :return: Rendered demo page for more posting.
    """
    # For HTTP GET method, simply render the empty demo page.
    if request.method == 'GET':
        return render_template('demo.html')
    # For other methods (i.e., POST), obtain data from the webpage, check for errors, and append the data to
    # existing data JSON file
    elif request.method == 'POST':
        name = request.form['name']
        desc = request.form['desc']
        if not name or not desc:
            flash('Name and Description are Required', 'error')
        else:
            data = load_data()
            if data is not None:
                data.append({'id': int(len(data)),
                             'name': str(name),
                             'desc': str(desc),
                             'time': str(datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z'))
                             })
            else:
                data = list()
                data.append({'id': 0, 'name': str(name), 'desc': str(desc)})
            # Write JSON data back out to disk and show successful or failed message.
            write_result = write_data(data=data)
            if write_result:
                flash('Posting successful', 'info')
            else:
                flash('Posting failed, failed to write to dataset', 'error')
        return redirect(url_for('demo'))


@app.route('/about', methods=['GET'])
def about():
    """
    Render the about page with supplied information from the config.py file.
    :return: Rendered about.html page.
    """
    return render_template('about.html', name=NAME, desc=DESC)


if __name__ == '__main__':
    app.run()
