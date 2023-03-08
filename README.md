## Scripted API Report

This assignment requires the user to retrieve some data from an API endpoint and write it to a CSV file eventually.

This could be done without having to import any 3rd party libraries but as was mentioned in the question, usage of libraries was optional.
I used the `requests` library to connect to the endpoint and send a GET request and also the `pandas` library to serialize and convert the raw data to CSV and eventually write it to file named `universities.csv`.

I'm afraid I did not get a chance to do any error handling and/or testing for this code. I could certainly to all that if I had more time for this project.

Runnign the code (I also skipped the creation of a `venv` for this one):
```
pip install -r requirements.txt
chmod u+x main.py
./main.py
```

And to see the results, you can open the `universities.csv` file with any CSV reader available.


TODO: Error handling
TODO: Tests, Tests and Tests
TODO: More tests
TODO: Create a Makefile and include all the steps required to run the code