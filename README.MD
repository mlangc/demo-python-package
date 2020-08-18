# Demo Python Package for Demo Purposes
## Setup develop environment
```shell script
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Simple type `deactivate` into the shell, to leave the development environment.

## Execute tests
```shell script
pytest
```

## Build wheel package that can be installed with pip
```shell script
python3 setup.py bdist_wheel
```
The resulting wheel package in `dist` can be installed with `pip` like so:
```shell script
pip install demo_python_package-0.0.2-py3-none-any.whl
```
## Install directly from git repository
```shell script
pip install git+https://github.com/mlangc/demo-python-package.git
```