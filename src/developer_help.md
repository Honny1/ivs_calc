# Developer help

## Before developing

### Install requirements

```bash
pip3 install -r requirements.txt
```

### Setup git

- [setup basic git info](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
- [generate ssh key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [setup ssh key on github](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

### Get repo

**Use SSH url for clone and setup upstream** [Fork repo tutorial](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo)

### Before start developing

```bash
git checkout -b name_new_branch
# Then develop

# If work is done.
git add changed_files
# or
git add -p

git commit 

git push origin name_new_branch
# Then continue on github (tutorial -> https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
```

### Get new future form upstream

```bash
git checkout master
git pull upstream master
git push origin master
```

## Run from source

```bash
# run command duck-calc
python3 -m duck_calc.main 
```

## Install a project in editable mode

(i.e. setuptools "develop mode") from a local project path or a VCS url

```bash
pip3 install -e .    
```

## Execute the test suite

There are many test options for syntax, code, code coverage.

### Before testing install requirements

```bash
pip3 install -r requirements.txt
```

### Test all that stuff together with tox

Run tests:

```bash
tox
```

>If requirements changes ```tox -r``` (recreates virtual environment) can help.

```bash
# Show coverage report
firefox htmlcov/index.html
```

You can run test for more python environments with command like this one:

```bash
tox -e py36,py37,py38,py39
```

### Test code and code coverage with pytest

Run tests:

```bash
python3 -m pytest
```

Run tests coverage:

```bash
python3 -m pytest --cov duck_calc --cov-report html --cov-branch

# Show coverage report
firefox htmlcov/index.html
```

### Test syntax

Run syntax tests:

```bash
flake8 ./duck_calc ./tests setup.py

#OR

pylint ./duck_calc ./tests setup.py
```

## Useful Tools and links

- [autopep8](https://pypi.org/project/autopep8/)
- [Virtual Enviroment](https://docs.python.org/3/tutorial/venv.html)
- [qt5 designer for python](https://realpython.com/qt-designer-python/)
- [pytests](https://realpython.com/pytest-python-testing/)
- [Rebase branch](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
