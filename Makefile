-include .env
.PHONY: prepare_venv help update-stats update-repos update-notebook git all

VENV_NAME=venv
PYTHON=${VENV_NAME}/bin/python

help: ## Show opstions and short description
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	python -m $(VENV_NAME) $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate

update-stats: prepare_venv ## Update repo stats by day
	${PYTHON} app.py

update-repos: prepare_venv ## Update repo global view
	${PYTHON} repos.py

update-notebook: ## Execute the notebook
	jupyter nbconvert --execute --to notebook --inplace repos_analysis.ipynb

git: ## Upload the changes to repository
	git commit -am 'update process'
	git push

all: update-stats update-repos update-notebook git