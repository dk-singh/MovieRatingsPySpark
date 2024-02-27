PY_VERSION=3.8.10
PYENV_NAME=movie-rating
PYENV=~/.pyenv/versions/${PY_VERSION}/envs/${PYENV_NAME}/bin

build-pyenv:
	pyenv install -s ${PY_VERSION}
	pyenv virtualenv -f ${PY_VERSION} ${PYENV_NAME}
	${PYENV}/pip install --no-cache-dir -U pip
	${PYENV}/pip install --no-cache-dir -U pip-tools
	${PYENV}/pip install --no-cache-dir -U pip-tools
	${PYENV}/pip install --no-cache-dir -e ".[dev]"

requirements:
	pip-compile --no-annotate --no-emit-index-url --output-file requirements.txt setup.py

install:
	pip install --no-cache-dir -r requirements.txt

run:
	python src/apps/movie_rating_app.py

format:
	isort setup.py src/ test/
	black setup.py src/ test/

lint:
	python -m flake8 setup.py src/ test/

coverage:
	python -m coverage run --source=src --branch -m pytest -sv test --junitxml=build/test.xml -v
	python -m coverage xml -i -o build/coverage.xml
	python -m coverage report

test: lint coverage

test-unit:
	python -m pytest -sv test/unit

test-e2e:
	python -m pytest -sv test/e2e