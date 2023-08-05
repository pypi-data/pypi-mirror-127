# Steps to build a python package

- Create __init__.py file for each python folder/module and import the funcs, classes you want to expose
- Create setup.py file
- python setup.py sdist bdist_wheel
- python -m pip install twine
- python -m twine upload dist/*
- Change version for each new upload