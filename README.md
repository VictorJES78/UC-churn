# Détection de churn exemple

1. Créer un environnement conda sous Python 3.9
2. `pip install -r requirements.txt`
3. Dans le fichier config indiquer le chemin de sauvegarde des runs Mlflow dans la variable ML_FLOW_PATH
4. `python main.py --log-level INFO --data-set chemin/données`

# TEMPLATE PROJET

## 1 - TODO FIRST

1. Clone the template project where you want `git clone https://gitlab...` 
2. Rename the project (template_projet) with the same project name as before (`mv template_projet <my_project>`)
3. Go into the project folder: `cd my_project`
4. Delete existing git tracking: `rm -rf .git`

## 2 - TODO GIT INIT

1. Init a new git tracking: `git init --initial-branch=main`
2. In gitlab interface, create a project (New project), choose 'Create blank project' and fill the blanks (Internal visibility level is OK, uncheck "
Initialize repository with a README". In "Pick a group or namespace" it's better to choose a group if you work with a team, if you work on your own project choose your pnom). Choose a project name (let's call it *my_project* here)
3. Add the remote you create in the first place (**at step 1**): `git remote add origin https://gitlab...`
4. Add all the files: `git add .` (you can check what you are about to add by running `git status` just before, which is recommended)
5. Commit the changes: `git commit -m "initial commit"`
6. Puhs (after reading warning): `git push origin master`. /!\Warning/!\: distant repository might have "main" branch instead of "master" (check on gitlab). If you want to have the same name locally rename you local "master" branch to "main" before pushing: `git branch -m master main`
7. You're done, congrats! Now follow the next todo

## 3 - TODO ADDITIONAL
1. Rename your source code folder with the name of your project (current is "src")
2. Add notebooks/* and logs/* to .gitignore file
3. If you do not use docker (e.g. in aws env), create a python environment for your project. You don't have to put this environment inside your project folder. If you do so your should add the folder to .gitignore file. Otherwise you can have this folder outside the project folder in a dedicated folder for instance.
4. Run `pip install --upgrade pip` then `pip install -r requirements`
5. You can run `python main.py` on terminal to see if you have "hello world" printed :)

## REMINDER OF GOOD PRACTICES FOR CODING
- **Use modular coding practice**: organise your code using modules, functions and class. Think your code in terms of pipeline "what's in what's out" 
- **Comment** your code and **document** all your functions 
- **Unit test** your code the most or at least the most critical function 
- Create **new branch** on git each time you develop **new feature** 
- Find a partner to **review your code**. Should be at least 2 hours (straight or 2*1h) a week on scheduled timeshifts 
- Follow the **google coding style** for harmonized practices : https://google.github.io/styleguide/pyguide.html
- Use **black** (https://github.com/psf/black) to format your code automatically before commit: `black src`
- You should use **notebooks** for **exploratory analysis and testing part of your code only**. If you don't have other choice than using notebook for your project please remove notebooks folder from .gitignore file
- All your imports should start by the project source code folder's name:
```
from src.XXXX import XXXX
```
or
```
from src import XXXX
```
- Log your code: the main.py contains the logger. It can be used in any module by juste using logging api
```
import logging
logging.info("my log message")
```
- The organisation inside your source code folder (src) is not mandatory, feel free to reorganize differently. Pay attention to how intuitive the code is.
- Use this README to provide information on how to use your code for other users or developpers

## USAGE OF THE OTHER FILES
- .gitlab-ci.yaml: TO BE COMPLETED
- requirements.txt : file that contains all the packages and their version used for the project
