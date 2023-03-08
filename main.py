#!/usr/bin/env python3

import requests
import pandas as pd
import json
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Our endpoint URL
endpoint = "http://universities.hipolabs.com/search?country=Canada"

def report_to_csv(api_url):
    # Making a GET request to the endpoint
    response = requests.get(api_url)

    # Serialize the response as JSON
    json_response = json.dumps(response.json())
    logging.info(" Data buffered successfully")

    # Use the pandas library to buffer the serialized response
    df = pd.read_json(json_response)
    logging.info(" %d records retrieved", (len(df)-1))
    logging.info(" Data converted to type JSON")

    # Sort the data frame by the 'name' column, ascending
    sorted_df = df.sort_values(by=["name"])
    logging.info(" Data Frame is now sorted alphabetically")

    # Create the universities.csv file and again use the pandas linrary to export the
    # JSON data frame to CSV format and write it to the file.
    # We're also changing the order of the columns in the CSV file so that it makes more sense.
    with open("universities.csv", 'w') as uni_csv:
        sorted_df.to_csv(uni_csv, index=False, columns=['name', 'domains', 'web_pages', 'state-province', 'alpha_two_code', 'country'])
    logging.info(" Data is now written to file universities.csv")



if __name__ == "__main__":
    report_to_csv(endpoint)
    logging.info(" Task finished with no error")