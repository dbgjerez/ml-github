#!make
-include .env
.ONESHELL:

help: ## Show opstions and short description
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

update: ## Update repo stats by day
	python -m venv venv; source venv/bin/activate; venv/bin/pip install -r requirements.txt; venv/bin/python app.py; deactivate

.PHONY: update-repos
update-repos: ## Update repo global view
	python -m venv venv
	. venv/bin/activate; pip install -r requirements.txt; python repos.py; deactivate

.PHONY: notebook
notebook: ## Execute the notebook
	jupyter nbconvert --execute --to notebook --inplace repos_analysis.ipynb

.PHONY: git
git: ## Upload the changes to repository
	git add .
	git commit -m 'update process'
	git push

.PHONY: all
all: update update-repos notebook git
