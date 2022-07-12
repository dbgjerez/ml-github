#!make
-include .env

.PHONY: help 
help: ## Show opstions and short description
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: update
update: ## Update repo stats
	python -m venv venv
	. venv/bin/activate; pip install -r requirements.txt; python app.py; deactivate

.PHONY: notebook
notebook: ## Execute the notebook
	jupyter nbconvert --execute --to notebook --inplace repos_analysis.ipynb

.PHONY: git
git: ## Upload the changes to repository
	git add .
	git commit -m 'update process'
	git push

.PHONY: all
all: update notebook git
