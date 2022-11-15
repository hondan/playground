#! /usr/bin/env python -tt
'''
This code snippet demonstrates how Python can be used to interact with APIs and also the use of functions
'''

import json
from requests import get


# Sample API URL for US population, this URL does not need authentication
URL = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"


def get_data(url):
    '''
    Function that tries to get API data and return the converted dictionary object
    :param url: REST Endpoint URL
    :return: Dictionary object or None
    '''
    try:
        return json.loads(get(url).content)
    except Exception:
        return None


def main():
    data = get_data(str(URL))

    # If the data obtained is a dictionary object, then print first layer keys and values
    if isinstance(data, dict):
        print("\n+++ Parsed Data: +++\n")
        for each_key in data.keys():
            print(f"Key: {str(each_key)}:\n")
            print(f"Data: {data[each_key]}\n")
    else:
        print(f"\nCan't parse data from {str(URL)}")


if __name__ == '__main__':
    main()
