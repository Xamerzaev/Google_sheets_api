import os
from dotenv import load_dotenv
from datetime import datetime

from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import apiclient.discovery

from core.models import Table
from core import db

load_dotenv()


class GoogleSheetsConfig:
    credentials_file = os.getenv("CREDENTIALS_FILE")
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]


def get_google_sheets_service(config, http_auth=None):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        config.credentials_file, config.scopes
    )
    http_auth = http_auth or credentials.authorize(httplib2.Http())
    return apiclient.discovery.build("sheets", "v4", http=http_auth)


def read_google_sheets_data(service, range_="B2:D999", major_dimension="ROWS"):
    try:
        values = (
            service.spreadsheets()
            .values()
            .get(
                spreadsheetId=GoogleSheetsConfig.spreadsheet_id,
                range=range_,
                majorDimension=major_dimension,
            )
            .execute()
        )
        return values.get("values", [])
    except Exception as e:
        print(f"Error reading Google Sheets data: {e}")
        return []


def add_values_to_db(session, data):
    for row in data:
        try:
            order, dollar, supply_str = row
            supply = datetime.strptime(supply_str, "%d.%m.%Y")
            values = Table(order=order, dollar=dollar, supply=supply)
            session.add(values)
        except ValueError as ve:
            print(f"Error parsing data: {ve}")
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error committing to the database: {e}")


def main():
    config = GoogleSheetsConfig()
    try:
        # Авторизация и получение сервиса для работы с Google Sheets API
        service = get_google_sheets_service(config)

        # Чтение данных из файла Google Sheets
        values = read_google_sheets_data(service)

        # Сохранение данных в базу данных
        add_values_to_db(db.session, values)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
