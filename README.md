### Описание проекта "Google Sheets API"

**Ссылка на Google Sheets документ:**
- [Google Sheets Document](https://docs.google.com/spreadsheets/d/1bgtvoIrVUw1WTJXzBGKzuCVXQ3ECASkqMBvyxv4wZR8/edit?usp=sharing)
- Для получения доступа к документу, свяжитесь со мной в Telegram (@mahamerz).

### Установка и Зависимости

Установите Python версии 3.6 и выше.

Установите все зависимости из файла `requirements.txt` с помощью команды:
```bash
pip install -r requirements.txt
```

### Запуск программы

- Для запуска программы используйте файл **run.py**.
- Для обновления базы данных с переносом данных с документа используйте файл **google_sheets.py**.

### Docker

Перед установкой убедитесь, что ваша хост-машина поддерживает виртуализацию и включена.

**Для Windows:**
Убедитесь, что у вас включен компонент Hyper-V.

Затем скачайте и установите Docker и Docker-Compose.

### Запуск с использованием Docker

1. Склонируйте репозиторий к себе.
2. Выполните команды:
    ```bash
    docker build -t compose-flask .
    docker-compose up
    ```

Приложение будет доступно по адресу http://127.0.0.1:5000/.

### Скрипт на Python 3

Скрипт выполняет следующие функции:

1. Получает данные с документа при помощи Google API, сделанного в [Google Sheets Document](https://docs.google.com/spreadsheets/d/1bgtvoIrVUw1WTJXzBGKzuCVXQ3ECASkqMBvyxv4wZR8/edit?usp=sharing).

2. Данные добавляются в базу данных (PostgreSQL) в том же виде, что и в файле-источнике, с добавлением колонки "стоимость в руб.".
    - Данные для перевода $ в рубли получены по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).

3. Скрипт работает постоянно для обеспечения обновления данных в онлайн-режиме.


### Языки и инструменты использованные в данном проекте:
  <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="40" height="40"/>&nbsp;

  <img src="https://github.com/devicons/devicon/blob/master/icons/mysql/mysql-original-wordmark.svg" title="MySQL"  alt="MySQL" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/git/git-original-wordmark.svg" title="Git" alt="Git" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/flask/flask-original-wordmark.svg" title="Flask" alt="Flask" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-original.svg" title="Bootstrap" alt="Bootstrap" width="40" height="40"/>&nbsp;
  <img src="https://github.com/devicons/devicon/blob/master/icons/google/google-original.svg" title="GoogleApi" alt="Google" width="40" height="40"/>&nbsp;
  
Проект также включает в себя одностраничное веб-приложение на основе Flask.

### Дополнительная информация

- Код логичен и не перегружен, соблюдены отступы и логика названий переменных и структур данных.
- Комментированность кода – комментарии понятны даже начинающему, и содержат достаточную информацию о функции, классе или методе.
- ООП (Объектно-Ориентированное Программирование).
- Решения упакованы в Docker контейнер.