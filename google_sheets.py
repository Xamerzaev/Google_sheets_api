from datetime import datetime

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

from core.models import Table
from core import db

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1bgtvoIrVUw1WTJXzBGKzuCVXQ3ECASkqMBvyxv4wZR8'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


# чтение файла
valuess = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='B2:D999',
    majorDimension='ROWS'
).execute()

# сохраняем данные в дб


def add_values_to_db():
    for i in valuess['values']:
        order = i[0]
        dollar = i[1]
        supply = i[2]
        supply = datetime.strptime(supply, "%d.%m.%Y")
        values = Table(order=order, dollar=dollar, supply=supply)
        db.session.add(values)
        db.session.commit()


add_values_to_db()
