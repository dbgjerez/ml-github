from dataclasses import dataclass
from unicodedata import name
from dotenv import load_dotenv
from datetime import datetime
from github import Github
import pandas as pd
import os

load_dotenv(".env", override=True)

def format_date(date):
    return date.strftime("%Y%m%d")

@dataclass
class Refer:
    repo: str
    ts: str
    name: str
    total: int = 0
    uniques: int = 0

token = os.getenv('GITHUB_TOKEN')
g = Github(token)

github_repos = g.get_user().get_repos()

print("[", g.get_user().login, "]:", github_repos.totalCount, "repositories")

refers = []
for repo in github_repos:
    for refer in repo.get_top_referrers():
        refers.append(Refer(repo=repo.name, ts=format_date(datetime.now()), name=refer.referrer, total=refer.count, uniques=refer.uniques))

df = pd.DataFrame(data = [r.__dict__ for r in refers])
df.to_csv("data/refers.csv")