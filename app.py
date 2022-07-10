from github import Github

# using an access token
g = Github("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")

class Repo:
    name: str
    ts: int
    views_total: int
    views_uniques: int
    clones_total: int
    clones_uniques: int

data = []

for repo in g.get_user().get_repos():
    name = repo.name
    clones = repo.get_clones_traffic()
    views = repo.get_views_traffic()
    for v in views["views"]: 
        print(repo.name, " ==> ", v.timestamp, v.uniques, v.count)
    #print(repo.name, " ==> ", clones, " ===> ", views)