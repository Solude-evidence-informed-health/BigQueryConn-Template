from google.oauth2 import service_account
import pandas as pd

class BigQueryConn:
    def __init__(self, credentials_path):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])

    def get_data_df(self, query_path):
        with open(query_path, 'r') as file:
            query = file.read()
        self.df = pd.read_gbq(query, credentials=self.credentials)
        return self.df