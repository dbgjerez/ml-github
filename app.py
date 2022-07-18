from dataclasses import dataclass
from dotenv import load_dotenv
from datetime import datetime
from github import Github
import pandas as pd
import os

load_dotenv(".env", override=True)

def file_path(date):
    dir = "data/" + date.strftime("%Y/%m/")
    if not os.path.exists(dir):
        os.makedirs(dir)
    return os.path.join(dir, formate_date(date)+".csv")

def formate_date(date):
    return date.strftime("%Y%m%d")

@dataclass
class Repo:
    name: str
    ts: int
    stars_count: int = 0
    views_total: int = 0
    views_uniques: int = 0
    clones_total: int = 0
    clones_uniques: int = 0

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

days = dict()

github_repos = g.get_user().get_repos()
print("[", g.get_user().login, "]:", github_repos.totalCount, "repositories")
for repo in github_repos:
    name = repo.name

    views = repo.get_views_traffic()
    for v in views["views"]: 
        ts = formate_date(v.timestamp)
        if ts not in days:
            days[ts] = dict()
        if name not in days[ts]:
            days[ts][name] = Repo(name=name, ts=v.timestamp, stars_count=repo.stargazers_count)
        r = days[ts][name]
        r.views_total = v.count
        r.views_uniques = v.uniques

    clones = repo.get_clones_traffic()
    for c in clones["clones"]: 
        ts = formate_date(c.timestamp)
        if ts not in days:
            days[ts] = dict()
        if name not in days[ts]:
            days[ts][name] = Repo(name=name, ts=c.timestamp, stars_count=repo.stargazers_count)
        r = days[ts][name]
        r.clones_total = c.count
        r.clones_uniques = c.uniques

for d in days.keys():
    df = pd.DataFrame(data = [r.__dict__ for r in days[d].values()])
    ts = datetime.strptime(d, "%Y%m%d")
    df.to_csv(file_path(ts))
