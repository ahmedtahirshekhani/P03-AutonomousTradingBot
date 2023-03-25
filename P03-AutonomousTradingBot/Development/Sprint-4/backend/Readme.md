## Requirements to run the flask server

1. Setup the virtual environment
   <code>python -m venv venv</code>
2. Activate the virtual environment
   <code>venv\Scripts\activate</code>
3. Install the requirements first
   <code>pip install -r requirements.txt</code>
4. Change the directory to flask app
   <code>cd trading_app/api/</code>
5. Run the flask server locally
   <code>flask --app flask_app --debug run </code>
6. Run the postgresql server on localhost
   <code>sudo -u postgres psql</code>

## To deploy backend to gcloud

-   `gcloud app deploy`
