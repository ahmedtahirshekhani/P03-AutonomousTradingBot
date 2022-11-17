#### Backend

To activate virtual env
`source venv/bin/activate`

To run the flask api (our backend server)
`gunicorn -b :8080 trading_app.api.flask_app:app`

To deploy backend to gcloud
`gcloud app deploy`
