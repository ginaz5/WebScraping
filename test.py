import datetime as dt
from posixpath import join
from googleapiclient.discovery import build
from google.oauth2 import service_account

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# --data-- 
def extract(page):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    # page 1 -> 0, 2 -> 10, 3 -> 20
    url = f"https://tw.indeed.com/jobs?q=Python+developer&l=Taiwan&start={page}"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')
    for item in divs:
        if item.find('span').text == "新職缺":
            title = "(NEW POST)" +item.find_all('span')[1].text
        else:
            title = item.find('span').text
        company = item.find('span', class_="companyName").text

        try:
            salary = item.find('div', class_ = 'salary-snippet').span.text
        except:
            salary = ''
        summary = item.find('div', class_ = 'job-snippet').text.replace('\n', '')

        job = {
            'Title': title,
            'Company':company,
            'Salary': salary,
            'Summary':summary
        }
        # job_list.append(job)∑
        for key, value in job.items():
            job_list.append(value)
    return
    
job_list = []

for i in range(0, 40, 10):
    print(f"Getting page {i} from Indeed")
    c = extract(i)
    transform(c)
print(job_list)

# Generate Credentials
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
today = str(dt.datetime.today().date())
request_body = {
    'requests': [{
        "addSheet": {
            'properties': {
                    'title': today,

                }
             },
    }]
}


# create new worksheet
add_response = sheet.batchUpdate(spreadsheetId = SPREADSHEET_ID, body = request_body).execute()

# write content
update_response = sheet.values().update(
    spreadsheetId = SPREADSHEET_ID, 
    range = today, 
    valueInputOption = "USER_ENTERED",
    body = {"majorDimension": "ROWS", "values":job_list}).execute() # ROWS is default setting

print("ADD:", add_response)
print("Update:", update_response)