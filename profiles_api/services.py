from google.cloud import bigquery
import requests


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()


def get_username(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
        user = response.get('results')[0]
        return user.get('name').get('first')

    return ''


def get_teams_BQ():

    # [START bigquery_query]
    # TODO(developer): Import the client library.
    # from google.cloud import bigquery

    # TODO(developer): Construct a BigQuery client object.
    client = bigquery.Client()

    query = """
    SELECT *
    FROM ``
    LIMIT 10"""

    query_job = client.query(query)  # Make an API request.

    return query_job
    # [END bigquery_query]
