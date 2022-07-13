Github provides us with an API to extract the last 14 days' stats over our repositories. 

This project aims to amplify and analyse them.

# Clean data
This repository contains my stats into ```data``` folder. You can remove it because you will generate your own data. 

# Get the data

To get the data you should use the ```app.py``` file. 

The best way to use it is using the virtual environment. 

## Configure

The application needs a GitHub token that grants privileges read-only over your public repositories. 

The application reads the token from ```.env``` file. You have to create the file ```.env``` with the following data:

```properties
GITHUB_TOKEN={your-token}
```

## Execute the code

Once you have created the ```.env``` file with the ```GITHUB_TOKEN``` variable, we can run the code.

The best way is using the virtual environment. If you don´t know how, I explaint it [here](https://blog.dbgjerez.es/posts/python-virtualenv/)

Execute the Python app: 

```zsh
❯ python app.py
```

The application will create a structure with one ```.csv``` per day:

```zsh
❯ ls -lchR data
data:
total 4,0K
drwxr-xr-x 4 db db 4,0K jul 12 19:03 2022

data/2022:
total 8,0K
drwxr-xr-x 2 db db 4,0K jul 12 19:03 06
drwxr-xr-x 2 db db 4,0K jul 13 06:34 07

data/2022/06:
total 12K
-rw-r--r-- 1 db db 164 jul 12 19:03 20220628.csv
-rw-r--r-- 1 db db 192 jul 13 12:22 20220629.csv
-rw-r--r-- 1 db db 272 jul 13 12:22 20220630.csv

data/2022/07:
total 52K
-rw-r--r-- 1 db db 257 jul 13 12:22 20220701.csv
-rw-r--r-- 1 db db 195 jul 13 12:22 20220702.csv
-rw-r--r-- 1 db db 237 jul 13 12:22 20220703.csv
-rw-r--r-- 1 db db 497 jul 13 12:22 20220704.csv
-rw-r--r-- 1 db db 493 jul 13 12:22 20220705.csv
-rw-r--r-- 1 db db 559 jul 13 12:22 20220706.csv
-rw-r--r-- 1 db db 614 jul 13 12:22 20220707.csv
-rw-r--r-- 1 db db 433 jul 13 12:22 20220708.csv
-rw-r--r-- 1 db db 238 jul 13 12:22 20220709.csv
-rw-r--r-- 1 db db 304 jul 13 12:22 20220710.csv
-rw-r--r-- 1 db db 402 jul 13 12:22 20220711.csv
-rw-r--r-- 1 db db 638 jul 13 12:22 20220712.csv
-rw-r--r-- 1 db db 357 jul 13 12:22 20220713.csv
```

## Makefile

In addition, a ```Makefile``` is provided, so you can use it: 

```zsh
make update
```

# Analysis the data

The file ```repos_analysis.ipynb``` execute a light analisys over the data. 

To update it, you have to use wherever editor that you prefer. In my case, I use ```junyper-notebook``` in local environments. 

```zsh
❯ jupyter nbconvert --execute --to notebook --inplace repos_analysis.ipynb
```

# References
* https://github.com/PyGithub/PyGithub
* https://blog.dbgjerez.es/posts/python-virtualenv/
