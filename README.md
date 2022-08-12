### Ссылка на GoogleSheets документ.
- https://docs.google.com/spreadsheets/d/1bgtvoIrVUw1WTJXzBGKzuCVXQ3ECASkqMBvyxv4wZR8/edit?usp=sharing
- Для получения доступа к документу, напишите мне в телегу (@mahamerz)

### Python

Установите Python версии 3.6 и выше.

### Зависмости

Установите все зависмости из файла requirements.txt


### Запуск программы

- Для запуска программы используйте файл **run.py**

- Для обновления базы данных с переносом данных с документа используйте файл **google_sheets.py**

<h4 align='center'>Установка</h4>
<p><b>Docker</b></p> 
Перед установкой убедитесь в том что ваша хост машина подерживает виртуализацию, и в том что она включена.

Для Windows: убедитесь в том что у вас включен компонент Hyper-V.

Затем скачайте и установите Docker, Docker-Compose

<h4 align='center'><p><b>Запуск</b></p> </h4>
Склонируйте репорзиторий к себе!<br>

<p><b>Для запуска программы используйте:</b></p> 

1.  docker build -t compose-flask .
2.  docker-compose up

Приложение доступно по адресу http://127.0.0.1:5000/

___________________________________________________________________________


Скрипт на языке Python 3, 

который выполняет следующие функции:

1. Получает данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1bgtvoIrVUw1WTJXzBGKzuCVXQ3ECASkqMBvyxv4wZR8/edit?usp=sharing).

2. Данные добавлены в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    a. DB, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли  получены по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме 
    

**Дополнительно:**

1. Код логичен и не перегружен, соблюдены отступы и логика названий переменных и структур данных.
2. Комментированность кода – комментарии понятны даже начинающему, и содержат достаточную информацию о функции, классе или методе.
3. ООП
4. Решения упаковано в docker контейнер  
5. Разработано одностраничное web-приложения на основе Flask.

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
