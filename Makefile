CODE = src
TESTS = tests

ALL = $(CODE) $(TESTS)

VENV ?= venv

venv:
	python -m venv $(VENV)
	$(VENV)\Scripts\activate
	$(VENV)\Scripts\python -m pip install --upgrade pip
	$(VENV)\Scripts\python -m pip install poetry
	$(VENV)\Scripts\poetry install
#	python3 -m venv $(VENV)
#	$(VENV)/bin/python -m pip install --upgrade pip
#	$(VENV)/bin/python -m pip install poetry
#	$(VENV)/bin/poetry install


setup:
	$(VENV)\Scripts\python setup.py install



test:
	$(VENV)\Scripts\pytest -v tests
#   $(VENV)/bin/pytest -v tests


lint:
	$(VENV)\Scripts\flake8 --jobs 4 --statistics --show-source $(ALL)
	$(VENV)\Scripts\pylint --jobs 4 --rcfile=setup.cfg $(CODE)
	$(VENV)\Scripts\black --skip-string-normalization --check $(ALL)
#	$(VENV)/bin/flake8 --jobs 4 --statistics --show-source $(ALL)
#	$(VENV)/bin/pylint --jobs 4 --rcfile=setup.cfg $(CODE)
#	$(VENV)/bin/black --skip-string-normalization --check $(ALL)



format:
	$(VENV)\Scripts\isort --apply --recursive $(ALL)
	$(VENV)\Scripts\black --skip-string-normalization $(ALL)
	$(VENV)\Scripts\autoflake --recursive --in-place --remove-all-unused-imports $(ALL)
	$(VENV)\Scripts\unify --in-place --recursive $(ALL)
#	$(VENV)/bin/isort --apply --recursive $(ALL)
#	$(VENV)/bin/black --skip-string-normalization $(ALL)
#	$(VENV)/bin/autoflake --recursive --in-place --remove-all-unused-imports $(ALL)
#	$(VENV)/bin/unify --in-place --recursive $(ALL)


