
# install fkae8 and radon packages
pip install flake8 radon mccabe


# check for errors (file)
python -m flake8 lab10/file.py

# check for errors (folder)
python -m flake8 lab10/


# compute mccabe metric (file)
python -m mccabe lab10/file.py

# compute mccabe metric (folder)
python -m mccabe lab10/*


# compute Cyclomatic Complexity metric (file)
python -m radon cc lab10/file.py

# compute Cyclomatic Complexity metric (folder)
python -m radon cc lab10/


# compute raw metrics (file)
python -m radon raw lab10/file.py

# compute raw metrics (folder)
python -m radon raw lab10/


# compute the Maintainability Index (file)
python -m radon mi lab10/file.py

# compute the Maintainability Index (folder)
python -m radon mi lab10/
