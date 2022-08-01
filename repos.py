from dataclasses import dataclass
from dotenv import load_dotenv
from datetime import datetime
from github import Github
from numpy import NaN
import pandas as pd
import os

load_dotenv(".env", override=True)

def format_date(date):
    return date.strftime("%Y%m%d")

def elapsted_time(start):
    return str((datetime.now()-start).seconds) + "s"

@dataclass
class Repo:
    name: str
    topics: str
    latest_commit_date: str
    owner: str

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

repos = list()

start = datetime.now()
print("app.py started at:", start)
github_repos = g.get_user().get_repos()
print("[",elapsted_time(start=start),"][", g.get_user().login, "]", github_repos.totalCount, "repositories")
for repo in github_repos:
    topics = repo.get_topics()
    commits = repo.get_commits()
    repo_name = repo.name
    owner = repo.__dict__.get('_rawData')['owner']['login']
    try:
        latest_commit_date = format_date(commits[0].commit.author.date)    
    except:
        print("WARN", repo_name)
        latest_commit_date = NaN
    r = Repo(name=repo_name, topics=topics, latest_commit_date=latest_commit_date, owner=owner)
    repos.append(r)
    print("[",elapsted_time(start=start),"][", owner, "][",repo_name,"]") 

df = pd.DataFrame(repos)
df.to_csv("repos.csv")

print("repos.py finish at:", datetime.now())
print("repos.py elapsted time", elapsted_time(start=start))