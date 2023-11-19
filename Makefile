# Makefile
# Переменные
PYTHON=python3
PIP=pip3
DOCKER=docker
FLASK_APP=app.py
FLASK_ENV=development

# Цели
install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(FLASK_APP)

docker-build:
	$(DOCKER) build -t compose-flask .

docker-run:
	$(DOCKER)-compose up
