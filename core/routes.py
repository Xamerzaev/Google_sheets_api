from flask import render_template
import datetime

from core import app
from core.models import db, Table
from core.convert import usd_rate


@app.route('/')
def index():
    # получаем все данные с таблицы
    table = Table.query.all()
    # список с рублями
    ruble = []

    # получаем доллар из таблицы
    dollar = db.session.query(Table.dollar)
    dollars = dollar.all()

    # конвертируем доллар в рубль
    for i in dollars:
        ruble.append(int(i[0]) * int(usd_rate))  # usd_rate - курс рубля

    items = [{"id": table[i].id, "order": table[i].order,
              "dollar": table[i].dollar, "supply": table[i].supply,
              "ruble": ruble[i]} for i in range(len(dollars))]
    return render_template('index.html',
                           context=items)


def telegram(supply):
    if datetime.datetime.now() > Table.query.get(supply):
        pass
