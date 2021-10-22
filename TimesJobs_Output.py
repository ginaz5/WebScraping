from bs4 import BeautifulSoup
import requests
import time

# add filter features:  remove unfamiliar skills
print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f"Flitering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        if 'few' in published_date:  # take jobs that post few days ago
            job_title = job.find('h2').text.replace(' ', '')
            company_name = job.find(
                'h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']  # to show only url

            if unfamiliar_skill not in skills:
                with open(f'Posts/{index}.text', 'w') as f:

                    f.write(f"Job Title: {job_title.strip()} \n")
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f"File saved: {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
