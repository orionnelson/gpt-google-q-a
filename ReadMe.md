# This Repo Scrapes Google then Runs it Through GPT-J-6b
Ask a question you would usually ask google then run it through a google search and language model to extract the results.
- Example 
```How Old is Barack Obama where and when was he Born?```
 President of the United States of America was born August 4, 1961 in Honolulu, Hawaii, the youngest 
of three children. Barack Obama Jr. was born at 6:11 a.m. in the maternity ward of Queen's Medical Center. The president's biological mother, Barack Obama Sr., was a student at the University of Hawaii. She was 18 and he was 24 when Barack Sr. and his infant son were married in 1964.
- Note GPT-J-6B often faces issues with identity resolution. 

## Clone and Checkout Repo of Branch
```
git clone https://github.com/orionnelson/gpt-google-q-a.git
git checkout -b myawesome_new_feature
```

## Set up python virtual Environment
```
python or python3 -m venv feature_branch_or_venv_name 
```
## Add Feature env name to gitignore else 
```
git rm -r my_venv/ --cached fix after git add -A
```
## Activate Venv 
source bin/activate in linux location or Scripts/activate.bat in windows
```
python or python3 -m pip install -r requirements.txt
```

## Run the demo
```
python content_retrieval.py
```

## Add Your Changes
```
git add -A
git diff --name-only # To preview changed files
git commit -m "This is what i changed"
git push # follow instruction of push message
```
