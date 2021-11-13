from googleapiclient.discovery import build

# Generate Credentials
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'pyjobs.json' # the path of json file
SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # to read and write

creds = None
creds = service_account.Credentials.from_service_account_file(
SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID spreadsheet.
SAMPLE_SPREADSHEET_ID = '13zrThBwGdVfhno9MILWokzJerrQKuS8iWZhakJdY87E'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="read!A1:I12").execute()


values = result.get('values', [])
print(values)

