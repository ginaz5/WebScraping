import datetime as dt
import numpy as np
from googleapiclient.discovery import build

# Generate Credentials
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'pyjobs.json' # the path of json file
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # to read and write

creds = None
creds = service_account.Credentials.from_service_account_file(
SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SPREADSHEET_ID = '13zrThBwGdVfhno9MILWokzJerrQKuS8iWZhakJdY87E'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
values = np.array([["12/1/2020", 4000], ["14/1/2010", 3000], ["5/1/2021", 7000]])
today = str(dt.datetime.today().date())
request_body = {
    'requests': [
        {
            "addSheet": {
                'properties': 
                    {
                        'title': today,
                    }
                },
        }
    ]
}


response = sheet.batchUpdate(spreadsheetId=SPREADSHEET_ID, body=request_body).execute() 
print(response)