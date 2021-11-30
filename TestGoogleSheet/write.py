import datetime as dt
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

values = [["12/1/2020", 4000], ["14/1/2010", 3000], ["5/1/2021", 7000]]

request = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID, 
    range="write!A1", 
    valueInputOption="USER_ENTERED",
    body={"values":values})

response = request.execute() 
print(response)