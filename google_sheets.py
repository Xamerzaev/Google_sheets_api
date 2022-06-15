from datetime import date, datetime
from pprint import pprint

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
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


# чтение order файла
order = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='B2:B51',
    majorDimension='COLUMNS'
).execute()


# чтение dollar файла
dollar = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='C2:C51',
    majorDimension='COLUMNS'
).execute()

# чтение supply файла
supply = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='D2:D51',
    majorDimension='COLUMNS'
).execute()


def add_values_to_db(order, dollar, supply):

    """   
    Функция заполнения данными  БД     
    
    """

    values = Table(order, dollar, supply)
    db.session.add(values)
    db.session.commit()

add_values_to_db(order, dollar, supply)