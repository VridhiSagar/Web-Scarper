import requests
import random
import pandas as pd
from bs4 import BeautifulSoup
import csv


url = "https://www.amazon.com/charts/mostsold/nonfiction/ref=bsm_char_sold_nonfict/ref=s9_acss_bw_cg_bsmmost_1a1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-5&pf_rd_r=71ZZE5ADT8J9PPR4GYR2&pf_rd_t=101&pf_rd_p=6be52979-aa91-4d19-9c0a-4b11ed3e5f6f&pf_rd_i=16857165011" 
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

for job in soup.find_all("div", {"class": "kc-horizontal-rank-card desktop-hide mobile-hide row"}):
#     print(job)
    title = job.find("div", {"class": "kc-rank-card-title"}).text.strip()
    author = job.find("div", {"class": "kc-rank-card-author"}).text.strip()
    pub = job.find("div", {"class": "kc-rank-card-publisher"}).text.strip()
#     description = job.find("div", {"class": "job_snippet"}).text.strip()
    
    jobs.append({"title": title, "author": author, "pub": pub})

for job in soup.find_all("div", {"class": "kc-horizontal-rank-card mobile-hide row"}):
#     print(job)
    title = job.find("div", {"class": "kc-rank-card-title"}).text.strip()
    author = job.find("div", {"class": "kc-rank-card-author"}).text.strip()
    pub = job.find("div", {"class": "kc-rank-card-publisher"}).text.strip()
#     description = job.find("div", {"class": "job_snippet"}).text.strip()
    
    jobs.append({"title": title, "author": author, "pub": pub})

# print(jobs)
jobs_df = pd.DataFrame(jobs)

