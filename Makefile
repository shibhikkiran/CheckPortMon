PYTHON_MODULES := checkportmon
PYTHONPATH := .
VENV := .venv
PYTEST := env PYTHONPATH=$(PYTHONPATH) PYTEST=1 $(VENV)/bin/py.test
PYLINT := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/pylint --disable=I0011 --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
PEP8 := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/pycodestyle --repeat --ignore=E202,E501,E402
AUTOPEP8 := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/autopep8 --aggressive --in-place --recursive  -v .
PYTHON := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/python
PIP := $(VENV)/bin/pip

DEFAULT_PYTHON := /usr/bin/python3
VIRTUALENV := /usr/local/bin/virtualenv

REQUIREMENTS := -r requirements.txt

default: check-coding-style

venv:
	test -d $(VENV) || $(VIRTUALENV) -p $(DEFAULT_PYTHON) -q $(VENV)

requirements:
	@if [ -d wheelhouse ]; then \
		$(PIP) install -q --no-index --find-links=wheelhouse $(REQUIREMENTS); \
	else \
		$(PIP) install -q $(REQUIREMENTS); \
	fi
bootstrap: venv requirements

check-coding-style: bootstrap
	$(PEP8) $(PYTHON_MODULES)
	$(PYLINT) -E $(PYTHON_MODULES)

pylint-full: check-coding-style
	$(PYLINT) $(PYTHON_MODULES)

autopep8-fix: check-coding-style
	$(AUTOPEP8)  

test: check-coding-style
	$(PYTEST) 

check:
	$(PYTEST) 

.PHONY: default venv requirements bootstrap check-coding-style pylint-full autopep8-fix test check
