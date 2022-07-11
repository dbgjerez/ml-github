from dataclasses import dataclass
from github import Github
import pandas as pd
import os

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

@dataclass
class Repo:
    name: str
    ts: int
    stars_count: int = 0
    views_total: int = 0
    views_uniques: int = 0
    clones_total: int = 0
    clones_uniques: int = 0

repos = dict()

github_repos = g.get_user().get_repos()
print("[ dbgjerez ]:", github_repos.totalCount, "repositories")
for repo in github_repos:
    name = repo.name

    views = repo.get_views_traffic()
    for v in views["views"]: 
        ts = v.timestamp.strftime("%Y/%m/%d")
        k = name + "-" + ts
        if k not in repos:
            repos[k] = Repo(name=name, ts=ts, stars_count=repo.stargazers_count)
        r = repos[k]
        r.views_total = v.count
        r.views_uniques = v.uniques

    clones = repo.get_clones_traffic()
    for c in clones["clones"]: 
        ts = c.timestamp.strftime("%Y/%m/%d")
        k = name + "-" + ts
        if k not in repos:
            repos[k] = Repo(name=name, ts=ts, stars_count=repo.stargazers_count)
        r = repos[k]
        r.clones_total = c.count
        r.clones_uniques = c.uniques

    
df = pd.DataFrame(data = [r.__dict__ for r in repos.values()], index=repos.keys())
df.to_csv('data.csv')