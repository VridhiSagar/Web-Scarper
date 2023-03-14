import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.allrecipes.com/recipes/455/everyday-cooking/more-meal-ideas/30-minute-meals/"
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
print(response)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
jobs = []

for job in soup.find_all("a", {"class": "comp mntl-card-list-items mntl-document-card mntl-card card card--no-image"}):
#     print(job)
    
    Dish_name = job.find("span", {"class": "card__title-text"}).text.strip()
    Link = job.get('href')
    
    jobs.append({"Dish Name": Dish_name, "Link": Link})


# # print(jobs)
jobs_df = pd.DataFrame(jobs)

