from dataclasses import dataclass
from dotenv import load_dotenv
from datetime import datetime
from github import Github
from numpy import NaN
import pandas as pd
import os

load_dotenv(".env", override=True)

def file_path(date):
    dir = "data/" + date.strftime("%Y/%m/")
    if not os.path.exists(dir):
        os.makedirs(dir)
    return os.path.join(dir, format_date(date)+".csv")

def format_date(date):
    return date.strftime("%Y%m%d")

@dataclass
class Repo:
    name: str
    topics: str
    latest_commit_date: str
    owner: str

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

repos = list()

github_repos = g.get_user().get_repos()
print("[", g.get_user().login, "]:", github_repos.totalCount, "repositories")
for repo in github_repos:
    topics = repo.get_topics()
    commits = repo.get_commits()
    owner = repo.__dict__.get('_rawData')['owner']['login']
    try:
        latest_commit_date = format_date(commits[0].commit.author.date)    
    except:
        print("WARN", repo.name)
        latest_commit_date = NaN
    r = Repo(name=repo.name, topics=topics, latest_commit_date=latest_commit_date, owner=owner)
    repos.append(r)

df = pd.DataFrame(repos)
df.to_csv("repos.csv")