from bs4 import BeautifulSoup
import requests
import time

# add filter features:  remove unfamiliar skills
# print("Put some skill that you are not familiar with")
# unfamiliar_skill = input('>')
# print(f"Flitering out {unfamiliar_skill}")


# def find_jobs():
html_text = requests.get(
'https://www.104.com.tw/jobs/search/?keyword=python&order=1&jobsource=2018indexpoc&ro=0').text
soup = BeautifulSoup(html_text, 'lxml') # lxml is specified as parser
jobs = soup.find('div', class_='b-block b-clear-border b-clearfix job-list')
print(jobs)
#     for job in jobs:
#         published_date = job.find('span', class_='sim-posted').span.text

#         if 'few' in published_date:  # take jobs that post few days ago
#             job_title = job.find('h2').text.replace(' ', '')
#             company_name = job.find(
#                 'h3', class_='joblist-comp-name').text.replace(' ', '')
#             skills = job.find(
#                 'span', class_='srp-skills').text.replace(' ', '')
#             more_info = job.header.h2.a['href']  # to show only url
#             if unfamiliar_skill not in skills:

#                 print(f"Job Title: {job_title.strip()}")
#                 print(f"Company Name: {company_name.strip()}")
#                 print(f"Required Skills: {skills.strip()}")
#                 print(f"More Info: {more_info}")

#                 print('')


# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 1
#         print(f"Waiting {time_wait} minutes...")
#         time.sleep(time_wait * 60)
