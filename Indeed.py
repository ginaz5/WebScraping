import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

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

        job_list.append(job)
    return
    
job_list = []

for i in range(0, 40, 10):
    print(f"Getting page {i} from Indeed")
    c = extract(i)
    transform(c)

today = dt.date.today()
month = today.month
date = today.day

df = pd.DataFrame(job_list)
print(df.head)
df.to_csv(f"{month}{date}_Python_jobs_indeed.csv", encoding='utf-8-sig')