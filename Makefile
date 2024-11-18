# SPDX-FileCopyrightText: 2024 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

clean:
	find . -name "*~" | xargs rm -f
	rm -fr licomp_osadl.egg-info
	rm -fr build
	rm -fr dist sdist
	rm -fr licomp_osadl/__pycache__
	rm -fr tests/__pycache__
	rm -fr .pytest_cache

py-lint:
	PYTHONPATH=. flake8 flame

build:
	rm -fr build && python3 setup.py sdist

test:
	PYTHONPATH=. python3 -m pytest --log-cli-level=10 tests/

test-local:
	PYTHONPATH=.:../licomp python3 -m pytest --log-cli-level=10 tests/

install:
	pip install .

reuse:
	reuse lint

update-matrix:
	curl -LJ "https://www.osadl.org/fileadmin/checklists/matrixseqexpl.json" -o licomp_osadl/var/matrixseqexpl.json
