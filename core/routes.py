import datetime

from flask import render_template
from flask import current_app

from core import app
from core.models import Table
from core.convert import usd_rate


@app.route("/")
def index():
    table_entries = Table.query.all()
    rubles = [int(entry.dollar) * int(usd_rate) for entry in table_entries]
    items = [
        {
            "id": entry.id,
            "order": entry.order,
            "dollar": entry.dollar,
            "supply": entry.supply,
            "ruble": ruble,
        }
        for entry, ruble in zip(table_entries, rubles)
    ]

    return render_template("index.html", context=items)


def telegram(supply):
    current_time = datetime.datetime.utcnow()
    table_entry = Table.query.get(supply)

    if table_entry and current_time > table_entry.supply:
        send_telegram_notification(
            f"Supply time exceeded for order {table_entry.order}"
        )
    else:
        if table_entry is None:
            current_app.logger.warning(f"Table entry with supply {supply} not found.")
        else:
            current_app.logger.info(
                f"Supply time has not been reached for order {table_entry.order}."
            )


def send_telegram_notification(message):
    # код для отправки уведомления в телеграмм
    print(f"Telegram notification: {message}")
